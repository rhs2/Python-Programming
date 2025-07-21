'''JavaScript Object Notation'''
#importing json
import json
#this is a python string that happend to be a valid json
#in the json file we always needs to put double qoute 
people_string = '''
{ 
    "people": [
    {   "name" : "John Smith",
        "phone" : "614-555-7164",
        "emails" : ["rhs0@yahoo.com", "rhs2@yahoo.com"],
        "has-licence" : false
    },
    {   "name": "john doe",
        "phone" : "560-444-3746",
        "emails" : null,
        "has-licence" : true

    }
    ]
}
'''
#loading strings in python 
data = json.loads(people_string)
print(data) #data is not clean readable 

print(type(data)) #we can see that the json strings converted to dict
#this is a pytho dict
#if we load a json object into python it will convert to as 
#JSON            #PYHTON
#object -------> dict
#array ---------> list
#string --------> str
#number(int) ----> int
#number(float) ---> float
#true -----------> True
#false ---------> False
#null ----------> None
#inside that dict as we can see there is a list so can loop through that dict with the key of people
for person in data['people']:
    print(person)
#since each of these people in our original json string are object themselves then we can convert those as dict also we can also access those within a loop
for person in data['people']:
    print(person['name'])
#we can dump a python object as json string
#remove the phone number and dump that to json string
for person in data['people']:
    del person['phone']
new_string = json.dumps(data, indent = 2, sort_keys = True)
print(new_string)
#here we can see phone key is deleted