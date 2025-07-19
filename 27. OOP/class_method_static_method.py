#creating a static method if a day is week day or not from the employee class we have used so far
#pass a string and create a employee from that
#running class method with the instance
import datetime
class employee():
    num_of_emps =0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@yahoo.com" 
        employee.num_of_emps +=1
    def display(self):
        print(f'Name: {self.first} {self.last}, Email: {self.email}, Pay: {self.pay}')
    def full_name(self):
        print(f"{self.first} {self.last}")
    def apply_raise(self):
        raise_pay = self.pay * self.raise_amount
        return raise_pay
    @classmethod
    def set_raise_amount(cls, amount): #in class method cls is the auto taking class variable
        # pass #initially skipping the cls method
        cls.raise_amount = amount
    #lets use class method to create the emp from that class

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    #static method does not take any parameter it is independent as hell
    #we can access static method from the class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

emp5 = employee('rhs', '2', 80000)
emp6 = employee('sio', '4', 50000)
emp5.set_raise_amount(1.09)

emp_str_1= 'John-Doe-70000'
emp_str_2= 'Steve-Smith-80000'
emp_str_3 = 'Jane-Doe-90000'
emp8= employee.from_string(emp_str_1)
emp9= employee.from_string(emp_str_2)
my_date = datetime.date(2016,7,16)
employee.is_workday(my_date)
print(emp6.__dict__)
print(employee.__dict__)
