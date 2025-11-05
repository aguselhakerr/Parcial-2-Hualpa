import os
import csv
from typing import List, Dict, Any

# Configuración de la estructura jerárquica
BASE_DIR = "data"
LEVEL_1 = "nivel1"
LEVEL_2 = "nivel2"
LEVEL_3 = "nivel3"

# Función para crear la estructura jerárquica
def crear_estructura():
    """Crea la estructura de carpetas de tres niveles."""
    try:
        os.makedirs(os.path.join(BASE_DIR, LEVEL_1, LEVEL_2, LEVEL_3), exist_ok=True)
        print(f"Estructura creada en: {BASE_DIR}")
    except Exception as e:
        print(f"Error al crear la estructura: {e}")

# Función recursiva para recorrer carpetas y consolidar datos CSV
def recorrer_y_consolidar(ruta: str, datos: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Recorre recursivamente la estructura y consolida todos los datos CSV en una lista."""
    if datos is None:
        datos = []
    try:
        for nombre_directorio, dirs, ficheros in os.walk(ruta):
            for fichero in ficheros:
                if fichero.endswith(".csv"):
                    ruta_completa = os.path.join(nombre_directorio, fichero)
                    try:
                        with open(ruta_completa, newline='', encoding='utf-8') as csvfile:
                            reader = csv.DictReader(csvfile)
                            for row in reader:
                                datos.append(row)
                    except Exception as e:
                        print(f"Error al leer {ruta_completa}: {e}")
    except Exception as e:
        print(f"Error al recorrer la ruta {ruta}: {e}")
    return datos

# Alta: Crear nuevo ítem (carpeta y archivo CSV)
def alta_item(nombre: str, datos: Dict[str, Any]):
    """Crea una nueva carpeta y archivo CSV en la estructura jerárquica."""
    try:
        ruta = os.path.join(BASE_DIR, LEVEL_1, LEVEL_2, LEVEL_3, f"{nombre}.csv")
        with open(ruta, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=datos.keys())
            writer.writeheader()
            writer.writerow(datos)
        print(f"Ítem '{nombre}' creado exitosamente.")
    except Exception as e:
        print(f"Error al crear ítem: {e}")

# Lectura global: Consolidar todos los datos CSV
def lectura_global():
    """Devuelve todos los datos consolidados de la estructura jerárquica."""
    return recorrer_y_consolidar(BASE_DIR)

# Modificación: Actualizar un ítem existente
def modificar_item(nombre: str, nuevos_datos: Dict[str, Any]):
    """Modifica los datos de un ítem existente."""
    ruta = os.path.join(BASE_DIR, LEVEL_1, LEVEL_2, LEVEL_3, f"{nombre}.csv")
    if os.path.exists(ruta):
        try:
            with open(ruta, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=nuevos_datos.keys())
                writer.writeheader()
                writer.writerow(nuevos_datos)
            print(f"Ítem '{nombre}' modificado exitosamente.")
        except Exception as e:
            print(f"Error al modificar ítem: {e}")
    else:
        print(f"Ítem '{nombre}' no encontrado.")

# Eliminación: Borrar un ítem
def eliminar_item(nombre: str):
    """Elimina un ítem (archivo CSV) de la estructura."""
    ruta = os.path.join(BASE_DIR, LEVEL_1, LEVEL_2, LEVEL_3, f"{nombre}.csv")
    if os.path.exists(ruta):
        try:
            os.remove(ruta)
            print(f"Ítem '{nombre}' eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar ítem: {e}")
    else:
        print(f"Ítem '{nombre}' no encontrado.")

# Ordenamiento: Ordenar datos por una clave
def ordenar_datos(datos: List[Dict[str, Any]], clave: str) -> List[Dict[str, Any]]:
    """Ordena los datos por una clave específica."""
    try:
        return sorted(datos, key=lambda x: x.get(clave, ""))
    except Exception as e:
        print(f"Error al ordenar datos: {e}")
        return datos

# Estadísticas: Calcular estadísticas básicas
def estadisticas(datos: List[Dict[str, Any]], clave: str) -> Dict[str, Any]:
    """Calcula estadísticas básicas sobre una clave numérica."""
    try:
        valores = [float(d[clave]) for d in datos if d.get(clave, "").replace('.', '', 1).isdigit()]
        if valores:
            return {
                "total": len(valores),
                "promedio": sum(valores) / len(valores),
                "minimo": min(valores),
                "maximo": max(valores)
            }
        else:
            return {"total": 0, "promedio": 0, "minimo": 0, "maximo": 0}
    except Exception as e:
        print(f"Error al calcular estadísticas: {e}")
        return {"total": 0, "promedio": 0, "minimo": 0, "maximo": 0}

# Ejemplo de uso
if __name__ == "__main__":
    crear_estructura()
    alta_item("producto1", {"ID": "1", "Nombre": "Producto A", "Precio": "100", "Stock": "50"})
    alta_item("producto2", {"ID": "2", "Nombre": "Producto B", "Precio": "200", "Stock": "30"})
    datos = lectura_global()
    print("Datos consolidados:", datos)
    modificar_item("producto1", {"ID": "1", "Nombre": "Producto A Modificado", "Precio": "150", "Stock": "40"})
    datos = lectura_global()
    print("Datos después de modificar:", datos)
    opcion = int(input("\nIngrese un producto a borrar: "))
    match opcion:
        ### ValueError
        case 1:
            eliminar_item("producto1")
        case 2:
            eliminar_item("producto2")
    datos = lectura_global()
    print("Datos después de eliminar:", datos)
    datos_ordenados = ordenar_datos(datos, "Precio")
    print("Datos ordenados por precio:", datos_ordenados)
    estadisticas_precio = estadisticas(datos, "Precio")
    print("Estadísticas de precios:", estadisticas_precio)
