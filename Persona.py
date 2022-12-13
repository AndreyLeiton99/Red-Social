'''class Persona:
    nombre = ""
    estadoCivil = ""
    direccion = ""
    comentarios = []

    def __init__(self, nombre, estadoCivil, direccion):
        self.nombre = nombre
        self.estadoCivil = estadoCivil
        self.direccion = direccion

    def __str__(self):
        return f"<< Datos personales >>\nNombre completo: {self.nombre}\n" \
               f"Estado Civil: {self.estadoCivil}\n" \
               f"Direccion: {self.direccion}\n"

    def showComments(self):
        cadena = f"\n<< Comentarios de {self.nombre} >>\n\n"

        aux = self.comentarios
        for i in range(len(aux)):
            cadena += f"{aux[-1]} \n"
            aux.pop()

        print(cadena)

    @classmethod
    def addCommment(cls, comentarios, post):
        comentarios.append(post)
        # print(comentarios)
        print("Comentario agregado!")'''


'''
persona = Persona("Andrey Leiton", "Soltero", "El roble")
persona.addComment(persona.comentarios, "Primer comentario")
persona.addComment(persona.comentarios, "Segundo comentario")
persona.addComment(persona.comentarios, "Tercero comentario")
persona.addComment(persona.comentarios, "Cuarto comentario")
persona.showComments()
'''
