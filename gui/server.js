const express = require('express')
const pug = require('pug');
var bodyParser = require('body-parser');
const app = express()
const port = 8080

app.set("view engine", "pug")
app.use(express.static('public'))

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

let commands = ["hello", "yay"]

app.get('/', (req, res) => res.render('gui', {commands}))

app.post('/save-command', function(req, res) {
    console.log(req.body);
    commands.push(req.body.command);
    res.json({message:"New command added"})
})
app.post('/delete-command', function(req, res) {
    console.log(req.body);
    commands = commands.filter(e => e !== req.body.command);
    res.json({message:"Command deleted"})
})


app.listen(port, () => console.log(`Example app listening on port ${port}!`))