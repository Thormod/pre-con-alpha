def insertQuery(data, conceptClass):
    queryStructure = 'INSERT INTO --NAME-- (--VARIABLES--) VALUES(--PHPVARIABLES--)'
    primaryKey = data['concept_class'][conceptClass]['constraints']['pk']
    content = queryStructure.replace('--NAME--', conceptClass)
    variablesStructure = ''
    phpVariablesStructure = ''
    targetClass = data['concept_class'][conceptClass]
    for j in targetClass:
        if j != 'constraints' and j != primaryKey:
            variablesStructure += j + ','
            phpVariablesStructure += "'$"+j+"',"
    content = content.replace('--VARIABLES--', variablesStructure[:-1])
    content = content.replace('--PHPVARIABLES--', phpVariablesStructure[:-1])
    return content

def selectAllQuery(data):
    queryList = []
    queryStructure = 'SELECT * From '
    for i in data:
        queryList.append(queryStructure+i)
    return queryList

def selectVariablesQuery(data, conceptClass, variables):
    queryStructure = 'SELECT --VARIABLES-- FROM --NAME--'  
    # SELECT employee_id, name FROM employee 
    variablesStructure = ''
    for i in variables:
        variablesStructure += i+', '
    content = queryStructure.replace('--VARIABLES--', variablesStructure[:-2])
    content = content.replace('--NAME--', conceptClass)
    return content

def selectVariablesWhereQuery(data, conceptClass, variables, condition):
    queryStructure = 'SELECT --VARIABLES-- FROM --NAME-- WHERE --CONDITIONS--='  
    # SELECT employee_id, name FROM employee 
    variablesStructure = ''
    conditionStructure = ''
    for i in variables:
        variablesStructure += i+', '
    for i in condition:
        conditionStructure += i
    content = queryStructure.replace('--VARIABLES--', variablesStructure[:-2])
    content = content.replace('--CONDITIONS--', conditionStructure)
    content = content.replace('--NAME--', conceptClass)
    return content

def selectWhereQuery(data, conceptClass, variables):
    queryStructure = 'SELECT * FROM --NAME-- WHERE --CONDITION--'  
    # SELECT employee_id, name FROM employee 
    conditionStructure = ''
    for i in variables:
        conditionStructure += i+', '
    return content

def updateQuery(data, conceptClass, variables):
    queryStructure = 'UPDATE '+conceptClass+' SET --VARIABLESTRUCTURE-- WHERE '+data['concept_class'][conceptClass]['constraints']['pk']+'='
    variableStructure = ''
    for i in variables:
        variableStructure += i+"='$"+i+"', "
    variableStructure = variableStructure[:-2]
    queryStructure = queryStructure.replace('--VARIABLESTRUCTURE--', variableStructure)
    return queryStructure

def queryGenerator(data, queryType, conceptClass, variables, condition):
    if queryType == 'select-all':
        return selectAllQuery(data)
    elif queryType == 'select-where':
        return selectWhereQuery(data, conceptClass, variables)
    elif queryType == 'select-variables':
        return selectVariablesQuery(data, conceptClass, variables)
    elif queryType == 'select-variables-where':
        return selectVariablesWhereQuery(data, conceptClass, variables, condition)
    elif queryType == 'insert':
        return insertQuery(data, conceptClass)
    elif queryType == 'update':
        return updateQuery(data, conceptClass, variables)
