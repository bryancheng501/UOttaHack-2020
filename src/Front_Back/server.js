//server
const express = require('express');
const busboy = require('connect-busboy');
const path = require('path');
const fs = require('fs-extra');
const mime = require('mime');

const spawn = require("child_process").spawn;
let app = express();

app.use(express.urlencoded({extended: true}));
app.use(busboy());
app.use(express.static(__dirname + "/public"));
//app.user(express.json());
let fileName = '';

app.get('/returnPokemon', returnPokemon);
//app.get('/process', process);
app.post('/upload', upload);

function upload(req, res, next){
  var fstream;
  req.pipe(req.busboy);
  req.busboy.on('file', function(fieldname, file, filename, encoding, mimetype){
    fileName = filename;
    console.log(fileName);
    fstream = fs.createWriteStream("C:/Users/harol/Documents/UOttaHack-2020/src/" + fileName);
    file.pipe(fstream);
    fstream.on('close', function(){
      console.log("Upload finished of " + fileName);
    })
  })
}


function returnPokemon(req, res, next){
  const pythonProcess = spawn('python', [__dirname + 'ml.py', fileName], function(err, stdout, stderr){
    console.log(stdout);
  });
}

// function process(req, res, next){
//   fileName =
// }


app.listen(3000, function(){
  console.log('server running on port 3000');
})
