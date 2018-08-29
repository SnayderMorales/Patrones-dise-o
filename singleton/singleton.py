#extraido de https://jarroba.com/patron-singleton-python-ejemplos/

#Clase singleton
class singleton(object):
    #Constructor
    def __init__(self):
        __instance = None
        #Metodo de si la instancia ya esta inicializada no la
        def __new__(cls):
            if singleton.__instance is None:
                singleton.__instance = object.__new__(cls)
                return singleton.__instance
