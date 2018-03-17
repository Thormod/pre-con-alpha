# insert into estudiante (age, nombre, cedula, programa) values (23, 'sebastian', '123456', 'sistemas');
# insert into profesor (age, nombre, cedula, programa) values (23, 'sebastian', '123456', 'sistemas');
# insert into curso (estudiante_id, profesor_id, codigo, nombre) values (2,2,'C0010', 'fundamentos');

import json
from sqlGenerator.sqlGenerator import sqlParse
from sqlGenerator.queryGenerator import queryGenerator
from folderStructureGenerator import createFolder,generateBasicStructure, generateDynamicStructure
from commonFilesGenerator import copyCommonFiles
from phpGenerator.baseGenerator import generateBase
from phpGenerator.indexGenerator import indexGenerator
from phpGenerator.addGenerator import addGenerator

data = json.load(open('data.json'))
generateBasicStructure()
copyCommonFiles()
sqlParse(data)
generateDynamicStructure(data)
generateBase(data)
indexGenerator(data)
addGenerator(data)