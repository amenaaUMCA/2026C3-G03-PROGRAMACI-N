#Listas
#               0          1         2
mi_lista = ["Manzana", "Sandia", 'Fresa']

cantidad = len(mi_lista)
print(mi_lista, "cantidad elementos:", cantidad)

mi_lista[1] = 'mango'
print(mi_lista)

temporada = ["Pera", "Kiwi"]
mi_lista = mi_lista + temporada
print(mi_lista)

mi_lista.sort()
print(mi_lista)

fruta_nueva = input("Ingrese su fruta favorita: ")
mi_lista.append(fruta_nueva)
print(mi_lista)

mi_lista.insert(1, "Melón")
print(mi_lista)

try:
    eliminar = input("Ingresa la fruta a eliminar: ").strip()
    mi_lista.remove(eliminar)
except ValueError:
    print("La fruta no existe en la lista")

print(mi_lista)

minimo = min(mi_lista)
maximo = max(mi_lista)

print(minimo, maximo)

if "Aguacate" in mi_lista:
    print("Tenemos Aguacate !!")
else:
    print("NO tenemos Aguacate")
