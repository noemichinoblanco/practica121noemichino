class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2

    def aprobo(self):
        return self.calcular_promedio() >= 6

    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        estado = "aprobó" if self.aprobo() else "no aprobó"
        print(f"{self.nombre} tiene un promedio de {promedio:.2f} y {estado}.")


e1 = Estudiante("Noemi", 8.9, 8.0)
e2 = Estudiante("jose", 5.0, 6.0)
e3 = Estudiante("ferr", 8.6, 5.5)

e1.mostrar_resultado()
e2.mostrar_resultado()
e3.mostrar_resultado()
