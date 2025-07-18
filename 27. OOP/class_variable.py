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
        print(f"{self.first} {self.last}")
    def apply_raise(self):
        raise_pay = self.pay * self.raise_amount
        return raise_pay

emp5 = employee('rhs', '2', 80000)
emp6 = employee('sio', '4', 50000)
emp6.raise_amount= 1.08
print(emp5.pay)
print(emp5.apply_raise())
print(emp6.apply_raise())
print(emp5.__dict__) #it does not have the raise amount but it gathers it from the employee class
print(employee.__dict__) #employee class has the raise amount because it is a class variable
print(emp5.raise_amount) #still here we can see emp5 gathers the raise amount from class variable
print(emp6.raise_amount) #but emp6 has its own class variable so it gathers from it