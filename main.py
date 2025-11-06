import os
import csv
from funciones.funcion_creacion_jerarquica import *
from funciones.funcion_mostrar_filtrar import mostrar_y_filtrar
from funciones.funcion_modificar_item import modificar_item
from funciones.funcion_eliminar_item import eliminar_item
from funciones.funcion_estadisticas_ordenamiento import estadisticas_y_ordenamiento
from utilidades.funciones_utiles import crear_directorio


# Datos iniciales
continentes = {
    "America": [
        {"nombre": "Argentina", "poblacion": 46250000, "superficie": 2780400, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 215313498, "superficie": 8515767, "continente": "America"}
    ],
    "Europa": [
        {"nombre": "España", "poblacion": 47450795, "superficie": 505990, "continente": "Europa"},
        {"nombre": "Francia", "poblacion": 65273511, "superficie": 643801, "continente": "Europa"}
    ]
}

paises_provincias = {
    "Argentina": [
        {"nombre": "BuenosAires", "poblacion": 17523996, "superficie": 307571, "pais": "Argentina"},
        {"nombre": "Cordoba", "poblacion": 3840905, "superficie": 165321, "pais": "Argentina"}
    ],
    "Brasil": [
        {"nombre": "Rio", "poblacion": 6748000, "superficie": 12500, "pais": "Brasil"},
        {"nombre": "SaoPaulo", "poblacion": 12300000, "superficie": 15210, "pais": "Brasil"}
    ],
    "España": [
        {"nombre": "Barcelona", "poblacion": 5585550, "superficie": 10190, "pais": "España"},
        {"nombre": "Madrid", "poblacion": 6661949, "superficie": 604, "pais": "España"}
    ],
    "Francia": [
        {"nombre": "Lyon", "poblacion": 515695, "superficie": 475, "pais": "Francia"},
        {"nombre": "Paris", "poblacion": 2148000, "superficie": 105, "pais": "Francia"}
    ]
}

