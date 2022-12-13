
class Nodo:

    def __init__(self):
        '''self.dato = Persona()
        self.sgte = Nodo()
        self.ady = Arista()'''
        self.dato = None # Persona
        self.sgte = None # Nodo
        self.ady = None # Arista

    def __str__(self):
        return f"{self.dato}"


class Arista:
    # destino = Nodo()
    # sgte = Arista()

    def __init__(self):
        self.destino = Nodo()
        self.sgte = Arista()


class Grafo:

    def __init__(self):
        self.head = None

    @classmethod
    def insertar_nodo(cls, self, dato):
        nuevo = Nodo()
        t = Nodo()

        nuevo.dato = dato

        if self.head is None:
            self.head = nuevo
            print("Primer usuario creado")
        else:
            t = self.head
            while t.sgte is not None:
                t = t.sgte

                t.sgte = nuevo
                print("Usuario creado correctamente!\n")


    @classmethod
    def mostrar_grafo(cls, self):
        ptr = Nodo()
        ar = Arista()
        ptr = self.head
        print("USUARIO   			 |  LISTA DE AMIGOS\n")
        print("_________________________________________________\n")

        while ptr is not None:
            print(f"   {ptr.dato.nombre} |")
            if ptr.ady is not None:
                ar = ptr.ady
                while ar is not None:
                    print(f" {ar.destino.dato.nombre} ,")
                    ar = ar.sgte

            ptr = ptr.sgte
            print("")
