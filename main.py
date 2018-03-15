import json
from sqlGenerator.sqlGenerator import sqlParse
from sqlGenerator.queryGenerator import queryGenerator
from folderStructureGenerator import createFolder,generateBasicStructure, generateDynamicStructure
from commonFilesGenerator import copyCommonFiles
from phpGenerator.indexGenerator import indexGenerator

data = json.load(open('data.json'))

generateBasicStructure()
copyCommonFiles()
sqlParse(data)
generateDynamicStructure(data)
indexGenerator(data)