provincias_ciudades = {
    "BuenosAires": [
        {"nombre": "Mar del Plata", "poblacion": 682605, "superficie": 398, "provincia": "BuenosAires"},
        {"nombre": "La Plata", "poblacion": 750000, "superficie": 940, "provincia": "BuenosAires"},
        {"nombre": "Bahía Blanca", "poblacion": 301572, "superficie": 262, "provincia": "BuenosAires"},
        {"nombre": "Tandil", "poblacion": 123733, "superficie": 52, "provincia": "BuenosAires"},
        {"nombre": "Olavarría", "poblacion": 111320, "superficie": 423, "provincia": "BuenosAires"}
    ],
    "Cordoba": [
        {"nombre": "Villa Carlos Paz", "poblacion": 75515, "superficie": 16, "provincia": "Cordoba"},
        {"nombre": "Río Cuarto", "poblacion": 157298, "superficie": 422, "provincia": "Cordoba"},
        {"nombre": "Villa María", "poblacion": 80239, "superficie": 28, "provincia": "Cordoba"},
        {"nombre": "Cruz del Eje", "poblacion": 38337, "superficie": 14, "provincia": "Cordoba"},
        {"nombre": "Alta Gracia", "poblacion": 48625, "superficie": 15, "provincia": "Cordoba"}
    ],
    "Rio": [
        {"nombre": "Niterói", "poblacion": 487320, "superficie": 133, "provincia": "Rio"},
        {"nombre": "Nova Iguaçu", "poblacion": 800000, "superficie": 520, "provincia": "Rio"},
        {"nombre": "Duque de Caxias", "poblacion": 900000, "superficie": 464, "provincia": "Rio"},
        {"nombre": "São Gonçalo", "poblacion": 1000000, "superficie": 250, "provincia": "Rio"},
        {"nombre": "Petrópolis", "poblacion": 300000, "superficie": 800, "provincia": "Rio"}
    ],
    "SaoPaulo": [
        {"nombre": "Campinas", "poblacion": 1214000, "superficie": 795, "provincia": "SaoPaulo"},
        {"nombre": "Santos", "poblacion": 433000, "superficie": 280, "provincia": "SaoPaulo"},
        {"nombre": "São Bernardo do Campo", "poblacion": 830000, "superficie": 405, "provincia": "SaoPaulo"},
        {"nombre": "Guarulhos", "poblacion": 1370000, "superficie": 317, "provincia": "SaoPaulo"},
        {"nombre": "Osasco", "poblacion": 700000, "superficie": 65, "provincia": "SaoPaulo"}
    ],
    "Barcelona": [
        {"nombre": "Hospitalet de Llobregat", "poblacion": 260000, "superficie": 12, "provincia": "Barcelona"},
        {"nombre": "Badalona", "poblacion": 220000, "superficie": 21, "provincia": "Barcelona"},
        {"nombre": "Sabadell", "poblacion": 210000, "superficie": 38, "provincia": "Barcelona"},
        {"nombre": "Terrassa", "poblacion": 210000, "superficie": 70, "provincia": "Barcelona"},
        {"nombre": "Mataró", "poblacion": 130000, "superficie": 22, "provincia": "Barcelona"}
    ],
    "Madrid": [
        {"nombre": "Alcalá de Henares", "poblacion": 196000, "superficie": 87, "provincia": "Madrid"},
        {"nombre": "Getafe", "poblacion": 180000, "superficie": 78, "provincia": "Madrid"},
        {"nombre": "Leganés", "poblacion": 188000, "superficie": 43, "provincia": "Madrid"},
        {"nombre": "Móstoles", "poblacion": 210000, "superficie": 48, "provincia": "Madrid"},
        {"nombre": "Fuenlabrada", "poblacion": 193000, "superficie": 39, "provincia": "Madrid"}
    ],
    "Lyon": [
        {"nombre": "Villeurbanne", "poblacion": 148000, "superficie": 14, "provincia": "Lyon"},
        {"nombre": "Vénissieux", "poblacion": 65000, "superficie": 16, "provincia": "Lyon"},
        {"nombre": "Saint-Priest", "poblacion": 47000, "superficie": 29, "provincia": "Lyon"},
        {"nombre": "Caluire-et-Cuire", "poblacion": 42000, "superficie": 10, "provincia": "Lyon"},
        {"nombre": "Bron", "poblacion": 42000, "superficie": 10, "provincia": "Lyon"}
    ],
    "Paris": [
        {"nombre": "Boulogne-Billancourt", "poblacion": 120000, "superficie": 6, "provincia": "Paris"},
        {"nombre": "Saint-Denis", "poblacion": 112000, "superficie": 12, "provincia": "Paris"},
        {"nombre": "Argenteuil", "poblacion": 108000, "superficie": 17, "provincia": "Paris"},
        {"nombre": "Montreuil", "poblacion": 105000, "superficie": 8, "provincia": "Paris"},
        {"nombre": "Nanterre", "poblacion": 95000, "superficie": 12, "provincia": "Paris"}
    ]
}


estructura = {
    "nombre": "CONTINENTES",
    "hijos": [
        {
            "nombre": "America",
            "hijos": [
                {
                    **pais,
                    "hijos": [
                        {
                            **provincia,
                            "hijos": provincias_ciudades.get(provincia["nombre"], [])
                        }
                        for provincia in paises_provincias.get(pais["nombre"], [])
                    ]
                }
                for pais in continentes["America"]
            ]
        },
        {
            "nombre": "Europa",
            "hijos": [
                {
                    **pais,
                    "hijos": [
                        {
                            **provincia,
                            "hijos": provincias_ciudades.get(provincia["nombre"], [])
                        }
                        for provincia in paises_provincias.get(pais["nombre"], [])
                    ]
                }
                for pais in continentes["Europa"]
            ]
        }
    ]
}

