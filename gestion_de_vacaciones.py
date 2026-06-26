import csv

def cargar_empleados(ruta_csv="empleados.csv"):
    empleados = {}
    try:
        with open(ruta_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                legajo = fila["legajo"].strip()
                empleados[legajo] = {
                    "nombre": fila["nombre"].strip(),
                    "dias_disponibles": int(fila["dias_disponibles"].strip()),
                    "estado": fila["estado"].strip()
                }
    except FileNotFoundError:
        print(f"🤖 Bot: ❌ No se encontró el archivo {ruta_csv}")
    return empleados

def solicitar_vacaciones():
    empleados = cargar_empleados()
    print("🤖 Bot: ¡Bienvenido al sistema de Solicitud de Vacaciones! 🏖️")

    legajo = input("👤 Usuario: Ingrese su número de legajo: ").strip()

    if legajo not in empleados:
        print("🤖 Bot: ❌ Legajo no encontrado. Solicitud rechazada.")
        return

    fechas = input("👤 Usuario: Ingrese las fechas deseadas (ej. 10-06 al 20-06): ").strip()
    if "-" not in fechas and "/" not in fechas:
        print("🤖 Bot: ❌ Formato de fechas inválido. Solicitud rechazada.")
        return

    dias_solicitados = int(input("👤 Usuario: Ingrese la cantidad de días solicitados: ").strip())
    dias_disponibles = empleados[legajo]["dias_disponibles"]

    print(f"🤖 Bot: 📊 Días disponibles para {empleados[legajo]['nombre']}: {dias_disponibles}")

    if dias_solicitados <= dias_disponibles:
        print("🤖 Bot: ✅ Solicitud enviada a RRHH para revisión...")
        decision = input("👩‍💼 RRHH: ¿Aprobar solicitud? (si/no): ").strip().lower()
        if decision == "si":
            print("🤖 Bot: 🎉 Vacaciones aprobadas. ¡Disfrute su descanso!")
        else:
            print("🤖 Bot: ❌ Solicitud rechazada por RRHH.")
    else:
        print("🤖 Bot: ❌ Saldo insuficiente de días. Solicitud rechazada.")

if __name__ == "__main__":
    solicitar_vacaciones()
