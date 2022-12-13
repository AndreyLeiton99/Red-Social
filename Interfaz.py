class Persona:

    def __init__(self, nombre, estadoCivil, direccion):
        self.nombre = nombre
        self.estadoCivil = estadoCivil
        self.direccion = direccion
        self.comentarios = []

    def __str__(self):
        return f"\n<< -------Datos personales------- >>" \
               f"\n[Nombre completo]...................{self.nombre}\n" \
               f"[Estado Civil]......................{self.estadoCivil}\n" \
               f"[Dirección].........................{self.direccion}\n"

    def showComments(self):
        cadena = f'\n<< Comentarios de "{self.nombre}" >>\n\n'

        aux = self.comentarios.copy()  # si se quita el .copy() vacia directamente la lista de comentarios
        if len(aux) == 0:
            cadena += f'El usuario "{self.nombre}" no ha publicado comentarios.\n'
        else:
            for i in range(len(aux)):
                cadena += f"-> {aux[-1]} \n"
                aux.pop()

        print(cadena)

    def sacaNombre(self):
        return self.nombre

    def sacaComentario(self):
        if self.comentarios:
            aux = self.comentarios.copy()
            aux2 = aux.pop()
        else:
            return '-------No hay comentarios-------'
        return aux2
    @classmethod
    def addComment(cls, self, post):
        self.comentarios.append(post)
        print("-------¡Comentario publicado!-------")


class Nodo:
    def __init__(self, i):
        self.id = i
        self.amigos = []

    def __str__(self):
        stringstream = "Amigos: "
        for friend in self.amigos:
            stringstream += f"{friend.nombre}, "
        return stringstream

    def buscarAmigo(self, name):
        added = False
        for i in self.amigos:
            if i.nombre == name:
                added = True
        return added

    def agregaAmigo(self, v):
        if self.buscarAmigo(v.nombre):
            print("¡Ustedes ya son amigos! :)")
        else:
            self.amigos.append(v)
            print("Amigo agregado.")

    def mostrarAmigosNodo(self,opc):
        lista = []
        if opc == '1':
            for i in self.amigos:
                print(i)
                i.showComments()
        elif opc == '2':
            for i in self.amigos:
                aux = i.sacaNombre()
                lista.append(aux)
            return lista

    def mostrarComentarioNodo(self):
        contador = 1
        for i in self.amigos:
            print(f'Ultimo comentario del usuario "{i.nombre}"\n'
                  f'❦ {i.sacaComentario()}\n')

class Grafo:
    def __init__(self):
        self.nodo = {}

    def agregaNodo(self, v):
        if self.buscarNodo(v.nombre):
            print("-------¡Usuario ya existente!-------")
            pause()
        else:
            self.nodo[v] = Nodo(v)
            print("-------¡Usuario creado!-------")
            print(v)

    def buscarNodo(self, name):
        exist = False
        for i in self.nodo:
            if i.nombre == name:
                exist = True
                break
        return exist

    def usarNodo(self, name):
        persona = None
        for i in self.nodo:
            if i.nombre == name:
                persona = i
                break
        return persona

    def actualizarDatosNodo(self, name, state, direction):
        for i in self.nodo:
            if i.nombre == name:
                i.nombre = name
                i.estadoCivil = state
                i.direccion = direction
                print("-------Datos actualizados correctamente-------\n")
                break

    def actualizarNodo(self, user):
        for i in self.nodo:
            if i.nombre == user.nombre:
                i.nombre = user.nombre
                i.estadoCivil = user.estadoCivil
                i.direccion = user.direccion
                i.comentarios = user.comentarios
                break

    def mostrarAmigos(self, user, opc):
        lista = []
        if opc == '1':
            for i in self.nodo:
                if i.nombre == user.nombre:
                    self.nodo[user].mostrarAmigosNodo('1')
                    break
        elif opc == '2':
            #for i in self.nodo[user].mostrarAmigosNodo('2'):
            lista = self.nodo[user].mostrarAmigosNodo('2')
            return lista
        elif opc == '3':
            for i in self.nodo:
                if i.nombre == user.nombre:
                    self.nodo[user].mostrarComentarioNodo()

    def agregaArista(self, nodo1, nodo2):
        if self.buscarNodo(nodo1.nombre) and self.buscarNodo(nodo2.nombre):
            self.nodo[nodo1].agregaAmigo(nodo2)
            self.nodo[nodo2].agregaAmigo(nodo1)
        else:
            if not self.buscarNodo(nodo1.nombre) and not self.buscarNodo(nodo2.nombre):
                print(f"-------Estos usuarios no existen-------")
                pause()
            if not self.buscarNodo(nodo1.nombre):
                print(f"    El usuario {nodo1.nombre} no existe! ")
                pause()
            if not self.buscarNodo(nodo2.nombre):
                print(f"    El usuario {nodo2.nombre} no existe! ")
                pause()

    def mostrarSugerencias(self, user):
        aux = []
        for i in self.nodo:
            if i.nombre == (user):
                #print(f'entro con {user}')
                aux = self.mostrarAmigos(i,'2')
        return aux

    def filtraSugerencias(self, user, lista1, lista2):
        lista = []
        lista = set(lista1) - set(lista2)
        lista = set(lista) - set(user.nombre)
        if lista:
            return lista
        else:
            return 'No hay sugerencias de amigos, lo sentimos \n' \
                   '                  :( '

