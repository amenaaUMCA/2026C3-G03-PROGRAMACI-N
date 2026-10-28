"""Reto integrador: control de ingreso al Anfiteatro del CENAC.

Nombre del estudiante: __________________________________________
Fecha: ____________________

Contexto:
Se analizará el ingreso de grupos a un evento en el Anfiteatro del CENAC, Costa Rica.
Para este ejercicio, use 700 como capacidad del escenario didáctico; no lo presente
como aforo operativo vigente. La ficha de SiCultura indica 700 y las condiciones
del MCJ publicadas en 2023 indican 500, por lo que las fuentes difieren.
SiCultura: https://si.cultura.cr/es/infraestructura/anfiteatro-del-centro-nacional-de-cultura
MCJ (condiciones de uso 2023): https://www.mcj.go.cr/sites/default/files/2023-07/Condiciones%20de%20uso%20de%20las%20instalaciones%20del%20CENAC%202023.pdf

Antes de programar, analice estos casos y complete una traza con ocupación anterior,
decisión y ocupación posterior:
- 650, 60, 50, fin -> acepta 650, rechaza 60, acepta 50; total 700.
- 400, 300, fin -> acepta ambos grupos; total 700.
- 701, fin -> rechaza el grupo; total 0.
- fin -> no hay grupos; total 0.

Traza esperada para 650, 60, 50:
Grupo | Ocupación anterior | Decisión  | Ocupación posterior
650   | 0                  | aceptado  | 650
60    | 650                | rechazado | 650
50    | 650                | aceptado  | 700

Preguntas de análisis:
- ¿Por qué no se conoce cuántas veces se solicitará un grupo?
- ¿Qué lista cambia cuando el grupo se acepta? ¿Y cuando se rechaza?
- ¿Qué no debe cambiar después de un rechazo?
- ¿Qué información puede calcularse al finalizar recorriendo los aceptados?

Objetivo:
Registrar los grupos y evitar que la ocupación supere la capacidad del escenario.

Reglas:
- Cada entrada es un grupo completo. No se permite entrada parcial.
- Escriba "fin" para terminar.
- Acepte solo enteros mayores que cero.
- Si ocupación actual + grupo <= 700, acepte el grupo.
- Si ocupación actual + grupo > 700, rechace el grupo.
- Las entradas inválidas se informan, pero no se cuentan como grupos rechazados por aforo.

Requisitos esenciales:
- Use una lista para grupos aceptados y otra para grupos rechazados.
- Use while para recibir grupos hasta la palabra fin.
- Use append() para guardar el grupo en la lista correspondiente.
- Use condicionales y try-except para decidir y validar cada entrada.
- Use for para calcular el total admitido recorriendo los grupos aceptados.
- Mantenga la ocupación dentro de la capacidad del escenario.
- Muestre ocupación y espacios disponibles después de cada grupo válido.
- Al finalizar, muestre grupos aceptados, grupos rechazados, total admitido
  y espacios disponibles.

Extensiones si hay tiempo:
- Calcule el porcentaje de ocupación.
- Encuentre el grupo aceptado más pequeño y el más grande.
- Clasifique el estado final del recinto.

No use menú, while True, funciones propias, CSV, listas anidadas ni
comprensiones de listas.

Después de cada grupo válido, muestre:
- Mensaje de aceptación o rechazo.
- Ocupación actual.
- Espacios disponibles.

El porcentaje, los extremos de los grupos y el estado final son extensiones;
no son necesarios para completar el objetivo esencial de esta práctica.

Ejemplo de salida completa (incluye indicadores que son extensión):
Entradas: 650, 60, 50, fin

Grupo aceptado: ingresan 650 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo rechazado: no hay espacio para 60 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo aceptado: ingresan 50 personas.
Ocupación actual: 700
Espacios disponibles: 0

REPORTE FINAL
Grupos aceptados: 2
Grupos rechazados: 1
Personas admitidas: 700
Capacidad máxima: 700
Espacios disponibles: 0
Porcentaje de ocupación: 100.00%
Grupo aceptado más pequeño: 50
Grupo aceptado más grande: 650
Estado final: capacidad completa.

Otros casos para probar:
- Entradas 100, 200, 150, fin -> 450 personas, estado normal.
- Entrada 701, fin -> grupo rechazado, 0 personas admitidas.
- Entrada fin -> reporte sin grupos aceptados.
- Texto, 0 o negativos -> entrada inválida y el programa continúa.
"""


# Desarrolle su solución a partir de esta línea.
CAPACIDAD_MAXIMA = 700
#Listas control
grupos_aceptados = []
grupos_rechazados = []
ocupacion_actual = 0 
espacio_disponilbles = CAPACIDAD_MAXIMA - ocupacion_actual

#
print("CONTROL DE INGRESO - ANFITEATRO DEL CENAC")
print(f"Capacidad del ecenario: {CAPACIDAD_MAXIMA} personas")
print("Escriba 'fin' para cerrar el ingreso.")

#entradas
entrada = input("Ingrese la cantidad de personas del grupo: ").strip().lower()
while entrada != "fin":
  try:
    cantidad = int(entrada)
  except ValueError:
    print("Entrada inválida: escriba un número entero o 'fin' para salir")
  else:
    if cantidad <= 0:
      print("Entrada inválida: el grupo debe tener al menos una persona.")
    elif ocupacion_actual + cantidad <= CAPACIDAD_MAXIMA:
      grupos_aceptados.append(cantidad)
      ocupacion_actual += cantidad
      espacio_disponilbles = CAPACIDAD_MAXIMA - ocupacion_actual
      print(f"Grupo aceptado: ingresan {cantidad} personas.")
      print(f"Ocupación actual: {ocupacion_actual}")
      print(f"Espacios disponibles: {espacio_disponilbles}")
    else:
      grupos_rechazados.append(cantidad)
      print(f"Grupo rechazado: no hay espacio para {cantidad} personas.")
      print(f"Ocupación actual: {ocupacion_actual}")
      print(f"Espacios disponibles: {espacio_disponilbles}")
    
  entrada = input("\nCantidad de personas del grupo: ").strip().lower()
    
    
    

# cuando ocupacion_actual también contiene ese valor durante el registro.
total_admitido = 0

for grupo in grupos_aceptados:
    total_admitido += grupo

# A partir de las listas se construyen indicadores que ayudan a interpretar
# el resultado del registro.
espacios_disponibles = CAPACIDAD_MAXIMA - total_admitido
porcentaje_ocupacion = total_admitido / CAPACIDAD_MAXIMA * 100

print("\nREPORTE FINAL")
print(f"Grupos aceptados: {len(grupos_aceptados)}")
print(f"Grupos rechazados: {len(grupos_rechazados)}")
print(f"Personas admitidas: {total_admitido}")
print(f"Capacidad máxima: {CAPACIDAD_MAXIMA}")
print(f"Espacios disponibles: {espacios_disponibles}")
print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")

# min y max requieren datos; primero se comprueba que la lista no esté vacía.
if grupos_aceptados:
    print(f"Grupo aceptado más pequeño: {min(grupos_aceptados)}")
    print(f"Grupo aceptado más grande: {max(grupos_aceptados)}")
else:
    print("No se aceptaron grupos durante el registro.")

# La clasificación convierte el indicador numérico en una lectura sencilla.
if total_admitido == CAPACIDAD_MAXIMA:
    print("Estado final: capacidad completa.")
else:
    print("Estado final: disponibilidad normal.")
