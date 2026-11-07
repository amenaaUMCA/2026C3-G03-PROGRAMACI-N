from sedes import empredimientos

print("Emprendimientos registrados:", len(empredimientos))
print("Primer emprendimiento:", empredimientos[-1]['nombre'])
print("Primer emprendimiento ventas:", empredimientos[-1]["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDEDORES")
provincias = set() # provincias = {1,2,3,4}

#Cada vuelta procesara un diccionario
for e in empredimientos:
    total = sum(e['ventas'])
    porcentaje = total * 100 / e['meta']
    
    if porcentaje >= 100:
        estado = "Felicidaeds meta alcanzada!"
    elif porcentaje >= 80:
        estado = "Advertencia, meta no alcanzada revisar."
    else:
        estado = "CRITICO: revisar urgentemente!"
    
    print(
        f"{e['nombre']} | Total ₡{total:,.2f} -> "
        f"{porcentaje:.0f}% | estado: {estado}"
    )