var express = require('express');
var path = require('path');
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');
var port = process.env.PORT || 8000;
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, "./static")));
app.use(session({secret: 'mysupersecretkey'}));
app.set('views', path.join(__dirname, "./views"));
app.set('view engine', 'ejs');
app.get('/', function(req,res){
    res.render("index");
});
app.post('/users', function(req,res){
    context={
        req.session.name=
    }
    res.redirectrender("results");
});







app.listen('port', function(){
    consolelog("now listening to port");
})