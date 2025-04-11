class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo

    def accion(self):
        print(f"El cofre de tipo {self.tipo} se abre para guardar objetos mágicos.")

    def colocar(self, lugar, orientacion="suelo"):
        print(f"Colocando el cofre en {lugar}, orientado en el {orientacion}.")

    def romper(self):
        if self.tipo == "madera":
            print("El cofre de madera se astilla y suelta monedas.")
        elif self.tipo == "hierro":
            print("El cofre de hierro se rompe lentamente y suelta gemas.")
        else:
            print("El cofre se rompe y deja caer sus objetos.")

class BloqueTnt:
    def __init__(self, tipo, daño):
        self.tipo = tipo
        self.daño = daño

    def accion(self):
        print(f"La TNT de tipo {self.tipo} se activa... ¡prepárate para una gran explosión!")

    def colocar(self, lugar, orientacion="suelo"):
        print(f"Colocando TNT en {lugar}, orientada en el {orientacion}.")

    def romper(self):
        if self.tipo == "explosiva":
            print("¡Explosión media! La TNT explosiva arrasa con todo.")
        elif self.tipo == "mega":
            print("¡Explosión masiva! Nada sobrevive a la TNT mega.")
        else:
            print("¡BOOM! La TNT explota al romperse.")

class BloqueHorno:
    def __init__(self, color, capacidad_comida):
        self.color = color
        self.capacidad_comida = capacidad_comida

    def accion(self):
        print(f"El horno de color {self.color} comienza a cocinar {self.capacidad_comida} alimentos.")

    def colocar(self, lugar, orientacion="suelo"):
        print(f"Colocando horno en {lugar}, orientado en el {orientacion}.")

    def romper(self):
        if self.capacidad_comida > 4:
            print("El horno gigante se rompe y quema todo a su alrededor.")
        else:
            print("El horno pequeño se rompe y solo deja un poco de humo.")

# Inciso a) 

cofre1 = BloqueCofre(capacidad=10, resistencia=5, tipo="madera")
cofre2 = BloqueCofre(capacidad=20, resistencia=8, tipo="hierro")

tnt1 = BloqueTnt(tipo="explosiva", daño=50)
tnt2 = BloqueTnt(tipo="mega", daño=100)

horno1 = BloqueHorno(color="gris", capacidad_comida=3)
horno2 = BloqueHorno(color="negro", capacidad_comida=6)


print("=== Cofres ===")
cofre1.accion()
cofre1.colocar("cueva", "pared")
cofre1.romper()

cofre2.accion()
cofre2.colocar("castillo", "suelo")
cofre2.romper()

print("\n=== TNTs ===")
tnt1.accion()
tnt1.colocar("mina", "pared")
tnt1.romper()

tnt2.accion()
tnt2.colocar("campo", "suelo")
tnt2.romper()

print("\n=== Hornos ===")
horno1.accion()
horno1.colocar("casa", "suelo")
horno1.romper()

horno2.accion()
horno2.colocar("refugio", "pared")
horno2.romper()
