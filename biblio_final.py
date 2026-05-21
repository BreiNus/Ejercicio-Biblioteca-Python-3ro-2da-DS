biblioteca = []
usuarios = []
class Libro:

    def __init__(self, titulo, autor, isbn, ejemplares):
    
        self.titulo = titulo
        self.autor = autor
        self.isbn = str(isbn)
        
        try:
            self.ejemplares = int(ejemplares)

            if self.ejemplares < 0:
                print("Los ejemplares no pueden ser negativos.")
                self.ejemplares = 0

        except ValueError:
            print("La cantidad de ejemplares debe ser un número.")
            self.ejemplares = 0

        self.disponible = False
        self.prestado_a = []

    def registrar_libro(self):
        
        if self.titulo == "":
                print('El titulo no puede estar vacio')
                
        if self.autor == "":
                print('El autor no puede estar vacio')
                
        try:
            for libro in biblioteca:

                if libro.isbn == self.isbn:
                    print("Ya existe un libro con el mismo ISBN.")
                    print("NO SE PUDO REGISTRAR EL LIBRO")
                    return
        
            biblioteca.append(self)
            

        except Exception as e:
            print(f"Error al registrar libro: {e}")

    def verificar_disponible(self):
        return self.ejemplares >= 1

class Usuario:

    def __init__(self, nombre, usuario_id):

        self.nombre = nombre
        self.id = str(usuario_id)
    
    def registrar_usuario(self):

        try:

            if not self.nombre or not self.id:
                print("El nombre de usuario o Id no pueden estar vacío.")
                return

                

            for usuario in usuarios:

                if usuario.id == self.id:
                    print("Ya existe un usuario con el mismo ID.")
                    return
            usuarios.append(self)

            print("Usuario registrado correctamente!")

        except Exception as e:

            print(f"Error al registrar usuario: {e}")
    

class Sistema_biblioteca:

    def prestar_libro(isbn, usuario_id):

        try:
            isbn = str(isbn)
            usuario_id = str(usuario_id)

            libro = None
            usuario = None

            for l in biblioteca:

                if l.isbn == isbn:
                    libro = l
                    break

            if libro is None:
                print("ISBN no válido.")
                return

            if not libro.verificar_disponible():
                print("No hay más copias disponibles.")
                return

            for u in usuarios:

                if u.id == usuario_id:
                    usuario = u
                    break

            if usuario is None:
                print("Usuario no encontrado.")
                return

            libro.ejemplares -= 1
            libro.prestado_a.append(usuario)

            print(f"Libro prestado a {usuario.nombre}")

        except Exception as e:
            print(f"Error al prestar libro: {e}")

    def devolver_libro(isbn, usuario_id):

        try:
            for libro in biblioteca:

                if libro.isbn == str(isbn):

                    for usuario in libro.prestado_a:

                        if usuario.id == str(usuario_id):

                            libro.prestado_a.remove(usuario)
                            libro.ejemplares += 1

                            print(f"Libro devuelto por {usuario.nombre}")
                            return

                    print("Ese usuario no tiene este libro.")
                    return

            print("Libro no encontrado.")

        except Exception as e:
            print(f"Error al devolver libro: {e}")

    def consultar_libro(titulo):

        try:
            for l in biblioteca:

                if l.titulo.lower() == titulo.lower():

                    estado = (
                        "Disponible"
                        if l.ejemplares >= 1
                        else "No disponible"
                    )

                    if l.prestado_a:
                        usuario = ", ".join(
                            u.nombre for u in l.prestado_a
                        )

                    else:
                        usuario = "Nadie"

                    print("\n--- INFORMACIÓN DEL LIBRO ---")
                    print(f"Título: {l.titulo}")
                    print(f"Autor: {l.autor}")
                    print(f"ISBN: {l.isbn}")
                    print(f"Ejemplares: {l.ejemplares}")
                    print(f"Estado: {estado}")
                    print(f"Prestado a: {usuario}")

                    return

            print("Libro no encontrado.")

        except Exception as e:
            print(f"Error al consultar libro: {e}")

    def consultar_todos_los_libros():

        try:
            if not biblioteca:
                print("No hay libros registrados.")
                return

            print("\n--- LIBROS REGISTRADOS ---")

            for l in biblioteca:

                estado = (
                    "Disponible"
                    if l.ejemplares >= 1
                    else "No disponible"
                )

                if l.prestado_a:
                    usuario = ", ".join(
                        u.nombre for u in l.prestado_a
                    )

                else:
                    usuario = "Nadie"

                print("\n--------------------------")
                print(f"Título: {l.titulo}")
                print(f"Autor: {l.autor}")
                print(f"ISBN: {l.isbn}")
                print(f"Ejemplares: {l.ejemplares}")
                print(f"Estado: {estado}")
                print(f"Prestado a: {usuario}")

        except Exception as e:
            print(f"Error al consultar libros: {e}")

    def consultar_todos_los_usuarios():

        try:
            if not usuarios:
                print("No hay usuarios registrados.")
                return

            print("\n--- USUARIOS REGISTRADOS ---")

            for u in usuarios:

                libros_prestados = []

                for libro in biblioteca:

                    if u in libro.prestado_a:
                        libros_prestados.append(libro.titulo)

                print("\n--------------------------")
                print(f"Usuario: {u.nombre}")
                print(f"ID: {u.id}")

                if libros_prestados:

                    print("Libros prestados:")

                    for titulo in libros_prestados:
                        print(f"- {titulo}")

                else:
                    print("Sin libros prestados.")

        except Exception as e:
            print(f"Error al consultar usuarios: {e}")


