class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def moverse(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre)
        self.edad = edad
        self.raza = raza

    def hacer_sonido(self):
        print("Guau guau")

    def moverse(self):
        print("El perro corre.")

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacer_sonido(self):
        print("Miau miau")

    def moverse(self):
        print("El gato salta.")

class Pajaro(Animal):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def hacer_sonido(self):
        print("Pío pío")

    def moverse(self):
        print("El pájaro vuela.")


perro = Perro("Firulais", 3, "kuquer")
gato = Gato("rufu", "Negro")
pajaro = Pajaro("hachiko", "Canario")

perro.hacer_sonido()
perro.moverse()

gato.hacer_sonido()
gato.moverse()

pajaro.hacer_sonido()
pajaro.moverse()
