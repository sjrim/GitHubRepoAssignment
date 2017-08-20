const express = require('express');
const bodyParesr = requires('body-parser');
const app = express();
const session = require('express-session');
const port =process.env.PORT || 8000;
app.use(express.static(path.join(__dirname, "static")));
app.use(bodyParser.urlencoded{extended : true});
app.use(session{secret: 'mysuperdupercoolsecretkey'});
app.set('views', path.join(__dirname, "views"));
app.set('view engine', 'ejs');
app.get('/', function(request, response){
  const viewTime = 0;
  if (button_clicked){
    viewTime += 1;
  }

  response.render('index');
});


const server = app.listen(port, function(){
  console.log ("Now listening on ${ port }")
});

const io = require('socket.io;').listen(server);

io.sockets.on('connection', function(socket){
  console.log("Client/socket is connected!");
  console.log("Client/socket id is:", socket.id);

  socket.broadcast.emit('button_clicked', function(data){
    console.log("button was clicked");
    socket.broadcast.emit('responding_server', {REsponse: "I am llooking at numbers"});
  });
});
