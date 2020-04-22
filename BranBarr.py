
def ingreso():
        carnes=[]
        nombres=[]
        secciones=[]
        cursos=[]
        notas=[]

        print("----------------------------------BIENVENIDO----------------------------------"
              "\nPRIMERO DEBE INGRESAR DATOS Y LUEGO BUSCAR UN DATO EN LAS LISTAS")
        cantidad=int(input("Cuantos alumnos ingresara: "))
        for x in range(cantidad):
                 carne=input("\nCarné del Alumno # "+str(x+1)+" : ")
                 carnes.append(carne)
                 nombre = input("Nombre y apellido: ")
                 nombres.append(nombre)
                 seccion = input("Sección: ")
                 secciones.append(seccion)
                 curso = input("Curso asignado: ")
                 cursos.append(curso)
                 nota = int(input("Ingrese nota Final del Alumno: "))
                 notas.append(nota)

        print(' {:<30} {:<22} {:<23} {:<33} {:<10} '.format("\n\nCODIGO", "NOMBRE", "SECCION", "CURSO_ASIGNADO", "NOTA:"))
        for x in range(cantidad):
                print(' {:<21} {:<30} {:<15} {:<40} {:<5} '.format(carnes[x], nombres[x], secciones[x], cursos[x], notas[x]))

        dato = input("\n\nEscriba el Carnet o Nombre de persona a buscar: ")
        if dato in carnes:
            print("El dato se encuentra en la lista Carnes. Posicion: ")
            print(carnes.index(dato))
        elif dato in nombres:
            print("El dato se encuentra en la lista Nombres. Posicion: ")
            print(nombres.index(dato))
        else:
            print("No esta en la lista.")


ingreso()