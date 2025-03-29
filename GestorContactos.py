#Gestor de Contactos

import Contactos
import re

validarCorreo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
validarTelefono = r'^\+?[0-9]{8,15}$'

print("Bienvenido al sistema!")

while True:    
    print("\n1. Agregar Contacto")
    print("2. Eliminar Contacto")
    print("3. Editar Contacto")
    print("4. Mostar todos los Contactos")
    print("5. Buscar Contacto")
    print("6. Ordenar Contactos")
    print("0. Salir")

    try:
        opc = int(input("\nIngrese una opcion: "))

    except:
        print("\nError, ingrese una opcion valida")

    else: 
        match opc:
            case 1:
                nombre = input("\nIngrese el nombre: ")
                telf = input("Ingrese el numero de telefono: ")
                correo = input("Ingrese el correo: ")
                direccion = input("Ingrese la direccion: ")

                if nombre is not None and telf is not None and correo is not None and direccion is not None:
                    if re.match(validarTelefono, telf):
                        if re.match(validarCorreo, correo):
                            telf = int(telf) if telf else None
                            
                            contacto = Contactos.Contacto(nombre, telf, correo, direccion)
                    
                            Contactos.Contacto.AgregarContacto(contacto)
                        else: 
                            print("Correo electronico no valido!")
                    else: 
                        print("Numero de telefono no valido!") 
                else: 
                    print("\nDebe de llenar todos los campos para poder crear un nuevo contacto!")
                
            case 2: 
                Contactos.Contacto.MostrarContactos()
                try:
                    id = int(input("\nIngrese el id del contacto a eliminar: "))
                
                except:
                    print("\nError, ingrese un id Valido")
                
                else:
                    Contactos.Contacto.EliminarContacto(id)
                
            case 3:
                Contactos.Contacto.MostrarContactos()

                try:
                    id = int(input("\nIngrese el id del contacto a editar: "))    

                except:
                    print("\nIngrese un id valido")
                
                else: 
                    print("\nDeje en blanco/De un enter para no modificar")
                    nombre = input("Ingrese el nombre: ")
                    telf = input("Ingrese el numero de telefono: ")
                    correo = input("Ingrese el correo: ")
                    direccion = input("Ingrese la direccion: ")

                    if re.match(validarTelefono, telf):
                        if re.match(validarCorreo, correo):
                            telf = int(telf) if telf else None
                    
                            Contactos.Contacto.EditarContacto(id, nombre if nombre else None, telf if telf else None, correo if correo else None, direccion if direccion else None)
                        else: 
                            print("\nEl correo electronico no es valido!")
                    else:
                        print("\nEl numero de telefono ingresado no es valido!")
            case 4:
                Contactos.Contacto.MostrarContactos()
            
            case 5:
                print("\n1) Buscar por nombre")
                print("2) Buscar por numero de telefono")
                opc = int(input("Seleccione su critero de busqueda: "))

                match opc:
                    case 1:
                        criterio = input("\nIngrese el nombre del contacto: ")

                        Contactos.Contacto.BuscarContacto(criterio, None)
                    case 2:
                        criterio = int(input("\nIngrese el numero de telefono del contacto: "))

                        Contactos.Contacto.BuscarContacto(None, criterio)
                    case _: 
                        print("\nOpcion incorrecta, intentelo de nuevo!")

            case 6:
                Contactos.Contacto.OrdenarContactos()
                
            case 0:
                print("\nSaliendo del programa!\n")
                break

            case _:
                print("\nOpcion incorrecta, intentelo de nuevo!")
