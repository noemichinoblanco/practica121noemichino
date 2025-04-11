class Aplicacion:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

class Celular:
    def __init__(self):
        self.apps = []
        self.espacio = 1024
        self.bateria = 100

    def instalar(self, app):
        if len(self.apps) >= 20 or app.tamano > self.espacio:

            print(f"No se puede instalar {app.nombre}.")
        else:
            self.apps.append(app)
            self.espacio -= app.tamano
            print(f"{app.nombre} instalada.")

    def usar(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado.")
            return

        encontrada = False
        for app in self.apps:
            if app.nombre == nombre:
                encontrada = True
                if app.tamano > 250:
                    consumo = 5

                elif app.tamano > 100:
                    consumo = 2
                else:
                    consumo = 1

                gasto = consumo * (minutos / 10)
                self.bateria -= gasto
                if self.bateria < 0:
                    self.bateria = 0

                estado = "apagado" if self.bateria == 0 else f"{self.bateria:.2f}% batería"
                print(f"Usando {nombre}... Estado: {estado}")
                break

        if not encontrada:
            print(f"{nombre} no está instalada.")

    def mostrar_bateria(self):
        print(f"Batería: {self.bateria:.2f}%")


cel = Celular()
cel.instalar(Aplicacion("telegram", 80))
cel.instalar(Aplicacion("Messenger", 150))
cel.instalar(Aplicacion("tic", 300))

cel.usar("telegram", 30)
cel.usar("Messenger", 20)
cel.usar("tic", 60)
cel.mostrar_bateria()
cel.usar("tic", 100)

