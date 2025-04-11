class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def mostrar_mayor_de_edad(self):
        if self.es_mayor_de_edad():
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} NO es mayor de edad.")


p1 = Persona("Noemi Chino blanco", 20, "La Paz")
p2 = Persona("Jose", 19, "Tarija")
p3 = Persona("Alejandro", 22, "Pando")

p1.saludar()
p1.mostrar_mayor_de_edad()
print()

p2.saludar()
p2.mostrar_mayor_de_edad()
print()

p3.saludar()
p3.mostrar_mayor_de_edad()
