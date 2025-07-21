#json file manupulations
#for file loading we use json.load
import json
with open ("states.json") as f:
    data = json.load(f)
for state in data['states']:
    print(state)
for state in data['states']:
    print(state['name'], state['abbreviation'])
for state in data['states']:
    del state['area_codes']
#now we have to write that file
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent = 2 )
with open('new_states.json','r') as f:
    data = json.load(f)
print(data)
