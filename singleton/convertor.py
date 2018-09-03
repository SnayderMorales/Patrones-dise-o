from singleton import singleton
class convertor(singleton):
    global instancia
    instancia = singleton()
    def metro(self, cm):
        print ("Instancia iniciada en el metodo #1")
        #Aqui imprimimos la instancia
        print (instancia)
        return cm/100.00

    def gramos(self,klg):
        print ("Instancia iniciada en el metodo #1")
        #Aqui imprimimos la instancia
        print (instancia)
        return klg/1000.00
