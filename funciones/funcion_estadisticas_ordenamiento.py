import os
from funciones.funcion_mostrar_filtrar import mostrar_y_filtrar_recursivo

BASE_DIR = "CONTINENTES"
# ==========================================
# Fase 5: Estadísticas y Ordenamiento Global
# ==========================================
def estadisticas_y_ordenamiento():
    if not os.path.exists(BASE_DIR):
        print("No existe la estructura de datos.")
        return
    registros = mostrar_y_filtrar_recursivo(BASE_DIR)
    if not registros:
        print("No hay datos registrados.")
        return
    # --- Ordenamiento ---
    print("Atributos disponibles: nombre, poblacion, superficie, continente, pais, provincia")
    attr1 = input("Ingrese primer atributo: ").strip().lower()
    attr2 = input("Ingrese segundo atributo (opcional): ").strip().lower()
    try:
        registros.sort(key=lambda x: (
            float(x.get(attr1, 0)) if str(x.get(attr1, "")).replace('.', '',1).isdigit() else str(x.get(attr1, "")),
            float(x.get(attr2, 0)) if attr2 and str(x.get(attr2, "")).replace('.', '',1).isdigit() else str(x.get(attr2, "")) if attr2 else ""
        ))
    except:
        print("No se pudo ordenar correctamente.")
    for i, r in enumerate(registros[:20], start=1):
        print(f"[{i}] {r.get('nombre', 'Sin nombre')} → {r.get('ruta')}")
    # --- Estadísticas ---
    suma_pob, suma_sup, cont_pob, cont_sup = 0,0,0,0
    for r in registros:
        try:
            if "poblacion" in r: 
                suma_pob += float(r["poblacion"]); cont_pob +=1
            if "superficie" in r:
                suma_sup += float(r["superficie"]); cont_sup +=1
        except: pass
    print(f"\nTotal ítems: {len(registros)}")
    print(f"Promedio población: {suma_pob/cont_pob:.2f}" if cont_pob else "👥 Promedio población: 0")
    print(f"Promedio superficie: {suma_sup/cont_sup:.2f}" if cont_sup else "🌍 Promedio superficie: 0")
