
############################
##  CORRRER DIRECTAMENTE ###
###########################



def idioma():
    print("="*30)
    print("Selecciona el idioma / Select the language")
    print("="*30)
    

    while True:
        print("""
        =====================
        1) ESPAÑOL / SPANISH
        2) INGLES / ENGLISH
        =====================
        """)
        while True:
            try:
                opciones_options = int(input("\nSelecciona la opción ( Select the option | 0 para salir / exit ): "))
                break
            except ValueError:
                print("ERROR. SOLO NÚMEROS. / ERROR. ONLY NUMBERS.")
        if opciones_options == 1:
            ejecutar()
        elif opciones_options == 2:
            run()
        elif opciones_options == 0:
            print("[-] SALIENDO... MUCHAS GRACIAS!!! | LEAVING... THANK YOU VERY MUCH!!! ")
            break



def ejecutar():
    print("="*30)
    print("GESTION DE ALUMNOS")
    print("="*30)

    while True:
        menu()
        while True:
            try:
                print("=>"*30)
                opcion = int(input("Elija una opción('9' Para salir): "))
                print("<="*30)
                break
            except ValueError:
                print("[-] Ingresa solo números...")
        if opcion == 1:
            crear(lista_usuarios)
        elif opcion == 2:
            modificar(lista_usuarios)
        elif opcion == 3:
            elimiar(lista_usuarios)
        elif opcion == 4:
            iteracion(lista_usuarios)
        elif opcion == 5:
            buscar(lista_usuarios)
        elif opcion == 6:
            menu()
        elif opcion == 7:
            iteracion(lista_usuarios)
            id(lista_usuarios)
        elif opcion == 8:
            filt_nac(lista_usuarios)
        elif opcion == 9:
            print("[-] CERRNADO EL PROGRAMA ...")
            break
            




## LISTA
lista_usuarios = [
    {"id": 1, "nombre": "ana", "apellido": "garcía", "año_nacimiento": 1995, "edad": 31},
    {"id": 2, "nombre": "luis", "apellido": "rodríguez", "año_nacimiento": 1988, "edad": 37},
    {"id": 3, "nombre": "maría", "apellido": "lópez", "año_nacimiento": 2001, "edad": 25},
    {"id": 4, "nombre": "carlos", "apellido": "martínez", "año_nacimiento": 1993, "edad": 33},
    {"id": 5, "nombre": "elena", "apellido": "gómez", "año_nacimiento": 1997, "edad": 29},
    {"id": 6, "nombre": "juan", "apellido": "sánchez", "año_nacimiento": 1990, "edad": 36},
    {"id": 7, "nombre": "sofía", "apellido": "pérez", "año_nacimiento": 2003, "edad": 23},
    {"id": 8, "nombre": "diego", "apellido": "gonzález", "año_nacimiento": 1985, "edad": 40},
    {"id": 9, "nombre": "lucía", "apellido": "fernández", "año_nacimiento": 1999, "edad": 27},
    {"id": 10, "nombre": "javier", "apellido": "ruiz", "año_nacimiento": 1992, "edad": 33},
    {"id": 11, "nombre": "marta", "apellido": "díaz", "año_nacimiento": 1996, "edad": 29},
    {"id": 12, "nombre": "alejandro", "apellido": "alvarez", "año_nacimiento": 1987, "edad": 39},
    {"id": 13, "nombre": "laura", "apellido": "moreno", "año_nacimiento": 1994, "edad": 32},
    {"id": 14, "nombre": "manuel", "apellido": "muñoz", "año_nacimiento": 1989, "edad": 37},
    {"id": 15, "nombre": "paula", "apellido": "jiménez", "año_nacimiento": 2002, "edad": 24},
    {"id": 16, "nombre": "mateo", "apellido": "hernández", "año_nacimiento": 1991, "edad": 35},
    {"id": 17, "nombre": "sara", "apellido": "romero", "año_nacimiento": 1998, "edad": 27},
    {"id": 18, "nombre": "david", "apellido": "alonso", "año_nacimiento": 1984, "edad": 42},
    {"id": 19, "nombre": "daniela", "apellido": "gutiérrez", "año_nacimiento": 2000, "edad": 25},
    {"id": 20, "nombre": "jorge", "apellido": "navarro", "año_nacimiento": 1993, "edad": 33}
]

