#creating a manage that handles employees 
#creating another subclass manager and make that manager to handle employees
#customise the sub class like in out employee class it takes parameter of first, last and pay and now we would like to make the parameter as prog_lang too
#developer subclass
#python class inheritance
#applying raise on developer instance
class employee():
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@yahoo.com" 
    def display(self):
        print(f'Name: {self.first} {self.last}, Email: {self.email}, Pay: {self.pay}')
    def full_name(self):
        return f"{self.first} {self.last}"
        #print(f"{self.first} {self.last})
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
class developer(employee):
    raise_amount = 1.10 #10%
    #now we can see we can inherit everything from the employee class and get access of employee from developer subclass
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # employee.__init__(self,first,last,pay)
        #we can use both of the method but for me super method is more convinience and easy to use
        #we use super method because we do not want to use the same code again and again do make out code DRY we reuse the code from employee class
        self.prog_lang = prog_lang

class Manager(employee): #another subclass of manager 
    # pass #skipping the class for a time being
#now we can take all the data from the employee class as we inheritance that manager class from employee class
    def __init__(self,first,last,pay,emps=None):
        super().__init__(first,last,pay)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps
    def add_emps(self,emp): #adding emps whom manager supervise
        if emp not in self.emps:
            self.emps.append(emp)
    def remove_emps(self,emp):
        if emp in self.emps:
            self.emps.remove(emp)
    def print_emps(self):
        for emp in self.emps:
            print('----->', emp.full_name())



    
dev1 = developer('rhs', '2', 80000,'python') 
dev2 = developer('sio','3', 95000,'java')
emp1 = employee('rhs2','4',80000)
mgr1 = Manager('john', 'doe', 90000, [dev1])
mgr2 = Manager('joe','smith', 75000, [] )
#adding supervision people
mgr1.add_emps(emp1)
mgr1.add_emps(mgr2)
#removing emps from supervision
mgr1.remove_emps(dev1)

mgr1.print_emps()
#isinstance() if a object is instance of a class
print(isinstance(mgr1, Manager))
#it is printing out if a instance is from a class or not in boolean version
print(isinstance(dev1, employee))

## issubclass- it will print out a class is a subclass of another class it means is it inheriting from that class in true or false
print(issubclass(Manager, employee))
print(issubclass(Manager, developer))

#chec k out HTTP Exception built in function is for more refference for practical and real worlds, EXCEPTION MODULE

