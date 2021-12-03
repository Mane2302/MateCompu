package maiz0;

import java.util.Scanner;

/**
 *
 * @author MANE2302
 */
public class maiz {
    Scanner datos = new Scanner(System.in);
		String nombre = "";
		int maiz = 0;
		float tierra = 0;
		int termina = 1;
		float total = 0;
                float bulto = 0;
    
    public static void main(String[] args) {
		maiz maiz1 = new maiz();

		System.out.println("-----------------------------");
		System.out.println("---------MaizContador--------");
		System.out.println("-----------------------------");
                System.out.println("Para el cálculo de los bultos de maíz a usar, se tomará la referencia");
                System.out.println("uno de 20 kg, (18000 maíces)");

                Scanner datos = new Scanner(System.in);
		System.out.println("¿Cual es su nombre?");
		maiz1.nombre = datos.nextLine();

		while (maiz1.termina ==1){

			System.out.println("¿Usaras 2 o 3 maices por hoyo de tierra?");
			maiz1.maiz = datos.nextInt();

			System.out.println("Introduce el total de hectareas a sembrar");
			maiz1.tierra = datos.nextFloat();

			if (maiz1.maiz == 2){
				maiz1.total = (maiz1.tierra*1000)*14;
                                maiz1.bulto = maiz1.total/18000;
                                
				System.out.println(maiz1.nombre + " el total de maices a sembrar por " + maiz1.tierra + " hectareas es: " + maiz1.total + " maices");
                                System.out.println("La cantidad de bultos a usar será de: " + maiz1.bulto);
				
			}
			else if (maiz1.maiz==3) {
				maiz1.total = (maiz1.tierra*1000)*12;
                                maiz1.bulto = maiz1.total/18000;
                                
				System.out.println(maiz1.nombre + " el total de maices a sembrar por " + maiz1.tierra + " hectareas es: " + maiz1.total + " maices");
				System.out.println("La cantidad de bultos a usar será de: " + maiz1.bulto);
			}
			else
				System.out.println("-opcion no valida-");

		System.out.println("¿Desea usar nuevamente el programa?");
		System.out.println("Ingrese (1) si desea continuar");
		System.out.println("Ingrese (2) si desea salir");
		maiz1.termina = datos.nextInt();	

		}
	System.out.println("Gracias por usar el programa :) ");	

	}
}
