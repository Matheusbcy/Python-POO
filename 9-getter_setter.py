class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Name: {self.name}\nSalary: {self.__salary}")

    # Metodo para buscar dados
    def get_salary8(self):
        return self.__salary

    # Método para modificar atributo privado
    def set_salary(self, salary):
        self.__salary = salary

fulano = Employee('Fulano', 1000)
sicrano = Employee('Sicrano', 2000)

fulano.show()

fulano.name = "Fulano2"

fulano.show()
sicrano.show()

fulano.set_salary(40000)
fulano.show()