def crear_nivel_recursivo(ruta_base, nodo, nombre_clave, hijos_clave, fieldnames, es_raiz=False):
    nombre_nodo = nodo[nombre_clave]

    datos_sin_hijos = dict(nodo)
    datos_sin_hijos.pop(hijos_clave, None)

    es_ciudad = "provincia" in datos_sin_hijos and "pais" not in datos_sin_hijos
    es_provincia = "pais" in datos_sin_hijos and "provincia" not in datos_sin_hijos
    es_pais = "continente" in datos_sin_hijos
    es_continente = es_raiz or ("hijos" in nodo and not es_pais and not es_provincia and not es_ciudad)

    if es_raiz:
        ruta_actual = ruta_base
    elif es_continente:
        ruta_actual = os.path.join(ruta_base, nombre_nodo)
        crear_directorio(ruta_actual)
        archivo_csv = os.path.join(ruta_base, f"{nombre_nodo}.csv")

        # Datos reales para continentes
        if nombre_nodo == "America":
            poblacion_real = 1010000000
            superficie_real = 42000000
            cant_paises_real = 35
        elif nombre_nodo == "Europa":
            poblacion_real = 747000000
            superficie_real = 10000000
            cant_paises_real = 44
        else:
            poblacion_real = datos_sin_hijos.get("poblacion", "")
            superficie_real = datos_sin_hijos.get("superficie", "")
            cant_paises_real = len(nodo.get(hijos_clave, []))

        datos_csv = {
            "nombre": nombre_nodo,
            "poblacion": poblacion_real,
            "superficie": superficie_real,
            "cant_paises": cant_paises_real
        }
        campos = ["nombre", "poblacion", "superficie", "cant_paises"]
        escribir_csv(archivo_csv, datos_csv, campos)

    elif es_pais:
        ruta_actual = os.path.join(ruta_base, nombre_nodo)
        crear_directorio(ruta_actual)
        archivo_csv = os.path.join(ruta_base, f"{nombre_nodo}.csv")
        campos = ["nombre", "poblacion", "superficie", "continente"]
        datos_csv = datos_sin_hijos
        escribir_csv(archivo_csv, datos_csv, campos)

    elif es_provincia:
        ruta_actual = os.path.join(ruta_base, nombre_nodo)
        crear_directorio(ruta_actual)
        archivo_csv = os.path.join(ruta_base, f"{nombre_nodo}.csv")
        campos = ["nombre", "poblacion", "superficie", "pais"]
        datos_csv = datos_sin_hijos
        escribir_csv(archivo_csv, datos_csv, campos)

    elif es_ciudad:
        ruta_actual = ruta_base
        archivo_csv = os.path.join(ruta_actual, f"{nombre_nodo}.csv")
        campos = ["nombre", "poblacion", "superficie", "provincia"]
        datos_csv = datos_sin_hijos
        escribir_csv(archivo_csv, datos_csv, campos)

    else:
        ruta_actual = os.path.join(ruta_base, nombre_nodo)
        crear_directorio(ruta_actual)
        archivo_csv = os.path.join(ruta_actual, f"{nombre_nodo}.csv")
        escribir_csv(archivo_csv, datos_sin_hijos, fieldnames)

    hijos = nodo.get(hijos_clave, [])
    for hijo in hijos:
        crear_nivel_recursivo(ruta_actual, hijo, nombre_clave, hijos_clave, fieldnames, es_raiz=False)

# Función recursiva para buscar nodo y devolver nodo + ruta de nombres desde raíz
def find_node_with_path(nodo, nombre_clave, buscado, path=None):
    if path is None:
        path = []
    current_name = nodo.get(nombre_clave)
    new_path = path + [current_name]
    if current_name == buscado:
        return nodo, new_path
    for hijo in nodo.get("hijos", []):
        res = find_node_with_path(hijo, nombre_clave, buscado, new_path)
        if res is not None:
            return res
    return None