def pause():
    print("\nPresione ENTER para continuar...", end="")
    input()


def menu():
    grafo = Grafo()

    repeat = True
    while repeat:
        print("\n<< --------|F A C E B R O O K|-------- >>\n\n")

        print("1- Crear usuario\n2- Ingresar\n3- Salir")
        opcion = input("Bienvenido/a, digite la opción que desea realizar: ")

        if opcion == "1":
            print("\n< -------Creando usuario------- >\n")
            name = input("Digite su nombre: ")
            state = input("Digite su estado civil: ")
            direction = input("Digite su dirección: ")
            grafo.agregaNodo(Persona(name, state, direction))

        elif opcion == "2":
            print("\n < -------Ingresar------- >\n\n")
            username = input("Por favor, digite su nombre de usuario: ")

            if grafo.buscarNodo(username):
                user = grafo.usarNodo(username)
                session = True
                while session:
                    print(f"\n\nBienvenido/a {user.nombre}\n\n")
                    print(" < -------MENÚ------- >")
                    print("1- Datos personales\n2- Agregar amigos\n3- Comentarios\n4- Ver amigos\n"
                          "5- Publicaciones de amigos\n6- Cerrar sesión")
                    op = input("¿Qué desea realizar? -> ")

                    if op == "1":
                        print(user)
                        print("¿Desea actualizar su informacion personal?\n1- Si\n2- No\n -> ")
                        opc = input()

                        if opc == "1":
                            name = input("Digite su nuevo nombre: ")
                            state = input("Digite su nuevo estado civil: ")
                            direction = input("Digite su nueva dirección: ")
                            user.nombre = name
                            user.estadoCivil = state
                            user.direccion = direction
                            grafo.actualizarDatosNodo(name, state, direction)
                            pause()

                        if opc != "1" and opc != "2":
                            print("-------¡Opción inválida!-------")

                    elif op == "2":
                        print("\n< -------Agregar amigos------- >")

                        print("\n1- Buscar amigos\n2- Sugerencias\n3- Salir")
                        opc = input("Digite una opcion: ")

                        if opc == "1":
                            print("\nDigite el nombre de usuario que desea buscar: ")
                            username = input()
                            if username == user.nombre:
                                print("Buen intento, pero el usuario ya esxiste") #este compa le sabe XD
                            else:
                                if grafo.buscarNodo(username):
                                    print("-------Usuario encontrado-------\n")
                                    print(grafo.usarNodo(username))
                                    print(f"Desea agregar a {username}? 1-Si   2-No")
                                    add = input(" -> ")
                                    if add == "1":
                                        grafo.agregaArista(user, grafo.usarNodo(username))
                                        grafo.actualizarNodo(user)   # importante actualizar en el grafo
                                else:
                                    print("-------Usuario no encontrado-------")

                        elif opc == "2":
                            print('\n-----Sugerencia de Amgios-----')
                            aux = []
                            lista = []
                            listaFinal = []
                            contador = 1

                            aux = grafo.mostrarAmigos(user, '2')
                            for i in aux:
                                lista += (grafo.mostrarSugerencias(i))
                            listaFinal = grafo.filtraSugerencias(user, lista, aux)

                            for i in listaFinal:
                                print(f'{contador}. {i}')
                                contador += 1

                        elif opc != "1" and opc != "2" and opc != "3":
                            print("-------¡Opción inválida!-------")
                        pause()

                    elif op == "3":
                        print("\n< -------Comentarios------- >")

                        print("\n1- Comentar\n2- Ver mis comentarios")
                        opc = input("Digite la opcion que desea: ")

                        if opc == "1":
                            comentario = input("\nEscriba el comentario que desea publicar: \n-> ")
                            user.addComment(user, comentario)
                            grafo.actualizarNodo(user)  # esto es para que se actualice dentro del grafo tambien, si no solo va a actualizar
                                                        # la persona que se crea dentro de la sesion
                        elif opc == "2":
                            user.showComments()

                        pause()
                    elif op == "4":
                        print(f"\n<<< Amigos de {user.nombre} >>>")

                        grafo.mostrarAmigos(user, '1')
                        pause()

                    elif op == "5":
                        print('\n------------------------------'
                              '\n---Publicaciones de amigos----'
                              '\n------------------------------\n')
                        lista = []
                        contador = 1
                        #aux = grafo.mostrarAmigos(user, '2')
                        grafo.mostrarAmigos(user, '3')
                        '''for i in lista:
                            print(f'{contador}. {i}')'''

                        pause()
                    elif op == "6":
                        print("\nCerrando sesión...")
                        pause()
                        session = False
                        grafo.actualizarNodo(user)
                    else:
                        print("¡Opción inválida!")

            else:
                print("¡Usuario inexistente! Volviendo a menú.")
                pause()

        elif opcion == "3":
            repeat = False
            print("\nCerrando programa...")
            pause()

        else:
            print("¡Opción inválida!\n")
            pause()
