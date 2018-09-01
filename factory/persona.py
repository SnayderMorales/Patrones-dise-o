from pypattyrn.creational.factory import Factory  # This is just an interface  # This is just an interface
#Clase pricipal que crea las clases secundaria
class persona(Factory):
    """docstring for persona."""
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    #Metodo para elegir cual clase vamos a crear
    def create(self, tipo_persona):
        if tipo_persona=='estudiante':
            carrera=input("Digite carrera >>");
            return estudiante(carrera)
        elif tipo_persona=='docente':
            curso=input("Digite Curso >>");
            return docente(curso)
        else:
            return None


#Clase estudiante(secundaria)
class estudiante(object):
    """docstring for estudiante."""
    def __init__(self, carrera):
        self.carrera= carrera
    def __str__(self):
        return "Estudia la carrera : "
#Clase docente(secundaria)
class docente(object):
    """docstring for docente."""

    def __init__(self, curso):
        self.curso = curso
    def __str__(self):
        return "Ensena un curso de: "

#Main
while True:
    print ("Selecciona una opcion")
    print ("1 - Desea crear estudiante")
    print ("\t2 - Desea crear docente")
    print ("\t3 - Desea salir")
    opcion = input("inserta un numero valor >> ")
    if(opcion=='1'):
        jairo = persona("jairo","gomez")
        carrera=jairo.create('estudiante');
        print(jairo.nombre," ",jairo.apellido,str(carrera),carrera.carrera)

    elif(opcion=='2'):
        jairo = persona("jairo","gomez")
        curso=jairo.create('docente');
        print(jairo.nombre," ",jairo.apellido,str(curso),curso.curso)
    else:
        print ("saliendo..")
        break
