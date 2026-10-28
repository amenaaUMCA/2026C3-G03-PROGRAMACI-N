from sedes import empredimientos

print("Emprendimientos registrados:", len(empredimientos))
print("Primer emprendimiento:", empredimientos[0]["nombre"])
print("Primer emprendimiento ventas:", empredimientos[0]["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDEDORES")
provincias = set() # provincias = {1,2,3,4}

#Cada vuelta procesara un diccionario
for empre in empredimientos:
    total = sum(empre['ventas'])
    porcentaje = total / empre['meta'] * 100
    
    provincias.add(empre['provincia'])
    
    if porcentaje >= 100:
        estado = "Meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención!"
        
    print(
        f"{empre["nombre"]} | Total: ₡{total:,.2f} | "
        f"Cumplimiento: {porcentaje:.2f}% | {estado}"
    )

print("\nProvincias set:", provincias)