#adding total salaries for 2 employees
#accssing __repr__
#accessing __str__
##dunder __str__ method
#magic method or dunder for operator loading
## Class Variable
class employee():
    raise_amount = 1.04 #class variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@yahoo.com" 
    def display(self):
        print(f'Name: {self.first} {self.last}, Email: {self.email}, Pay: {self.pay}')
    def full_name(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        raise_pay = self.pay * self.raise_amount
        return raise_pay
    def __repr__(self):
        return f"Employee: {self.first}, {self.last}, {self.pay}"
    def __str__(self):
        return f"{self.full_name()}, {self.email}"
    def __add__(self,other): #combind salaries for 2 emps
        return self.pay+ other.pay
    def __len__(self): #printing out character of the emp full name
        return len(self.full_name())


emp5 = employee('rhs', '2', 80000)
emp6 = employee('sio', '4', 50000)
#no[w as we can see we are over write the __repr__ method by __str__ method]
# print(emp5) #now whenever we run the emp5 now we see the details about emp5 but before we would get vague as memory object print out
print(emp5+emp6)
print(len(emp5))
