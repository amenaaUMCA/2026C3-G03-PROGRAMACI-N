"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")

# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
# Cada clave es un nombre de medicamento y su valor es el nombre estandarizado
equivalencias = {
    "acetaminofen" : "acetaminofén",
    "paracetamol": "acetaminofén",
    "antiacido": "antíacido",
    "losartán": "losartan"
}
conteo_medicamentos = {}
total_medicamentos = 0
print("\n\tANALISIS FASE #1 MUESTRA 3")
for indice in range (3):
    registro = registros[indice]
    print(f"\nCédula: {registro['paciente_cedula']}"
        f"\n- Paciente: {registro['paciente_nombre']}"
        f"\n- Diagnóstico: {registro['diagnostico']}"
        f"\n- Medicamentos: {registro['medicamentos']}")

    for medicamento in registro['medicamentos']:
        #Limpieza PARACETAMOL -> paracetamol -> aceteminofén
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        #Contar medicamentos
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
        
print("\nTotal de medicamentos recetados:", total_medicamentos)
print(conteo_medicamentos)

# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\nANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")
conteo_medicamentos = {}
total_medicamentos = 0
conteo_hospital = {}
total_paciente = 0
for registro in registros:
    
    
    for medicamento in registro['medicamentos']:
        #Limpieza PARACETAMOL -> paracetamol -> aceteminofén
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]
        #Contar medicamentos
        total_medicamentos += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
            
print("\nTotal de medicamentos recetados:", total_medicamentos)
for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}:\t {cantidad}")
print("\nTotal de PACIENTES:", total_paciente)


# FASE 3: CONTAR ATENCIONES POR HOSPITAL
conteo_hospital = {}
total_paciente = 0
for registro in registros:
    total_paciente += 1
    hospital = registro["hospital"]
    if hospital not in conteo_hospital:
        conteo_hospital[hospital] = 0
    conteo_hospital[hospital] +=1
print("\nTotal de PACIENTES:", total_paciente)
for hospital, cantidad in conteo_hospital.items():
    print(f"- {hospital}:\t {cantidad}")

# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

