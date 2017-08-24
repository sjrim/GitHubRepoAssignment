var express = require("express");
var app = express();
var path = require('path');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var port = 8000;

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
mongoose.connect('mongodb://localhost/otters_db');

var OtterSchema = new mongoose.Schema({
 name: { type: String, required: true, minlength: 3 },
 age: Number,
 size: String
});
mongoose.model('Otter', OtterSchema);
var Otter = mongoose.model('Otter');

app.get('/', function(req, res) {
	Otter.find({}, function(err, results) {
		if (err){
			console.log(err);
		} else {
			res.render('index', {otters: results})
		}
	});
});

app.get('/new', function(req, res){
	res.render('new')
})
app.post('/', function(req, res){
	var otter = new otter(req.body);
	otter.save(function(err){
		if (err){
			res.render('new', {title: 'you have errors!', errors: otter.errors})
		} else {
			res.redirect('/')
		}
	})
});
app.get('/:id', function(req, res){
	otter.find({ _id: req.params.id }, function(err, otter){
		if (err){
			console.log(err);
		} else {
			res.render('show', {otter: otter[0]});
		}
	});
});
app.get('/:id/edit/', function(req, res){
	otter.find({ _id: req.params.id }, function(err, otter){
		if (err){
			console.log(err);
		} else {
			res.render('edit', {otter: otter[0]});
		}
	});
});
app.post('/otters/:id', function(req, res){
	otter.update({ _id: req.params.id }, req.body, function(err, otter){
		if (err){
			console.log(err);
		} else {
			res.redirect('/')
		}
	});
});
app.post('/:id/destroy', function(req, res){
	otter.remove({ _id: req.params.id }, function(err, result){
		if (err){
			console.log(err);
		} else {
			res.redirect('/')
		}
	});
});

app.listen(port, function() {
	 console.log("listening on port " + port);
})
