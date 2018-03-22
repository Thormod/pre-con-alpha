
from phpGenerator.addGenerator import addGenerator
from phpGenerator.editGenerator import editGenerator

def dynamicRelationshipGenerator(data):
    for i in data['dynamic_relationship']:
        for j in data['dynamic_relationship'][i]:
            conceptClass = data['dynamic_relationship'][i][j]['class']
            relationshipType = data['dynamic_relationship'][i][j]['type']
            if(relationshipType == 'add'):
                addGenerator(data, conceptClass, j)
            elif(relationshipType == 'edit'):
                relationship = str(conceptClass).split('.')
                targetClass = relationship[0]
                targetVariable = relationship[1]
                editGenerator(data, targetClass, j, targetVariable )

                