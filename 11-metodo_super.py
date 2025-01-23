class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"{self._brand} - {self._model_name}"

    @staticmethod
    def make_a_call(phone_num):
        print(f"dialing {phone_num}...")


class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)

        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera


Moto = Phone("Moto", "G7", 1000)
print(Moto)
Moto.make_a_call(1234567890)
print(f"Valor do {Moto._brand}{Moto._model_name}: R${Moto._price}")
print(vars(Moto))

Iphone = Smartphone("Iphone", "13", 5000, "4GB", "128GB", "25MP")
print(Iphone)
Iphone.make_a_call(1234567890)
print(f"Valor do {Iphone._brand}{Iphone._model_name}: R${Iphone._price}")