def iteracion(listas):
        alumnos = lambda lista: [print(f"Id: {p['id']} | Nombre: {p['nombre'].capitalize()} | Apellido: {p['apellido'].capitalize()} | Nacimiento: {p['año_nacimiento']} | Edad: {p['edad']}") for p in lista]
        print("="*30)
        alumnos(listas)
        print("="*30)



def crear(liss):
        contador = 20
        while True:
            print("=>"*30)
            nom = input("Ingresa nombre : ").strip().lower()
            print("<="*30)
            if nom == "":
                print("[-]ERROR. ¡CAMPO OBLIGATORIO!")
                continue
            else:
                break
        while True:
            print("=>"*30)
            apell = input("Ingresa apellido: ").strip().lower()
            print("<="*30)
            
            if apell == "":
                print("[-]ERROR. ¡CAMPO OBLIGATORIO!")
                continue
            else:
                break
        #AÑO NACIMEINTO
        while True:
                try:
                    print("=>"*30)
                    nacimiento = int(input("Ingresa año de nacimiento: "))
                    print("<="*30)
                    if nacimiento == "":
                        print("[-]ERROR. ¡CAMPO OBLIGATORIO!")
                    else:
                        break
                except ValueError:
                    print("[-] ERROR. SOLO NÚMEROS ENTEROS")
            
        #EDAD
        while True:
            try:
                print("=>"*30)
                edad = int(input("Ingresa tu edad: "))
                print("<="*30)
                break
            except ValueError:
                print("[-] ERROR. SOLO NÚMEROS ENTEROS")
        if nom in lista_usuarios and apell in lista_usuarios:
            print("[-] El alumno ya existe en la lista")
        else:
            contador += 1    
            liss.append({"id":contador,"nombre":nom.strip(),"apellido":apell.strip(),"año_nacimiento":nacimiento,"edad":edad})
            




def modificar(lista):
        iteracion(lista_usuarios)
        while True:
            try:
                print("=>"*30)
                num = int(input("Selecciona el id del alumno a modificar: "))
                print("<="*30)
                break
            except ValueError:
                print("[-] ERROR. SOLO NÚMEROS ENTEROS")
                print("="*30)
        print("""
            1) FECHA DE NACIMIENTO
            2) NOMBRE
            3) APELLIDO
            4) SALIR
            """)
        while True:
            while True:
                try:
                    print("=>"*30)
                    modificar = int(input("¿Qué quieres modificar? ( 1,2,3,4 ) : "))
                    print("<="*30)
                    break
                except ValueError:
                    print("[-] ERROR. SOLO NÚMEROS")
                    print("="*30)
            
            if modificar == 1:
                for i in lista:
                        if i['id'] == num:
                            while True:
                                try:
                                    print("=>"*30)
                                    i['año_nacimiento'] = int(input("Ingresa una nueva fecha de nacimiento: "))
                                    print("<="*30)
                                    break
                                except ValueError:
                                    print("[-] ERROR. SOLO NÚMEROS")
                            i['edad'] = 2026 - i['año_nacimiento']
                            print(f"Alumno modificado: id: {i['id']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Nacimiento: {i['año_nacimiento']}")
            elif modificar == 2:
                for i in lista:
                        if i['id'] == num:
                            print("=>"*30)
                            i['nombre'] = input("Ingresa el nombre: ").lower().strip()
                            print("<="*30)
                            print(f"Alumno modificado: id: {i['id']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Nacimiento: {i['año_nacimiento']}")
            elif modificar == 3:
                for i in lista:
                        if i['id'] == num:
                            while True:
                                try:
                                    print("=>"*30)
                                    i['apellido'] = input("Ingresa el nuevo apellido: ").lower().strip()
                                    print("<="*30)
                                    break
                                except ValueError:
                                    print("[-] ERROR. SOLO LETRAS")
                            print(f"Alumno modificado: id: {i['id']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Nacimiento: {i['año_nacimiento']}")
            elif modificar == 4:
                print("=> VOLVIENDO AL MENÚ PRINCPIPAL ...")
                break
            
