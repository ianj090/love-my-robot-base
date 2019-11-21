const express = require('express')
const pug = require('pug');
var bodyParser = require('body-parser');
var request = require('request-promise');
const app = express()
const port = 8080

app.set("view engine", "pug")
app.use(express.static('public'))

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

let commands = []

app.get('/postdata', async function (req, res) {
    var data = { // this variable contains the data you want to send
        data1: "yup",
        data2: "bar"
    }

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

app.get('/', (req, res) => res.render('gui', { commands }))

// app.post("/postdata", (req, res) => {
//     var code = req.body.status;
//     console.log(code);
//     res.send("Successful");
// }); // Esta parte no es muy importante en nuestro caso (solo lo puse por si acaso)


// app.get("/getdata", (req, res) => {
//     var data = {};
//     res.status(200).json(data)
// });

// app.post("/send_data", function(req, res) {
//     app.get("/getdata", (req, res) => {
//         var data = { // this is the data you're sending back during the GET request
//             action: "say",
//             text: "hello world"
//         }
//         res.status(200).json(data)
//     });
// })



app.post('/save-command', function (req, res) {
    console.log(req.body);
    commands.push(req.body.command);
    res.json({ message: "New command added" })
})
app.post('/delete-command', function (req, res) {
    console.log(req.body);
    commands = commands.filter(e => e !== req.body.command);
    res.json({ message: "Command deleted" })
})
app.post('/delete-all', function (req, res) {
    console.log(req.body);
    let some = req.body + '';
    var block = some.split(" ");
    for (item in block) {
        commands = commands.filter(e => e !== req.body.command);
    }
    res.json({ message: "Commands deleted" })
})


app.listen(port, () => console.log(`App listening on port ${port}!`))
