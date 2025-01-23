class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f'Name: {self.name}\nSalary: {self.__salary}')
        
fulano = Employee('Fulano', 1000)
sicrano = Employee('Sicrano', 2000)
fulano.show()
sicrano.show()
fulano.__salary = 40000
fulano.show()