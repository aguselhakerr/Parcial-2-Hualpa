import os
import csv

BASE_DIR = "CONTINENTES"

# Diccionarios con los datos requeridos
continentes = {
    #Primer elemento de la carpeta "CONTINENTES"
    "America": [
        {"nombre": "Argentina", "poblacion": 46250000, "superficie": 2780400, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 215313498, "superficie": 8515767, "continente": "America"}
    ],
    #Segundo elemento de la carpeta "CONTINENTES"
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


# Crear estructura de carpetas y archivos CSV con datos
def crear_directorio(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"Error creando directorio {path}: {e}")

def escribir_csv(ruta, datos, fieldnames):
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            if isinstance(datos, list):
                writer.writerows(datos)
            else:
                writer.writerow(datos)
    except Exception as e:
        print(f"Error escribiendo archivo {ruta}: {e}")
'''
def crear_estructura_completa():
    crear_directorio(BASE_DIR)
    for continente, paises in continentes.items():
        ruta_cont = os.path.join(BASE_DIR, continente)
        crear_directorio(ruta_cont)

        # Crear archivos CSV de países en nivel 2 (nombre del país)
        for pais in paises:
            nombre_pais = pais["nombre"]
            ruta_pais = os.path.join(ruta_cont, nombre_pais)
            crear_directorio(ruta_pais)

            archivo_pais_csv = os.path.join(ruta_cont, f"{nombre_pais}.csv")
            escribir_csv(archivo_pais_csv, pais, fieldnames=["nombre", "poblacion", "superficie", "continente"])

            # Crear carpetas y archivos CSV de ciudades (nivel 3)
            provincias = paises_provincias.get(nombre_pais, [])
            for provincia in provincias:
                nombre_provincia = provincia["nombre"]
                ruta_provincia = os.path.join(ruta_pais, nombre_provincia)
                crear_directorio(ruta_provincia)

                archivo_provincia_csv = os.path.join(ruta_pais, f"{nombre_provincia}.csv")
                escribir_csv(archivo_provincia_csv, provincia, fieldnames=["nombre", "poblacion", "superficie", "pais"])
                
                # Crear carpetas y archivos CSV para las ciudades dentro de la provincia
                ciudades = provincias_ciudades.get(nombre_provincia, [])
                for ciudad in ciudades:
                    nombre_ciudad = ciudad["nombre"]
                    ruta_ciudad = os.path.join(ruta_provincia, nombre_ciudad)
                    crear_directorio(ruta_ciudad)

                    archivo_ciudad_csv = os.path.join(ruta_ciudad, f"{nombre_ciudad}.csv")
                    escribir_csv(archivo_ciudad_csv, ciudad, fieldnames=["nombre", "poblacion", "superficie", "provincia"])
'''


'''
def crear_nivel_recursivo(ruta_base, nodo, nombre_clave, hijos_clave, fieldnames):
    """
    Crea directorio y archivo CSV para el nodo actual,
    luego llama recursivamente para cada hijo.

    :param ruta_base: ruta del directorio donde crear la carpeta del nodo
    :param nodo: dict con datos actuales
    :param nombre_clave: clave para nombre del nodo, p.ej. "nombre"
    :param hijos_clave: clave para lista de hijos en nodo, p.ej. "hijos"
    :param fieldnames: lista de campos para el CSV
    """
    nombre_nodo = nodo[nombre_clave]
    ruta_actual = os.path.join(ruta_base, nombre_nodo)
    crear_directorio(ruta_actual)

    # Crear archivo CSV con datos del nodo (sin los hijos)
    datos_sin_hijos = dict(nodo)
    datos_sin_hijos.pop(hijos_clave, None)  # eliminar la lista hijos para no guardar en csv
    archivo_csv = os.path.join(ruta_actual, f"{nombre_nodo}.csv")
    escribir_csv(archivo_csv, datos_sin_hijos, fieldnames)

    # Procesar recursivamente los hijos si existen
    hijos = nodo.get(hijos_clave, [])
    for hijo in hijos:
        crear_nivel_recursivo(ruta_actual, hijo, nombre_clave, hijos_clave, fieldnames)
'''
# Adaptación para tu estructura:

# Crear diccionario con jerarquía anidada
estructura = {
    "nombre": "CONTINENTES",
    "hijos": [
        {
            **{"nombre": "America"},
            "hijos": [
                {
                    **pais,
                    "hijos": paises_provincias.get(pais["nombre"], [])
                }
                for pais in continentes["America"]
            ]
        },
        {
            **{"nombre": "Europa"},
            "hijos": [
                {
                    **pais,
                    "hijos": paises_provincias.get(pais["nombre"], [])
                }
                for pais in continentes["Europa"]
            ]
        }
    ]
}






def crear_nivel_recursivo(ruta_base, nodo, nombre_clave, hijos_clave, fieldnames, es_raiz=False):
    nombre_nodo = nodo[nombre_clave]
    if not es_raiz:
        ruta_actual = os.path.join(ruta_base, nombre_nodo)
        crear_directorio(ruta_actual)
    else:
        ruta_actual = ruta_base  # no crear carpeta con nombre raíz, usar la base existente

    hijos = nodo.get(hijos_clave, [])
    # Crear archivo CSV en carpeta padre salvo si es nodo raíz
    if not es_raiz:
        # Si tiene hijos, crear CSV en carpeta padre
        if hijos:
            archivo_csv = os.path.join(ruta_base, f"{nombre_nodo}.csv")
            datos_sin_hijos = dict(nodo)
            datos_sin_hijos.pop(hijos_clave, None)
            escribir_csv(archivo_csv, datos_sin_hijos, fieldnames)
        else:
            # Nodo hoja, crear CSV dentro de su carpeta
            archivo_csv = os.path.join(ruta_actual, f"{nombre_nodo}.csv")
            escribir_csv(archivo_csv, nodo, fieldnames)

    # Recursividad para hijos
    for hijo in hijos:
        crear_nivel_recursivo(ruta_actual, hijo, nombre_clave, hijos_clave, fieldnames, es_raiz=False)



# Luego, creas la estructura
if __name__ == "__main__":
    #llamada inicial
    crear_directorio(BASE_DIR)
    crear_nivel_recursivo(BASE_DIR, estructura, "nombre", "hijos", ["nombre", "poblacion", "superficie", "continente", "pais", "provincia"], es_raiz=True)


def menu():
    print("\n"+"-"*13+"Menu"+"-"*13)
    print("1) Añadir un país")
    print("2) Añadir una provincia")
    print("2) Añadir una ciudad")
    print("• Seleccione cualquier otro número para salir")

if __name__ == "__main__":
    print("\nEstructura creada con éxito.")
    while True:
        try:
            # crear_estructura_completa()
            menu()
            seleccion = int(input("Ingrese una opción: "))
            match seleccion:
                case 1:
                    print("1")
                case 2:
                    print("2")
                case 3:
                    print("3")
                case _:
                    print("Saliendo...")
                    break
        except ValueError:
            print("Incorrecto. Porfavor, solo ingrese numeros!!")