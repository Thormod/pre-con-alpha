from sqlGenerator.queryGenerator import queryGenerator
from phpGenerator.editGenerator import editBaseGenerator

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


if(isset($_POST['sel1'])){
    $id = $_POST['sel1'];
    
    $firsVariableId = '';
    $secondVariableId = '';
    $firstVariableValue = '';
    $secondVariableValue = '';

    $query1 = "--IDQUERY1--'$id'";
    $result = mysqli_query($conn, $query1);
    if ($result->num_rows > 0) {
        $res = mysqli_fetch_array($result);
        $firstVariableId = --FIRSTVARIABLE--;
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }
    
    $query2 = "--IDQUERY2--'$id'";
    $result = mysqli_query($conn, $query2);
    if ($result->num_rows > 0) {
        $res = mysqli_fetch_array($result);
        $secondVariableId = --SECONDVARIABLE--;
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }

    $query3 = "--VALUEQUERY1--'$firstVariableId'";
    $result = mysqli_query($conn, $query3);
    if ($result->num_rows > 0) {
        $res = mysqli_fetch_array($result);
        $firstVariableValue = --THIRDVARIABLE--;
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }

    $query4 = "--VALUEQUERY2--'$secondVariableId'";
    $result = mysqli_query($conn, $query4);
    if ($result->num_rows > 0) {
        $res = mysqli_fetch_array($result);
        $secondVariableValue = --FOURTHVARIABLE--;
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }

    --OPERATONSTRUCTURE--
}   
"""
# SELECT employee_id FROM wage WHERE wage_id = 1
#     SELECT selling FROM employee WHERE employee_id = 1
#     SELECT selling_goal FROM employee WHERE employee_id = 1

#     if(selling_goal <= selling){
#        wage = 1
#     }
def selfGenerator(data, targetClass, targetVariable, firstVariable, secondVariable, operation, dynamicRelationshipName):
    editBaseGenerator(data, targetClass, dynamicRelationshipName, targetVariable)
    selfActionGenerator(data, targetClass, targetVariable, firstVariable, secondVariable, operation, dynamicRelationshipName)

def selfActionGenerator(data, targetClass, targetVariable, firstVariable, secondVariable, operation, dynamicRelationshipName):
    firstVariableList  = str(firstVariable).split('.')
    firstConceptClass = firstVariableList[0]
    firstTargetVariable = firstVariableList[1]
    secondVariableList  = str(secondVariable).split('.')
    secondConceptClass = secondVariableList[0]
    secondTargetVariable = secondVariableList[1]
    filePath = './generated_files/www/'+targetClass+'/'+dynamicRelationshipName+'-action.php'
    f = open(filePath,'w')
    #firstId
    firstIdQuery = queryGenerator(data, 'select-variables-where', targetClass, [data['concept_class'][firstConceptClass]['constraints']['pk']], [data['concept_class'][targetClass]['constraints']['pk']])
    content = baseAction.replace('--IDQUERY1--', firstIdQuery)
    firstVariableIdStructure = '$res['+data['concept_class'][firstConceptClass]['constraints']['pk']+']'
    content = content.replace('--FIRSTVARIABLE--', firstVariableIdStructure )
    #secondId
    secondIdQuery = queryGenerator(data, 'select-variables-where', targetClass, [data['concept_class'][secondConceptClass]['constraints']['pk']], [data['concept_class'][targetClass]['constraints']['pk']])
    content = content.replace('--IDQUERY2--', secondIdQuery)
    secondVariableIdStructure = '$res['+data['concept_class'][secondConceptClass]['constraints']['pk']+']'
    content = content.replace('--SECONDVARIABLE--', secondVariableIdStructure )
    #firstVariableData
    firstVariableValueQuery = queryGenerator(data, 'select-variables-where', firstConceptClass, [firstTargetVariable], [data['concept_class'][firstConceptClass]['constraints']['pk']])
    content = content.replace('--VALUEQUERY1--', firstVariableValueQuery)
    firstVariableValueStructure = '$res['+firstTargetVariable+']'
    content = content.replace('--THIRDVARIABLE--', firstVariableValueStructure )
    #secondVariableData
    secondVariableValueQuery = queryGenerator(data, 'select-variables-where', secondConceptClass, [secondTargetVariable], [data['concept_class'][secondConceptClass]['constraints']['pk']])
    content = content.replace('--VALUEQUERY2--', secondVariableValueQuery)
    secondVariableValueStructure = '$res['+secondTargetVariable+']'
    content = content.replace('--FOURTHVARIABLE--', secondVariableValueStructure )
    operationContent = ''
    if(operation == '<' or operation == '>' or operation == '==' or operation == '!=' or operation == '>=' or operation == '<='):
        operationStructure = """
    if($firstVariableValue --OPERATION-- $secondVariableValue) {
        --VARIABLESTRUCTURE--=1.0;
    } else {
        --VARIABLESTRUCTURE--=0.0;
    }

    $query5 = "--QUERY--'$id'";
    if(mysqli_query($conn, $query5)){
        header("Location: ./index.php");
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }
    """
        operationQuery = queryGenerator(data, 'update', targetClass, [targetVariable], '')
        variableStructure = '$'+targetVariable
        operationContent = operationStructure.replace('--OPERATION--', operation)
        operationContent = operationContent.replace('--VARIABLESTRUCTURE--', variableStructure)
        operationContent = operationContent.replace('--QUERY--', operationQuery)
    else:
        operationStructure = """
    --VARIABLESTRUCTURE--=$firstVariableValue --OPERATION-- $secondVariableValue;
    $query5 = "--QUERY--'$id'";
    if(mysqli_query($conn, $query5)){
        header("Location: ./index.php");
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
    }
    """
        operationQuery = queryGenerator(data, 'update', targetClass, [targetVariable], '')
        variableStructure = '$'+targetVariable
        operationContent = operationStructure.replace('--OPERATION--', operation)
        operationContent = operationContent.replace('--VARIABLESTRUCTURE--', variableStructure)
        operationContent = operationContent.replace('--QUERY--', operationQuery)
        
    content = content.replace('--OPERATONSTRUCTURE--', operationContent)
    f.write(content)
    f.close()
    