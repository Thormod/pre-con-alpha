def selectQuery(data):
    queryList = []
    queryStructure = 'SELECT * From '
    for i in data:
        queryList.append(queryStructure+i)
    return queryList

def queryGenerator(data, queryType):
    if queryType == 'select':
        return selectQuery(data)
