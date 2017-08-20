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








var server = app.listen(port, function(){
    console.log("Now listening on port ${ port }")
});
var io = require('socket.io').listen(server);

io.sockets.on('connection', function(socket){
    socket.on("button_clicked", function(data){
      console.log("Someone clicked a button! Reason:" +data.reason);
      socket.emit('server_response', {response: "sockets are the best!"});
    });
    console.log("Client/socket is connected!");
    console.log("Client/socket id is:", socket.id);
    socket.on("posting_form", function(data){
        console.log("Someone submitted a form"+ data.name + data.location + data.Favoritelang);
        socket.emit('updated_message', function(){
            console.log(Math.floor(math.random()*100000));
        })
    })
  });
  