"""Micro-reto 4: reunir datos hasta recibir una palabra de cierre.

Contexto: se registran resultados ficticios de una actividad universitaria.
La cantidad de registros no se conoce al iniciar.

Ingrese enteros positivos y escriba "fin" para terminar. No ingrese texto
distinto de "fin" ni números negativos en esta práctica.
"""
max_aforo = 700
aforo = 0
aceptados = []
rechazados = []

entrada = input("Cantidad de grupo (o fin para terminar): ").strip().lower()

while entrada != "fin":
    grupo = int(entrada)
    if grupo + aforo > max_aforo:
        print("Rechazado")
        rechazados.append(grupo)        
    else:
        print("Aceptado")
        aceptados.append(grupo)
        aforo = aforo + grupo

    entrada = input("Cantidad de grupo (o fin para terminar): ").strip().lower()

print("Resultados rechazados:", rechazados)
print("Cantidad de resultados:", len(rechazados))

if rechazados:
    promedio = sum(rechazados) / len(rechazados)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron resultados.")

# Con las entradas 80, 65, 90 y fin, se espera:
# Resultados registrados: [80, 65, 90]
# Cantidad de resultados: 3
# Promedio: 78.33