def main():

    while True:

        try:
            print("================================")
            print("====== SISTEMA BIBLIOTECA ======")
            print("================================")
            print("1 - Agregar libro")
            print("2 - Agregar usuario")
            print("3 - Prestar libro")
            print("4 - Devolver libro")
            print("5 - Consultar libro")
            print("6 - Consultar todos los libros")
            print("7 - Consultar todos los usuarios")
            print("8 - Salir")

            opcion = input("\nIngrese su opción: ")

            if opcion == "1":

                titulo = input("Ingrese título: ")
                autor = input("Ingrese autor: ")
                isbn = input("Ingrese ISBN: ")
                ejemplares = input(
                    "Ingrese la cantidad de ejemplares: "
                )

                libro_nuevo = Libro(
                    titulo,
                    autor,
                    isbn,
                    ejemplares
                )

                libro_nuevo.registrar_libro()

            elif opcion == "2":

                nombre = input("Ingrese nombre: ")
                usuario_id = input("Ingrese ID: ")

                nuevo_usuario = Usuario(
                    nombre,
                    usuario_id
                )

                nuevo_usuario.registrar_usuario()

            elif opcion == "3":

                isbn = input("Ingrese ISBN: ")
                usuario_id = input(
                    "Ingrese ID de usuario: "
                )

                Sistema_biblioteca.prestar_libro(
                    isbn,
                    usuario_id
                )

            elif opcion == "4":

                isbn = input("Ingrese ISBN: ")
                usuario_id = input("Ingrese ID: ")

                Sistema_biblioteca.devolver_libro(
                    isbn,
                    usuario_id
                )

            elif opcion == "5":

                titulo = input(
                    "Ingrese el título del libro: "
                )

                Sistema_biblioteca.consultar_libro(
                    titulo
                )

            elif opcion == "6":

                Sistema_biblioteca.consultar_todos_los_libros()

            elif opcion == "7":

                Sistema_biblioteca.consultar_todos_los_usuarios()

            elif opcion == "8":

                print("Saliendo del sistema...")
                break

            else:
                print("Opción incorrecta.")

        except KeyboardInterrupt:

            print("\nPrograma interrumpido.")
            break

        except Exception as e:

            print(f"Error inesperado: {e}")


main()