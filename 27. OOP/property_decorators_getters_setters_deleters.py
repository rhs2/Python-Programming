## Class Variable
#property decorators
#changing the full name
#using setter and that will change our full name 
class employee():
    raise_amount = 1.04 #class variable
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def display(self):
        print(f'Name: {self.first} {self.last}, Email: {self.email}, Pay: {self.pay}')
    @property
    def email(self):
        return self.first + '.' + self.last + "@yahoo.com"  
    #now we can see it solves out problems
    @property #removing the () from the function and it works like a attribute
    def full_name(self):
        return f"{self.first} {self.last}"
    @full_name.setter #getting the new name for setters methods
    def full_name(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @full_name.deleter #it will delete the name 
    def full_name(self):
        print('Deleted the name!')
        self.first = None
        self.last = None



emp1 = employee('john','doe')
emp1.full_name = 'Jusi smith' #adding a new name 
print(emp1.first)
print(emp1.email) #instead of calling () funtion we can remove that function by just adding the @property 
print(emp1.full_name) #calling the funtions without the parenthesis, it is a method but we accessing it like a attribute
del  emp1.full_name #completely delete the name and returns None