def elimiar(lista_1):
        iteracion(lista_usuarios)
        while True:
            try:
                print("=>"*30)
                elim = int(input("Selecciona el id del alumno a modificar: "))
                print("<="*30)
                break
            except ValueError:
                print("[-] ERROR. SOLO NÚMEROS ENTEROS")
                print("="*30)
        lista_1[:] = [n for n in lista_usuarios if n['id'] != elim]
        print(f"[+] Alumno con id : {elim} eliminado con éxito.")
        
def buscar(lista_2):
        while True:

            print("=>"*30)
            apell_nomb = input("Ingresa nombre, apellido o una letra (ENTER para salir): ").lower().strip()
            print("<="*30)

            if apell_nomb == "":
                break
            temp = []
            bandera = False
            for x in lista_2:
                if apell_nomb in x['nombre'] or apell_nomb in x['apellido']:
                    temp.append(x)
                    bandera = True
            if bandera == True:
                iteracion(temp)
            else:
                print(f"El alumno {apell_nomb} no existe")


def menu():
    print("\n"+"="*30)
    print("""
        --- MENÚ PRINCIPAL ---
        1- CREAR ALUMNO
        2- MODIFICAR ALUMNO
        3- ELIMINAR ALUMNO
        4- LISTAR ALUMNOS
        5- BUSCAR POR APELLIDO, NOMBRE O LETRA
        6- ABRIR MENU
        7- BUSCAR POR ID
        8- FILTRAR POR AÑO DE NACIMIENTO 
        9- SALIR
        ----------------------
        """)


def id(liste):
    mostrar = False
    while True:
        while True:
            try:
                print("=>"*30)
                idd = int(input("Ingresa el ID a encontrar ( 0 para salir): "))
                print("<="*30)
                if idd == 0:
                    break
                break
            except ValueError:
                print("[-] ERROR. SOLO NÚMEROS ENTEROS")
        if idd == 0:
            break
        for i in liste:
            if i['id'] == idd:
                print(f"id: {i['id']} | Nombre: {i['nombre']} | Apellido: {i['apellido']} | Nacimiento: {i['año_nacimiento']}")
                mostrar = True
        if not mostrar:
            print("[-] No se encontró ningún alumno con ese ID.")


def filt_nac(listaa):
    print("=>"*30)
    print("Filtrar por fecha de nacimiento")
    print("<="*30)
    while True:
        try:
            año_desde = int(input("Ingresa el año desde: "))
            break
        except ValueError:
            print("[-] ERROR. SOLO NÚMEROS ENTEROS")
    while True:
        try:
            año_hasta = int(input("Ingresa el año hasta: "))
            break
        except ValueError:
            print("[-] ERROR. SOLO NÚMEROS ENTEROS")
    temp = []
    for i in listaa:
        if i["año_nacimiento"] >= año_desde and i["año_nacimiento"] <= año_hasta:
            temp.append(i)
    iteracion(temp)
        



###################################################################################################
###################################################################################################

##### INGLES

def run():
    print("="*30)
    print("STUDENT MANAGEMENT")
    print("="*30)

    while True:
        display_menu()
        while True:
            try:
                print("=>"*30)
                option = int(input("Choose an option ('9' to exit): "))
                print("<="*30)
                break
            except ValueError:
                print("[-] Enter numbers only...")
        if option == 1:
            create(database_records)
        elif option == 2:
            modify(database_records)
        elif option == 3:
            delete(database_records)
        elif option == 4:
            display_all(database_records)
        elif option == 5:
            search_text(database_records)
        elif option == 6:
            display_menu()
        elif option == 7:
            display_all(database_records)
            search_id(database_records)
        elif option == 8:
            filter_year(database_records)
        elif option == 9:
            print("[-] CLOSING THE PROGRAM ...")
            break


