from PyPattyrn.persona import docente
from PyPattyrn.persona import persona
from PyPattyrn.pypattyrn.creational.factory import Factory
jairo = persona("jairo","gomez")
curso=jairo.create('docente');
print(jairo.nombre," ",jairo.apellido,str(curso),curso.curso)
