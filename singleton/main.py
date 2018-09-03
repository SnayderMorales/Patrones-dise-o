from convertor import convertor
from singleton import singleton
import os
os.system('cls')
#Singleton
while True:
    print ("Selecciona una opcion")
    print ("1 - Desea convertir cm a metro")
    print ("\t2 - Desea convertir klg a G")
    print ("\t3 - Desea salir")
    opcion = input("inserta un numero valor >> ")
    if(opcion==1):
        metro=convertor()
        cm=input("Digite cm >>")
        print metro.metro(cm)
        print "Instancia en el main #2"

    elif(opcion==2):
        gramos=convertor()
        klg=input("Digite klg >>")
        print "%.6f" %(gramos.gramos(klg))
        print "Instancia en el main #2"
    else:
        print "saliendo.."
        break
