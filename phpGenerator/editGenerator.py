from sqlGenerator.queryGenerator import queryGenerator

base = """
<?php
// including the database connection file
include_once("../config.php");
include_once("../base.php");
$query = "--SELECTQUERY--"; 
$result = mysqli_query($conn, $query);
echo "--FORMSTRUCTURE--";
echo "<div class='form-group'>";
echo "<label for='sel1'>Select list (select one):</label>";
echo "<select class='form-control' id='sel1' name='sel1'>";
if ($result->num_rows > 0) {
    // output data of each row
    while ($row = $result->fetch_assoc()) {
        --SELECTVARIABLES--
    }
}
echo "</select>";
echo "<br><button type='submit' class='btn btn-default btn-md btn-block' name='Submit'>SELECT</button>";
echo "</form>";
echo "</div>";
echo "</body>";
echo "</html>";
"""

baseAction = """
<?php
// including the database connection file
include_once("../config.php");
include_once("../base.php");

if (isset($_POST['update'])) {
	$id = $_POST['id'];
	--VARIABLESTRUCTURE--
	$sql = "--QUERY--'$id'";
    if(mysqli_query($conn, $sql)){
        header("Location: ./index.php");
        exit();
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }
}

if(isset($_POST['sel1'])){
    $id = $_POST['sel1'];
    echo "--FORMSTRUCTURE--";
    echo "<div class='form-group'>";
    echo "--LABELSTRUCTURE--";
    echo "--INPUTSTRUCTURE--";
    echo "</div>";
    echo "--BUTTONSTRUCTURE--";
    echo "</form>";
}   
"""

def editBaseGenerator(data, conceptClass, dynamicRelationshipName, targetVariable):
    targetClass = data['concept_class'][conceptClass]
    primaryKey = targetClass['constraints']['pk']	
    selectQuery = queryGenerator(data, 'select-variables', conceptClass, [primaryKey], '')
    query = queryGenerator(data, 'select-variables', conceptClass, [targetVariable], '')
    filePath = './generated_files/www/'+conceptClass+'/'+dynamicRelationshipName+'.php'
    f = open(filePath,'w')
    content = base.replace('--SELECTQUERY--', selectQuery)
    selectVariableStructure = "unset($"+primaryKey+"); $"+primaryKey+" = $row['"+primaryKey+"'];"
    selectVariableStructure += "echo '<option value='.$"+primaryKey+".'>'.$"+primaryKey+".'</option>';"
    content = content.replace('--SELECTVARIABLES--', selectVariableStructure)
    formStructure = "<form action='"+dynamicRelationshipName+"-action.php' method='post' name='form1' role='form'>"
    content = content.replace('--FORMSTRUCTURE--', formStructure)
    f.write(content)
    f.close()

def editActionGenerator(data, conceptClass, dynamicRelationshipName, targetVariable):
    filePath = './generated_files/www/'+conceptClass+'/'+dynamicRelationshipName+'-action.php'
    f = open(filePath,'w')
    formStructure = "<form action='"+dynamicRelationshipName+"-action.php' method='post' name='form1' role='form'>"
    content = baseAction.replace('--FORMSTRUCTURE--', formStructure)
    labelStructure = "<label>"+targetVariable.upper()+"</label>"
    content = content.replace('--LABELSTRUCTURE--', labelStructure)
    butronStructure = "<button type='submit' class='btn btn-default btn-md btn-block' name='update'>"+dynamicRelationshipName+"</button>"
    content = content.replace('--BUTTONSTRUCTURE-', butronStructure)
    inputStructure = "<input class='form-control' type='text' name='"+targetVariable+"'><input class='form-control' type='hidden' name='id' value='$id'>"
    content = content.replace('--INPUTSTRUCTURE--', inputStructure)
    variableStructure = "$"+targetVariable+"=$_POST['"+targetVariable+"'];"  
    content = content.replace('--VARIABLESTRUCTURE--', variableStructure)
    variableStructure = targetVariable+"='$"+targetVariable+"'"
    content = content.replace('--QUERY--', queryGenerator(data, 'update', conceptClass, [targetVariable],''))
    f.write(content)
    f.close()

def editGenerator(data, conceptClass, dynamicRelationshipName, targetVariable):
    editBaseGenerator(data, conceptClass, dynamicRelationshipName, targetVariable)
    editActionGenerator(data, conceptClass, dynamicRelationshipName, targetVariable)

