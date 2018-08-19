import sys

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def my_name_is(self):
        return "My name is : " + self.first_name + " " + self.last_name;   


class Student(object):
    def __init__(self, first_name, last_name, roll_number = 100):
        print("roll_numberroll_numberroll_number",roll_number)
        self.first_name = first_name
        self.last_name  = last_name
        self.roll_number = roll_number
    
    def student_details(self):
        return "Student Name : "+self.first_name + " "+ self.last_name + " And my roll number" #+ self.roll_number


class Employee(Person,Student):
    empCount = 0
    def __init__(self, first_name, last_name, emp_salary):
        super().__init__(first_name, last_name)
        Student.__init__(self,first_name, last_name, emp_salary)
        Employee.empCount += 1
        self.first_name = first_name
        self.last_name = last_name
        self.emp_salary = emp_salary

    def emp_details(self):
        return self.student_details() + " And My Salary Is : "+ self.emp_salary


obj = Employee("Ravi", "Guru", "150000")
print(obj.emp_details());
print("Number of employee : ",Employee.empCount);