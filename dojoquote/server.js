var express = require('express');
var app = express();
var mongoose= require('mongoose');
mongoose.connect('mongodb://localhost/basic_mongoose');
var UserSchema = new mongoose.schema({
  name:"string";
  age: "12";
})
var bodyParser = require('body-parser');
var path = require('path');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
app.get('/', function(req,res){
  res.render('index');
});
app.post('/quotes', function(req.res){
  var user = {
    name : req.body.name;
  }
  var userQuote = {
    userQuote: req.body.quote;
  }
  res.render('quotes');
});

app.get ('/quotes', function(req,res){
  res.render('quotes');
});


app.listen(8000, function(){
  console.log("Now listening on port 8000");
})
