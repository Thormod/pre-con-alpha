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

indexBase = """
<html>
<head>
	<title>INDEX</title>
</head>

<body>
<?php
//including the database connection file
include_once("./base.php");
?>
</div>
</body>
</html>
"""

def generateDropdowns(dynamic_relationships):
  dropdownStructure = ''
  for i in dynamic_relationships:
    dropdownStructure += '<li class="dropdown">'
    dropdownStructure += '<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">'+i.upper()+'<span class="caret"></span></a>'
    dropdownStructure += '<ul class="dropdown-menu">'
    for j in dynamic_relationships[i]:
      if(dynamic_relationships[i][j]['type'] == 'add'):
        dropdownStructure += '<li><a href="/'+dynamic_relationships[i][j]['class']+'/'+j+'.html">'+j+'</a></li>'
      else:
        dropdownStructure += '<li><a href="/'+dynamic_relationships[i][j]['class'].split('.')[0]+'/'+j+'.php">'+j+'</a></li>'
    dropdownStructure += '</ul>'    
    dropdownStructure += '</li>'
  return dropdownStructure

def generateNavs(class_concepts):
  navsStructure = ''
  for i in class_concepts:
        navsStructure += '<li><a href="/'+i+'/index.php">'+i.upper()+'</a></li>'
  return navsStructure

def generateNavbar(data):
  navbarStructure = ''
  navbarStructure += generateDropdowns(data['dynamic_relationship'])
  navbarStructure += generateNavs(data['concept_class'])
  return navbarStructure
  
def generateIndex():
  filePath = './generated_files/www/index.php'
  f = open(filePath,'w') 
  f.write(indexBase)
  f.close()  

def generateBase(data):
  filePath = './generated_files/www/base.php'
  f = open(filePath,'w')    
  content = base.replace('--NAVS--', generateNavbar(data))
  f.write(content)
  f.close()
  generateIndex() 
