from pypattyrn.structural.flyweight import FlyweightMeta
#Creamos una clase que manejara muchos datos y para los datos iguales se inicializara
#la misma instancia
class pelota(object, metaclass=FlyweightMeta):
    """docstring for Pelota."""
    def __init__(self, color, area):
        self.color = color
        self.area = area

pelota1 = pelota('rojo','4 cm cuadrado')
pelota2 = pelota('rojo','5 cm cuadrado')
pelota3 = pelota('rojo','4 cm cuadrado')

#Aqui imprimimos la misma instancia para la pelota 1 y la pelota 3 porque son iguales
#Y diferentes instancia para la pelota 1 y 2 por que son diferentes
print(pelota1,"=",pelota3)
print(pelota1,"!=",pelota2)
