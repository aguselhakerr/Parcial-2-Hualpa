import os
import csv

def crear_directorio(path):
    """Crea un directorio si no existe."""
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"Error creando directorio {path}: {e}")

def escribir_csv(ruta, datos, fieldnames):
    """Escribe datos en CSV (sobrescribe si ya existe)."""
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            if isinstance(datos, dict):
                writer.writerow(datos)
            elif isinstance(datos, list):
                writer.writerows(datos)
    except Exception as e:
        print(f"Error escribiendo archivo {ruta}: {e}")

def leer_csv(ruta):
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    try:
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            return [fila for fila in lector]
    except Exception as e:
        print(f"Error leyendo {ruta}: {e}")
        return []

def pedir_numero(mensaje):
    """Pide un número positivo (entero o flotante)."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo no puede estar vacío.")
            continue
        try:
            numero = float(valor)
            if numero <= 0:
                print("El valor debe ser mayor que cero.")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un número válido (entero o decimal).")

def pedir_texto(mensaje):
    """Pide un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo no puede estar vacío.")
        else:
            return valor.capitalize()
