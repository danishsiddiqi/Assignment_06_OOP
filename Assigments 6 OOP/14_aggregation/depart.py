class Employee:
    def __init__(self, name):
        self.name = name
        
class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Mustufa")

dept = Department(emp)
print(dept.employee.name)
