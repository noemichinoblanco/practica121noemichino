/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package introduccionpoo.polimorfismo;

class Oficina {
    int sillas, escritorios, estanterias;

    public Oficina(int sillas, int escritorios, int estanterias) {
        this.sillas = sillas;
        this.escritorios = escritorios;
        this.estanterias = estanterias;
    }

    public void mostrar() {
        System.out.println("Oficina - Sillas: " + sillas + ", Escritorios: " + escritorios + ", Estanterías: " + estanterias);
    }

    public int cantidadMuebles() {
        return sillas + escritorios + estanterias;
    }
}

class Aula {
    String nombre;
    int capacidad, nroPupitres;

    public Aula(String nombre, int capacidad, int nroPupitres) {
        this.nombre = nombre;
        this.capacidad = capacidad;
        this.nroPupitres = nroPupitres;
    }

    public void mostrar() {
        System.out.println("Aula " + nombre + " - Capacidad: " + capacidad + ", Pupitres: " + nroPupitres);
    }

    public int cantidadMuebles() {
        return nroPupitres;
    }
}

class Laboratorio {
    String nombre;
    int capacidad, nroMesas, nroSillas;

    public Laboratorio(String nombre, int capacidad, int nroMesas, int nroSillas) {
        this.nombre = nombre;
        this.capacidad = capacidad;
        this.nroMesas = nroMesas;
        this.nroSillas = nroSillas;
    }

    public void mostrar() {
        System.out.println("Laboratorio " + nombre + " - Capacidad: " + capacidad + ", Mesas: " + nroMesas + ", Sillas: " + nroSillas);
    }

    public int cantidadMuebles() {
        return nroMesas + nroSillas;
    }
}

public class Ambientes {
    public static void main(String[] args) {
        Oficina oficina1 = new Oficina(4, 2, 1);
        Oficina oficina2 = new Oficina(6, 3, 2);
        Aula aula1 = new Aula("A1", 30, 30);
        Aula aula2 = new Aula("A2", 25, 25);
        Laboratorio lab1 = new Laboratorio("LabFisica", 20, 10, 20);

        Object[] ambientes = { oficina1, oficina2, aula1, aula2, lab1 };

        System.out.println("Datos de los ambientes:");
        System.out.println("noemi chino blanco");
        for (Object amb : ambientes) {
            if (amb instanceof Oficina) {
                Oficina o = (Oficina) amb;
                o.mostrar();
                System.out.println("Total muebles: " + o.cantidadMuebles());
            } else if (amb instanceof Aula) {
                Aula a = (Aula) amb;
                a.mostrar();
                System.out.println("Total muebles: " + a.cantidadMuebles());
            } else if (amb instanceof Laboratorio) {
                Laboratorio l = (Laboratorio) amb;
                l.mostrar();
                System.out.println("Total muebles: " + l.cantidadMuebles());
            }
        }
    }
}
