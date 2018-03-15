def generate_sql_file(structure):
    f = open('./generated_files/database/setup.sql','w')
    f.write(structure)
    f.close()

def dict_parse(data, structure):
    for i in data:
        if type(data[i]) is int:
            structure += i+' INTEGER NOT NULL, '
        elif type(data[i]) is float:
            structure += i+' DOUBLE NOT NULL, '
        elif type(data[i]) is str:
            structure += i+' VARCHAR(50) NOT NULL, '
    structure += 'PRIMARY KEY ('+ data['constraints']['pk'] +'), '
    for fk in data['constraints']['fk']:
        if(fk['id'] != ''):
            structure += 'FOREIGN KEY (' + fk['id'] + ') REFERENCES ' + fk['references'] + '(' + fk['id'] + '), '
    structure = structure[:-2]
    structure += ');'
    return structure

def sqlParse(data):
    structure = 'CREATE TABLE'
    sql = ''
    for i in data:
        structure += ' '+i+' ('
        structure = dict_parse(data[i], structure)
        sql += structure + '\n'
        structure = 'CREATE TABLE'
    generate_sql_file(sql)