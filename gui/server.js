const express = require('express');
const pug = require('pug');
var bodyParser = require('body-parser');
var request = require('request-promise');
const app = express()
const port = 8080

app.set("view engine", "pug") // declara el engine de pug, no funcionará sin el view engine.
app.use(express.static('public')) // accede a la carpeta 'public'.

app.use(bodyParser.urlencoded({ extended: false })); // declares encoding example: UTF-8
app.use(bodyParser.json()); // declares to use json FORMAT

let commands = []
let lmr = commands // Solo lo puse para formatear el payload y para que se mire más como el mock up.

app.get('/postdata', async function (req, res) {
    let date_ob = new Date(); // All vars to get the time_stamp
    let date = ("0" + date_ob.getDate()).slice(-2);
    let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
    let year = date_ob.getFullYear();
    let hours = date_ob.getHours();
    let minutes = date_ob.getMinutes();
    let seconds = date_ob.getSeconds();

    const request_timestamp = month + " " + date + " " + hours+":"+minutes+":"+seconds + " " + year

    var data = { request_timestamp, lmr }

    var options = {
        method: 'POST',
        uri: 'http://0.0.0.0:5000/lex',
        body: data, 
        json: true // Automatically stringifies the body to JSON
    };

    var returndata;
    var sendrequest = await request(options)
        .then(function (parsedBody) {
            console.log(parsedBody); // parsedBody contains the data sent back from the Flask server
            returndata = parsedBody; // do something with this data, here I'm assigning it to a variable.
        })
        .catch(function (err) {
            console.log(err);
        });

    res.send(returndata);

});

//////////////////////////////////////////////////////////////////////////////////////////////////

app.get('/', (req, res) => res.render('gui', { commands }));
// .get genera una página, res.render = render template en flask, renderiza la página gui,
// busca solo el nombre sin extension


app.post('/save-command', function (req, res) { // metodos de app, "en la pagina principal que estes dice que haga post a la hora de acceder /save-command"
    console.log(req.body);
    commands.push(req.body.command); // red.body.command: el contenido que este adentro de push lo meta a commands. COMMAND es newComand
    res.json({ message: "New command added" });
})
app.post('/delete-command', function (req, res) { // solo funciona cuando se accede /save command, 
    console.log(req.body);
    commands = commands.filter(e => e !== req.body.command); // filter es BUSCA Y QUITA CIERTA VARIABLE, regresa el mensaje de command deleted.
    res.json({ message: "Command deleted" });
})

app.post('/delete-all', function (req, res) { // manda un mensaje a la terminal para saber lo que está pasando
    console.log(req.body); 
    commands = []; // declara que comands es NADA
    res.json({ message: "Commands deleted" });
})

app.listen(port, () => console.log(`App listening on port ${port}!`))