database_records = [
    {"id": 1, "nombre": "ana", "apellido": "garcía", "año_nacimiento": 1995, "edad": 31},
    {"id": 2, "nombre": "luis", "apellido": "rodríguez", "año_nacimiento": 1988, "edad": 37},
    {"id": 3, "nombre": "maría", "apellido": "lópez", "año_nacimiento": 2001, "edad": 25},
    {"id": 4, "nombre": "carlos", "apellido": "martínez", "año_nacimiento": 1993, "edad": 33},
    {"id": 5, "nombre": "elena", "apellido": "gómez", "año_nacimiento": 1997, "edad": 29},
    {"id": 6, "nombre": "juan", "apellido": "sánchez", "año_nacimiento": 1990, "edad": 36},
    {"id": 7, "nombre": "sofía", "apellido": "pérez", "año_nacimiento": 2003, "edad": 23},
    {"id": 8, "nombre": "diego", "apellido": "gonzález", "año_nacimiento": 1985, "edad": 40},
    {"id": 9, "nombre": "lucía", "apellido": "fernández", "año_nacimiento": 1999, "edad": 27},
    {"id": 10, "nombre": "javier", "apellido": "ruiz", "año_nacimiento": 1992, "edad": 33},
    {"id": 11, "nombre": "marta", "apellido": "díaz", "año_nacimiento": 1996, "edad": 29},
    {"id": 12, "nombre": "alejandro", "apellido": "alvarez", "año_nacimiento": 1987, "edad": 39},
    {"id": 13, "nombre": "laura", "apellido": "moreno", "año_nacimiento": 1994, "edad": 32},
    {"id": 14, "nombre": "manuel", "apellido": "muñoz", "año_nacimiento": 1989, "edad": 37},
    {"id": 15, "nombre": "paula", "apellido": "jiménez", "año_nacimiento": 2002, "edad": 24},
    {"id": 16, "nombre": "mateo", "apellido": "hernández", "año_nacimiento": 1991, "edad": 35},
    {"id": 17, "nombre": "sara", "apellido": "romero", "año_nacimiento": 1998, "edad": 27},
    {"id": 18, "nombre": "david", "apellido": "alonso", "año_nacimiento": 1984, "edad": 42},
    {"id": 19, "nombre": "daniela", "apellido": "gutiérrez", "año_nacimiento": 2000, "edad": 25},
    {"id": 20, "nombre": "jorge", "apellido": "navarro", "año_nacimiento": 1993, "edad": 33}
]


def display_all(lists):
    students_lambda = lambda current_list: [print(f"Id: {p['id']} | Name: {p['nombre'].capitalize()} | Last Name: {p['apellido'].capitalize()} | Birth Year: {p['año_nacimiento']} | Age: {p['edad']}") for p in current_list]
    print("="*30)
    students_lambda(lists)
    print("="*30)


def create(target_list):
    while True:
        print("=>"*30)
        name = input("Enter name: ").strip().lower()
        print("<="*30)
        if name == "":
            print("[-] ERROR. REQUIRED FIELD!")
            continue
        else:
            break
    while True:
        print("=>"*30)
        last_name = input("Enter last name: ").strip().lower()
        print("<="*30)
        if last_name == "":
            print("[-] ERROR. REQUIRED FIELD!")
            continue
        else:
            break
    while True:
        try:
            print("=>"*30)
            birth_year = int(input("Enter birth year: "))
            print("<="*30)
            break
        except ValueError:
            print("[-] ERROR. INTEGERS ONLY")
    while True:
        try:
            print("=>"*30)
            age = int(input("Enter age: "))
            print("<="*30)
            break
        except ValueError:
            print("[-] ERROR. INTEGERS ONLY")
            
    exists = any(p['nombre'] == name and p['apellido'] == last_name for p in target_list)
    if exists:
        print("[-] The student already exists in the list")
    else:
        new_id = len(target_list) + 1    
        target_list.append({"id": new_id, "nombre": name, "apellido": last_name, "año_nacimiento": birth_year, "edad": age})
        print("[+] Student successfully registered.")


