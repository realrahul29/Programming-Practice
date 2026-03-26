class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Manager(Employee):
    def display(self):
        print(self.name, self.age, self.salary)

managers = []
for i in range(3):
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    managers.append(Manager(name, age, salary))

for m in managers:
    m.display()