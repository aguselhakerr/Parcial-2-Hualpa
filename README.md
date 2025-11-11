# INTEGRANTES


1PRO4:

→ Facundo Chacón

→ Agustín Mora

#RESUMEN

Es un programa que trabaja con recursividad, cuyas funciones se encargan de crear carpetas, y creando, abriendo, modificando y eliminando archivos .csv, según lo que el input del usuario.

# EXPLICACION DETALLADA

El menú se divide en 5 funciones principales: creacion_jerarquica, mostrar_y_filtrar_recursivo, modificar_item, elimnar_item y estadística_y_ordenamiento

En caso de no elegir ninguna opción de las anteriores se sale del programa.
Si no se ingresa un número retorna ValueError, por lo que entra al try/except y le indica al usuario que no ingresó una opción correcta.

1) La funcion_jerarquica: Se encarga de crear carpetas con sus respectivos archivos csv, a los cuales el usuario les puede ingresar los datos correspondientes.

2) mostrar_y_filtrar_recursivo: Se encarga de revisar las rutas de los archivos, y permite un input del usarario con el cual se busca el elemento deseado

3) modificar_item_recursivo: Lee la ruta de los archivos, permite el input del usuario y modifica un archivo deseado, según lo que ingrese

4) eliminar_item_recursivo: Similar al anterior, lee la ruta de los archivos y permite el input del usuario para eliminar el archivo deseado

5) estadisticas_y_ordenamiento: Lee la ruta de los archivos, permitiendo el input del usuario, con el cual filtra según lo que ingrese el usuario. Suma el valor de los números indicados en el filtro que ingresó el usuario, y los divide por la cantidad archivos csv que lee.






# VIDEO EXPLICATIVO

[https://youtu.be/GFMc6vA5L7Q](https://youtu.be/7Vp_dtsLnEw?si=oC_kq7p-BIryjsg7)