def modify(target_list):
    display_all(database_records)
    while True:
        try:
            print("=>"*30)
            num = int(input("Select the student ID to modify: "))
            print("<="*30)
            break
        except ValueError:
            print("[-] ERROR. INTEGERS ONLY")
            print("="*30)
    print("""
        1) BIRTH YEAR
        2) NAME
        3) LAST NAME
        4) EXIT
        """)
    while True:
        while True:
            try:
                print("=>"*30)
                modify_option = int(input("What do you want to modify? (1, 2, 3, 4): "))
                print("<="*30)
                break
            except ValueError:
                print("[-] ERROR. NUMBERS ONLY")
                print("="*30)
        
        if modify_option == 1:
            for i in target_list:
                if i['id'] == num:
                    while True:
                        try:
                            print("=>"*30)
                            i['año_nacimiento'] = int(input("Enter a new birth year: "))
                            print("<="*30)
                            break
                        except ValueError:
                            print("[-] ERROR. NUMBERS ONLY")
                    i['edad'] = 2026 - i['año_nacimiento']
                    print(f"Student modified: Id: {i['id']} | Name: {i['nombre']} | Last Name: {i['apellido']} | Birth Year: {i['año_nacimiento']}")
        elif modify_option == 2:
            for i in target_list:
                if i['id'] == num:
                    print("=>"*30)
                    i['nombre'] = input("Enter name: ").lower().strip()
                    print("<="*30)
                    print(f"Student modified: Id: {i['id']} | Name: {i['nombre']} | Last Name: {i['apellido']} | Birth Year: {i['año_nacimiento']}")
        elif modify_option == 3:
            for i in target_list:
                if i['id'] == num:
                    print("=>"*30)
                    i['apellido'] = input("Enter last name: ").lower().strip()
                    print("<="*30)
                    print(f"Student modified: Id: {i['id']} | Name: {i['nombre']} | Last Name: {i['apellido']} | Birth Year: {i['año_nacimiento']}")
        elif modify_option == 4:
            print("=> RETURNING TO MAIN MENU ...")
            break


def delete(target_list):
    display_all(database_records)
    while True:
        try:
            print("=>"*30)
            elim = int(input("Select the student ID to delete: "))
            print("<="*30)
            break
        except ValueError:
            print("[-] ERROR. INTEGERS ONLY")
            print("="*30)
            
    found_student = None
    for n in database_records:
        if n['id'] == elim:
            found_student = n
            break
    if found_student:
        database_records.remove(found_student)
        print(f"[+] Student with id: {elim} successfully deleted.")
    else:
        print("[-] Student ID not found.")


def search_text(target_list):
    while True:
        print("=>"*30)
        search_query = input("Enter name, last name or letter (ENTER to exit): ").lower().strip()
        print("<="*30)
        if search_query == "":
            break
        temp_list = []
        flag = False
        for x in target_list:
            if search_query in x['nombre'] or search_query in x['apellido']:
                temp_list.append(x)
                flag = True
        if flag == True:
            display_all(temp_list)
        else:
            print(f"The student {search_query} does not exist")


def display_menu():
    print("\n"+"="*30)
    print("""
        --- MAIN MENU ---
        1- CREATE STUDENT
        2- MODIFY STUDENT
        3- DELETE STUDENT
        4- LIST STUDENTS
        5- SEARCH BY LAST NAME, NAME OR LETTER
        6- OPEN MENU
        7- SEARCH BY ID
        8- FILTER BY BIRTH YEAR
        9- EXIT
        -----------------
        """)


def search_id(target_list):
    show = False
    while True:
        while True:
            try:
                print("=>"*30)
                student_id = int(input("Enter the ID to find (0 to exit): "))
                print("<="*30)
                break
            except ValueError:
                print("[-] ERROR. INTEGERS ONLY")
        if student_id == 0:
            break
        for i in target_list:
            if i['id'] == student_id:
                print(f"Id: {i['id']} | Name: {i['nombre']} | Last Name: {i['apellido']} | Birth Year: {i['año_nacimiento']}")
                show = True
        if not show:
            print("[-] No student was found with that ID.")


def filter_year(target_list):
    print("=>"*30)
    print("Filter by birth year")
    print("<="*30)
    while True:
        try:
            year_from = int(input("Enter year from: "))
            break
        except ValueError:
            print("[-] ERROR. INTEGERS ONLY")
    while True:
        try:
            year_to = int(input("Enter year to: "))
            break
        except ValueError:
            print("[-] ERROR. INTEGERS ONLY")
    temp_list = []
    for i in target_list:
        if i["año_nacimiento"] >= year_from and i["año_nacimiento"] <= year_to:
            temp_list.append(i)
    display_all(temp_list)


idioma()