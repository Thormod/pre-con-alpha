import json
from sqlGenerator.sqlGenerator import sqlParse
from sqlGenerator.queryGenerator import queryGenerator
from folderStructureGenerator import createFolder,generateBasicStructure, generateDynamicStructure
from commonFilesGenerator import copyCommonFiles
from phpGenerator.baseGenerator import generateBase
from phpGenerator.dynamicRelationshipGenerator import dynamicRelationshipGenerator
from phpGenerator.indexGenerator import indexGenerator
from phpGenerator.addGenerator import addGenerator
from phpGenerator.editGenerator import editGenerator

data = json.load(open('data.json'))
concept_classes = data['concept_class']
dynamic_relationships = data['dynamic_relationship']
generateBasicStructure()
copyCommonFiles()
sqlParse(concept_classes)
generateDynamicStructure(concept_classes)
generateBase(data)
indexGenerator(concept_classes)
dynamicRelationshipGenerator(data)