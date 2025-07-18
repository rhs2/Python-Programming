#Python Object oriented programming
#class and instances
#instance method
#using special __init__ method to initilize as __init__ constructor
class employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@yahoo.com" 
    def display(self):
        print(f'Name: {self.first} {self.last}, Email: {self.email}, Pay: {self.pay}')
    def full_name(self):
        print(f"{self.first} {self.last}")

emp5 = employee('rhs', '2', 80000)
print(emp5)
print(emp5.email)
emp5.display()
emp5.full_name()
employee.full_name(emp5) #we can also the direct class to see the method


