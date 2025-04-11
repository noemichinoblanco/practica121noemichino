class Oficina:
    def __init__(self, sillas, escritorios, estanterias):
        self.sillas = sillas
        self.escritorios = escritorios
        self.estanterias = estanterias

    def mostrar(self):
        print(f"Oficina - Sillas: {self.sillas}, Escritorios: {self.escritorios}, Estanterías: {self.estanterias}")

    def cantidad_muebles(self):
        return self.sillas + self.escritorios + self.estanterias


class Aula:
    def __init__(self, nombre, capacidad, nro_pupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_pupitres = nro_pupitres

    def mostrar(self):
        print(f"Aula {self.nombre} - Capacidad: {self.capacidad}, Pupitres: {self.nro_pupitres}")

    def cantidad_muebles(self):
        return self.nro_pupitres


class Laboratorio:
    def __init__(self, nombre, capacidad, nro_mesas, nro_sillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_mesas = nro_mesas
        self.nro_sillas = nro_sillas

    def mostrar(self):
        print(f"Laboratorio {self.nombre} - Capacidad: {self.capacidad}, Mesas: {self.nro_mesas}, Sillas: {self.nro_sillas}")

    def cantidad_muebles(self):
        return self.nro_mesas + self.nro_sillas


oficina1 = Oficina(4, 2, 1)
oficina2 = Oficina(6, 3, 2)
aula1 = Aula("A1", 30, 30)
aula2 = Aula("A2", 25, 25)
lab1 = Laboratorio("LabFisica", 20, 10, 20)

ambientes = [oficina1, oficina2, aula1, aula2, lab1]

print("Datos de los ambientes:")
for amb in ambientes:
    amb.mostrar()
    print("Total muebles:", amb.cantidad_muebles())