# Operaciones de añadir (usando recursividad para localizar y actualizar la estructura)
def agregar_pais():
    continente = input("Nombre del continente (ej. America, Europa): ").strip()
    if not continente:
        print("Continente no puede estar vacío.")
        return

    pais = input("Nombre del país (Región): ").strip()
    if not pais:
        print("País no puede estar vacío.")
        return

    provincia = input("Nombre de la provincia (División): ").strip()
    if not provincia:
        print("Provincia no puede estar vacía.")
        return

    # Atributos de la provincia
    try:
        poblacion = float(input("Población de la provincia: ").strip())
        superficie = float(input("Superficie de la provincia: ").strip())
        if poblacion <= 0 or superficie <= 0:
            print("Población y superficie deben ser mayores a cero.")
            return
    except ValueError:
        print("Población y superficie deben ser números válidos.")
        return

    # Crear carpetas
    ruta_continente = os.path.join(BASE_DIR, continente)
    ruta_pais = os.path.join(ruta_continente, pais)
    ruta_provincia = os.path.join(ruta_pais, provincia)

    for ruta in [ruta_continente, ruta_pais, ruta_provincia]:
        crear_directorio(ruta)

    # Agregar registro a CSV de provincia (modo append, crea si no existe)
    archivo_provincia_csv = os.path.join(ruta_pais, f"{provincia}.csv")
    campos_provincia = ["nombre", "poblacion", "superficie", "pais"]
    fila_provincia = {"nombre": provincia, "poblacion": poblacion, "superficie": superficie, "pais": pais}

    file_exists = os.path.isfile(archivo_provincia_csv)
    with open(archivo_provincia_csv, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos_provincia)
        if not file_exists:
            writer.writeheader()
        writer.writerow(fila_provincia)
    print(f"Provincia '{provincia}' agregada a archivo {archivo_provincia_csv}.")

    # Añadir ciudades dinámicamente
    while True:
        add_ciudad = input("¿Desea agregar una ciudad en esta provincia? (s/n): ").strip().lower()
        if add_ciudad != 's':
            break

        nombre_ciudad = input("Nombre de la ciudad: ").strip()
        if not nombre_ciudad:
            print("Nombre de ciudad no puede estar vacío.")
            continue

        try:
            poblacion_c = float(input("Población de la ciudad: ").strip())
            superficie_c = float(input("Superficie de la ciudad: ").strip())
            if poblacion_c <= 0 or superficie_c <= 0:
                print("Población y superficie deben ser mayores a cero.")
                continue
        except ValueError:
            print("Población y superficie deben ser números válidos.")
            continue

        campo_ciudad = ["nombre", "poblacion", "superficie", "provincia"]
        fila_ciudad = {"nombre": nombre_ciudad, "poblacion": poblacion_c, "superficie": superficie_c, "provincia": provincia}

        archivo_ciudad_csv = os.path.join(ruta_provincia, f"{nombre_ciudad}.csv")
        with open(archivo_ciudad_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campo_ciudad)
            writer.writeheader()
            writer.writerow(fila_ciudad)
        print(f"Ciudad '{nombre_ciudad}' agregada en archivo {archivo_ciudad_csv}.")

