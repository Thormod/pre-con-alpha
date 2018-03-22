from phpGenerator.baseGenerator import generateNavbar
from sqlGenerator.queryGenerator import queryGenerator

baseHtml = """
<html>
<head>
    <title>directory.add</title>
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
	<div class="well">
	--FORM--
		--VARIABLES--
		--BUTTON--
	</form>
	</div>
	</div>
	</div>
	</div>
</body>
</html>
"""

basePhp = """
<html>
<head>
	<title>Add Data</title>
</head>

<body>
<?php
//including the database connection file
include_once("../base.php");
include_once("../config.php");

if(isset($_POST['Submit'])) {
	--VARIABLES--	
	// checking empty fields
	if(--IFSTATEMENT--) {
		--IFACTION--
		//link to the previous page
		echo "<br/><a href='javascript:self.history.back();'>Go Back</a>";
	} else { 
		$sql = "--QUERY--";
		if(mysqli_query($conn, $sql)){
			header("Location: ./index.php");
			exit();
		} else{
			echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
		}
	}
}
?>
</div>
</body>
</html>
"""


def addHtmlGenerator(data, conceptClass, dynamicRelationshipName):
	targetClass = data['concept_class'][conceptClass]
	primaryKey = targetClass['constraints']['pk']		
	filePath = './generated_files/www/'+conceptClass+'/'+dynamicRelationshipName+'.html'
	f = open(filePath,'w')
	submitStructure = ''
	formStructure = '<form action="'+dynamicRelationshipName+'.php" method="post" name="form1" role="form">'
	buttonStructure = '<button type="submit" class="btn btn-default btn-md btn-block" name="Submit">'+dynamicRelationshipName+'</button>'
	for j in targetClass:
		if j != 'constraints' and j != primaryKey:
			submitStructure +='<div class="form-group"><label>'+j.upper()+'</label><input class="form-control" type="text" name="'+j+'"></div>'
	content = baseHtml.replace('--VARIABLES--', submitStructure)
	content = content.replace('--NAVS--', generateNavbar(data))
	content = content.replace('--FORM--', formStructure)
	content = content.replace('--BUTTON--', buttonStructure)
	f.write(content)
	f.close()

def addPhpGenerator(data, conceptClass, dynamicRelationshipName):
	query = queryGenerator(data, 'insert', conceptClass, '')
	targetClass = data['concept_class'][conceptClass]
	primaryKey = targetClass['constraints']['pk']		
	filePath = './generated_files/www/'+conceptClass+'/'+dynamicRelationshipName+'.php'
	f = open(filePath,'w')
	variableStructure = ''
	ifStatementStructure = ''
	ifActionStructure = ''
	for j in targetClass:
		if j != 'constraints' and j != primaryKey:
			ifStatementStructure += 'empty($'+j+') || '
			variableStructure += "$"+j+" = $_POST['"+j+"'];\n"
			ifActionStructure += 'if(empty($'+j+')) {echo "<font color='+"'red'"+'>'+j+' field is empty.</font><br/>";}\n'
	content = basePhp.replace('--VARIABLES--', variableStructure)
	content = content.replace('--IFSTATEMENT--', ifStatementStructure[:-4])
	content = content.replace('--IFACTION--', ifActionStructure)
	content = content.replace('--QUERY--', query)
	f.write(content)
	f.close()

def addGenerator(data, conceptClass, dynamicRelationshipName):
	addHtmlGenerator(data, conceptClass, dynamicRelationshipName)
	addPhpGenerator(data, conceptClass, dynamicRelationshipName)