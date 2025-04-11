class Computadora:
    def __init__(self):
        self.componentes = ["CPU", "RAM", "Disco Duro", "Placa Madre", 
                            "Fuente de Poder", "Monitor", "Teclado", "Mouse","memoria"]
        self.encendida = False

    def mostrar_componentes(self):
        print("Componentes de la computadora:")
        for comp in self.componentes:
            print(f" - {comp}")

    def mostrar_estado(self):
        estado = "Encendida" if self.encendida else "Apagada"
        print(f"Estado actual: {estado}")
        print("noemi chino blanco")

    def encender(self):
        if not self.encendida:
            self.encendida = True

            print("La computadora se a encendido.")
        else:
            print("La computadora ya esta encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("La computadora se a apagado.")
        else:
            print("La computadora ya esta apagada.")

pc = Computadora()
pc.mostrar_componentes()
pc.mostrar_estado()
pc.encender()
pc.mostrar_estado()
pc.apagar()
pc.mostrar_estado()