def agregar_provincia():
    pais = input("Nombre del país donde añadir la provincia: ").strip()
    # buscar país en estructura recursivamente
    res = find_node_with_path(estructura, "nombre", pais)
    if res is None:
        print("País no encontrado.")
        return
    pais_node, path = res
    try:
        poblacion = int(input("Población de la provincia: ").strip())
        superficie = int(input("Superficie de la provincia: ").strip())
    except ValueError:
        print("Población y superficie deben ser números enteros.")
        return
    nombre = input("Nombre de la provincia: ").strip()
    provincia_dict = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "pais": pais, "hijos": []}
    pais_node.setdefault("hijos", []).append(provincia_dict)

    # actualizar dict de paises_provincias
    paises_provincias.setdefault(pais, []).append({k: provincia_dict[k] for k in ["nombre", "poblacion", "superficie", "pais"]})

    # ruta en disco: BASE_DIR/continente/pais/provincia
    # path tiene ['CONTINENTES', 'Continente', 'Pais']
    if len(path) >= 3:
        continente = path[1]
        pais_nombre = path[2]
        ruta_pais = os.path.join(BASE_DIR, continente, pais_nombre)
        crear_directorio(ruta_pais)
        ruta_provicia_dir = os.path.join(ruta_pais, nombre)
        crear_directorio(ruta_provicia_dir)
        archivo_prov_csv = os.path.join(ruta_pais, f"{nombre}.csv")
        escribir_csv(archivo_prov_csv, provincia_dict, fieldnames=["nombre", "poblacion", "superficie", "pais"])
        print(f"Provincia '{nombre}' agregada en país '{pais_nombre}'.")
    else:
        print("Error determinando ruta en disco para la provincia.")

def agregar_ciudad():
    provincia = input("Nombre de la provincia donde añadir la ciudad: ").strip()
    res = find_node_with_path(estructura, "nombre", provincia)
    if res is None:
        print("Provincia no encontrada.")
        return
    provincia_node, path = res
    try:
        poblacion = int(input("Población de la ciudad: ").strip())
        superficie = int(input("Superficie de la ciudad: ").strip())
    except ValueError:
        print("Población y superficie deben ser números enteros.")
        return
    nombre = input("Nombre de la ciudad: ").strip()
    ciudad_dict = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "provincia": provincia}
    provincia_node.setdefault("hijos", []).append(ciudad_dict)

    # actualizar provincias_ciudades
    provincias_ciudades.setdefault(provincia, []).append(ciudad_dict)

    # ruta disco: BASE_DIR/continente/pais/provincia/ciudad
    # path ejemplo: ['CONTINENTES','America','Argentina','BuenosAires']
    if len(path) >= 4:
        continente = path[1]
        pais = path[2]
        prov = path[3]
        ruta_provincia = os.path.join(BASE_DIR, continente, pais, prov)
        archivo_ciudad_csv = os.path.join(ruta_provincia, f"{nombre}.csv")

        escribir_csv(archivo_ciudad_csv, ciudad_dict, fieldnames=["nombre", "poblacion", "superficie", "provincia"])
        print(f"Ciudad '{nombre}' agregada en provincia '{prov}'.")
    else:
        print("Error determinando ruta en disco para la ciudad.")



# ===============================
# Menú
# ===============================
menu = True
while menu:
    crear_directorio(BASE_DIR)
    crear_nivel_recursivo(BASE_DIR, estructura, "nombre", "hijos",["nombre", "poblacion", "superficie", "continente", "pais", "provincia"],es_raiz=True)
    print("\n" + "-"*13 + " Menu " + "-"*13)
    print("1) Crear estructura jerárquica con datos")
    print("2) Mostrar ítems totales y filtrado (lectura global)")
    print("3) Modificar un ítem existente (Update)")
    print("4) Eliminar un ítem existente (Delete)")
    print("5) Estadísticas y ordenamiento global")
    
    print("• Cualquier otro número para salir")
    try:
        seleccion = int(input("Ingrese una opción: ").strip())
        match seleccion:
            case 1:
                crear_nivel(BASE_DIR, 1)
                # agregar_pais()
            case 2:
                mostrar_y_filtrar()
            case 3:
                modificar_item()
            case 4:
                eliminar_item()
            case 5:
                estadisticas_y_ordenamiento()
            case _:
                print("Saliendo del menú...")
                menu = False
    except ValueError:
        print("Incorrecto. Por favor, solo ingrese números.")


# Construcción de estructura anidada para operaciones recursivas

# Utilidades de FS y CSV


# Reuso de función recursiva para crear estructura en disco desde nodo raíz

