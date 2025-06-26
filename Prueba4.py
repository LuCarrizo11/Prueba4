
#Usuarios tiene Nombre, sexo y contraseña

usuarios={
     "nombres":["lu","tom"],
     "sexo":["M","F"],
     "contra":["12345678","87654321"]
}

TF=False
option=0
def ingresar_usuario():
    global TF
    nombre=input("Ingrese su nombre: ").lower()
    for n in usuarios["nombres"]:
        if nombre == n:
            print("El nombre que ha ingresado ya ha sido utilizado")
            return False
    if True:
        sexo=input("Ingrese su sexo ('F' o 'M'): ").lower()
        if sexo.lower()=="f" or sexo.lower()=="m":
            print("Sexo guardado exitosamente")  
        else:
            print("Por favor ingrese 'F' o 'M' solamente")
    if True and sexo.lower()=="f" or sexo.lower()=="m":
        contraseña=input("Ingrese su contraseña: ")
        contraseña=contraseña.strip()
        if len(contraseña)>=8 and True:
            usuarios["nombres"].append(nombre)
            usuarios["sexo"].append(sexo)
            usuarios["contra"].append(contraseña)
            print("Datos ingresados correctamente")
        else:
            print("Por favor ingrese una contraseña de 8 o mas caracteres")

def buscar_usuario():
    nombre=input("Ingrese el nombre que desea buscar: ")
    num=0
    for n in usuarios["nombres"]:
        num+=1
        if nombre == n:
            print(f"Nombre del usuario: {usuarios["nombres"][num-1]}")
            print(f"Sexo del usuario: {usuarios["sexo"][num-1]}")
            print(f"Contraseña del usuario: {usuarios["contra"][num-1]}")
            return False
    if True:
        print("Usuario no encontrado")

def eliminar_usuario():
    nombre=input("Ingrese el nombre del usuario que desea eliminar: ")
    num=0
    for n in usuarios["nombres"]:
        num+=1
        if nombre == n:
            usuarios.popitem["nombres"][num-1]
            #no pude aregglar el pop y el remove :C profe misericordia
            print(usuarios)
            print("Usuario eliminado")

while option!=4:
    try:
        print("MENU PRINCIPAL")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir")
        option=int(input("Ingrese opcion: "))
        match option:
            case 1:
                ingresar_usuario()
            case 2:
                buscar_usuario()
            case 3:
                eliminar_usuario()
            case 4:
                print("Gracias por su preferencia :)")
            case _:
                print("Opcion invalida, por favor eliga un numero entre 1 y 4")
    except ValueError:
        print("Ha ocurrido un de valores :(")
    except:
        print("Ha currido un error desconocido")