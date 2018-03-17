def insertQuery(data):
    queryList = []
    queryStructure = 'INSERT INTO --NAME-- (--VARIABLES--) VALUES(--PHPVARIABLES--)'
    for i in data:
        primaryKey = data[i]['constraints']['pk']
        content = queryStructure.replace('--NAME--', i)
        variablesStructure = ''
        phpVariablesStructure = ''
        for j in data[i]:
            if j != 'constraints' and j != primaryKey:
                variablesStructure += j + ','
                phpVariablesStructure += "'$"+j+"',"
        content = content.replace('--VARIABLES--', variablesStructure[:-1])
        content = content.replace('--PHPVARIABLES--', phpVariablesStructure[:-1])
        queryList.append(content)
    return queryList

def selectQuery(data):
    queryList = []
    queryStructure = 'SELECT * From '
    for i in data:
        queryList.append(queryStructure+i)
    return queryList

def queryGenerator(data, queryType):
    if queryType == 'select':
        return selectQuery(data)
    if queryType == 'insert':
        return insertQuery(data)
