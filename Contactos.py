#Contactos
import json

ruta = "C:\\Users\\artur\\OneDrive\\Escritorio\\Prueba.txt"

class Contacto:

    contactos = []

    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        return f"\nNombre: {self.nombre} \nTelefono: {self.telefono} \nCorreo: {self.correo} \nDireccion: {self.direccion}"


    @staticmethod
    def AgregarContacto(contacto1):
        Contacto.CargarContactos()

        #Validar si el nombre ya existe
        if any(contacto['Nombre'] == contacto1.nombre for contacto in Contacto.contactos):
            print("\nNo se pudo agregar el contacto porque el nombre ya existe!")
        else:
            # Agregar el nuevo contacto a la lista
            Contacto.contactos.append(contacto1.ConvertirADiccionario())

            # Guardar la lista completa de contactos en el archivo con formato JSON válido
            Contacto.AlmacenarContactos("\nContacto agregado con exito!", "\nNo se pudo agregar el contacto, intentelo de nuevo!", Contacto.contactos)
                    
        
    @staticmethod
    def EliminarContacto(id):
        Contacto.CargarContactos()

        if id > 0 and id <= len(Contacto.contactos):
            Contacto.contactos.pop(id - 1)

            Contacto.AlmacenarContactos("\nContacto Eliminado con exito!", "\nError, no se pudo eliminar el contacto", Contacto.contactos)                     
        else:
            print("\nNo se encontro el contacto.")

    
    @staticmethod
    def MostrarContactos():
        Contacto.CargarContactos()
            
        if Contacto.contactos:
            contador = 1
            print("")
            for i in Contacto.contactos:
                print(f"ID: {contador} {i}")   
                contador+=1        

        else:
            print("\nNo hay contactos.")
        

    @staticmethod
    def EditarContacto(indice, nombre = None, telefono = None, correo = None, direccion = None):
        Contacto.CargarContactos()

        if indice > 0 and indice <= len(Contacto.contactos):
            contacto = Contacto.contactos[indice - 1]

            if nombre is not None:
                contacto['Nombre'] = nombre
            if telefono is not None:
                contacto["Telefono"] = telefono
            if correo is not None:
                contacto["Correo"] = correo
            if direccion is not None:
                contacto["Direccion"] = direccion

            Contacto.AlmacenarContactos("\nContacto editado con exito!", "\nError al guardar los cambios!", Contacto.contactos)
        else:
            print("\nIndice del contacto invalido.")


    @staticmethod
    def BuscarContacto(nombre = None, telefono = None):
        Contacto.CargarContactos()

        if Contacto.contactos:
            encontrado = False
            print("")

            for i in Contacto.contactos:
                encontrarNombre = (nombre is not None and i['Nombre'].lower() == nombre.lower())
                encontrarTelefono = (telefono is not None and i['Telefono'] == telefono)

                if encontrarNombre or encontrarTelefono:
                    encontrado = True
                    print("Contacto/os encontrado")
                    print(i)

            if not encontrado:
                print("\nNo hay contactos con ese nombre o numero de telefono!")
        else:
            print("\nNo hay contactos guardados!")


    @staticmethod
    def OrdenarContactos():
        Contacto.CargarContactos()
            
        contactosOrdenados = sorted(Contacto.contactos, key=lambda i: i['Nombre'].lower())

        Contacto.AlmacenarContactos("\nContactos ordenados con exito!", "\nError al ordenar los datos, intentelo de nuevo!", contactosOrdenados)
           

    @staticmethod
    def CargarContactos():
        try:
            with open(ruta, 'r') as archivo:
                try:
                    Contacto.contactos = json.load(archivo)
                except json.JSONDecodeError:
                    Contacto.contactos = []
        except FileNotFoundError:
            Contacto.contactos = []

    
    @staticmethod
    def AlmacenarContactos(mensaje1, mensaje2, listaContactos):
        try:
            with open(ruta, 'w') as archivo:
                json.dump(listaContactos, archivo, indent=4)
                print(f"\n{mensaje1}")
        except:
            print(f"\n{mensaje2}")


    def ConvertirADiccionario(self):
        formatoJson = {
            "Nombre": self.nombre,
            "Telefono":  self.telefono,
            "Correo": self.correo,
            "Direccion": self.direccion
        }
        return formatoJson
    