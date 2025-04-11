
package introduccionpoo;

public class Persona {
    private String nombre;
    private int edad;
    private String ciudad;

    
    public Persona(String nombre, int edad, String ciudad) {
        this.nombre = nombre;
        this.edad = edad;
        this.ciudad = ciudad;
    }

    public void saludar() {
        System.out.println("Hola, soy " + nombre + " de " + ciudad);
    }

    public boolean esMayorDeEdad() {
        return edad >= 18;
    }

    
    public static void main(String[] args) {
      
        Persona persona1 = new Persona("Noemí", 20, "  rio seco");
        Persona persona2 = new Persona("Chino", 17, "peru");
        Persona persona3 = new Persona("Anahi", 25, "muñecas");

       
        persona1.saludar();
        persona2.saludar();
        persona3.saludar();

        System.out.println(persona1.nombre + " es mayor de edad: " + persona1.esMayorDeEdad());
        System.out.println(persona2.nombre + " es mayor de edad: " + persona2.esMayorDeEdad());
        System.out.println(persona3.nombre + " es mayor de edad: " + persona3.esMayorDeEdad());
        System.out.println("noemi chino blanco");
    }
}
