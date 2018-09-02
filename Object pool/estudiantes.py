from pypattyrn.creational.pool import Reusable, Pool

#Clase que vamos a reusar
class estudiantes(Reusable):
    """docstring for estudiantes."""
    def __init__(self, nombre,apellido,codigo):
        self.nombre = nombre
        self.apellido=apellido
        self.codigo = codigo
        super().__init__()

#Clase donde almacenaremos los objetos de estudiante que reusaremos
class estudiantePool(Pool):
    """docstring for ."""
    def __init__(self):
        super().__init__(estudiantes,'hola','que','37486')

estudiante_pool = estudiantePool()
#inicialzamos el pool de objeto inicializado
estudiante_uno = estudiante_pool.acquire()
estudiante_dos = estudiante_pool.acquire()
estudiante_dos = estudiantes('Esnayder','Morales', '3' )

estudiante_pool.release(estudiante_uno)
estudiante_tres = estudiante_pool.acquire()

estudiante_pool.release(estudiante_dos)
estudiante_cuatro = estudiante_pool.acquire()

#Estudiante uno y tres pertenecen al mismo pool de objeto inicializado
print ("uno",estudiante_uno)
print ("tres",estudiante_tres)
#Estudiante dos y cuatro pertenecen al mismo pool de objeto inicializado
print ("dos",estudiante_dos)
print ("cuatro",estudiante_cuatro)
