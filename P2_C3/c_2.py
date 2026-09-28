# 2. Desarrolle en algún lenguaje de programación un sistema para una librería. La librería debe
#    agregar y buscar libros basados en su título. Para hacer la búsqueda más eficiente, haga uso del
#    código del ejercicio 1.

class Libreria:
    def __init__(self, nombre_de_libreria):
        self.nombre_L = nombre_de_libreria                                                   # Atributo1: str: Contiene el nombre de la libreria
        self.biblioteca = {100: 'celeste castillo', 101: "el principito", 102: "el universo"} # Atributo2: dict: Contiene la relacion {id: titulo}

    # Metodo 1: Busqueda nativa de Python usando .get()
    # Aprovecha la implementacion interna de tabla hash (hash table) de los diccionarios.
    # Complejidad temporal promedio: O(1). No requiere ordenar las claves previamente ni iterar.
    def buscar_libro_get(self, x):
        return self.biblioteca.get(x, f'No se encuentra ningún libro con el id entregado: {x}')

    # Metodo 2: Algoritmo de Busqueda Binaria manual
    # Para aplicar búsqueda binaria sobre un diccionario, primero se extraen y ordenan sus claves.
    # Complejidad temporal: O(log n) sobre las claves ordenadas.
    # En caso de no encontrar el id, retorna un mensaje descriptivo.
    def buscar_libros_binaria(self, x):
        claves = sorted(self.biblioteca.keys())  # Obtenemos las claves ordenadas para dividir el espacio de busqueda
        low = 0
        high = len(claves) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            if claves[mid] < x:
                low = mid + 1
            elif claves[mid] > x:
                high = mid - 1
            else:
                return self.biblioteca[claves[mid]]  # Retorna el titulo asociado al id encontrado

        return f'No se encuentra ningún libro en el id entregado: {x}'

    # Metodo 3: Agrega o actualiza un libro en la coleccion
    def agregar_libro(self, ID, libro):
        self.biblioteca[ID] = libro  # Insercion directa O(1) en el diccionario


# --- Pruebas del sistema ---
lib = Libreria('Libreria-9029')

# Agregar nuevos libros
lib.agregar_libro(103, "Cien años de soledad")
lib.agregar_libro(99, "Ficciones")

print("--- Búsqueda nativa (.get) ---")
print(lib.buscar_libro_get(101))  # 'el principito'
print(lib.buscar_libro_get(999))  # Mensaje no encontrado

print("\n--- Búsqueda manual (Binaria) ---")
print(lib.buscar_libros_binaria(99))   # 'Ficciones'
print(lib.buscar_libros_binaria(103))  # 'Cien años de soledad'
print(lib.buscar_libros_binaria(500))  # Mensaje no encontrado
