base = """
<html>
<head>
<title>ADD</title>
<meta charset="utf-8"> 
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<link href="/css/main.css" rel="stylesheet">
<link href="/css/font-awesome.min.css" rel="stylesheet" type="text/css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

</head>
<body>
<nav class="navbar navbar-default">
<div class="container-fluid">
<!-- Brand and toggle get grouped for better mobile display -->
<div class="navbar-header">
<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="#">Pre-concept-Alpha</a>
</div>
<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
<ul class="nav navbar-nav">
--NAVS--
</div><!-- /.navbar-collapse -->
</div><!-- /.container-fluid -->
</nav>

<div class="container">
<div class="row">
<div class="col-xs-6 col-xs-offset-3">

"""

def generateNav(data):
  navsStructure = ''
  for i in data:
        navsStructure += '<li><a href="/'+i+'/index.php">'+i.upper()+'</a></li>'
  return navsStructure
  
def generateBase(data):
    filePath = './generated_files/www/base.php'
    f = open(filePath,'w')    
    content = base.replace('--NAVS--', generateNav(data))
    f.write(content)
    f.close()
