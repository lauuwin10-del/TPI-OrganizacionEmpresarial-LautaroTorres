import csv


# Esta función se encarga de leer los datos de los empleados desde un archivo CSV
# y devolverlos en un diccionario para que el sistema pueda consultarlos

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


# Esta función simula la interacción de un chatbot para gestionar solicitudes de vacaciones.

def solicitar_vacaciones():
    empleados = cargar_empleados()

    print("🤖 Bot: ¡Bienvenido al sistema de Solicitud de Vacaciones! 🏖️")

    # =============================
    # VALIDACIÓN DEL LEGAJO
    # =============================
    while True:
        legajo = input("👤 Usuario: Ingrese su número de legajo: ").strip()

        if legajo in empleados:
            break

        print("🤖 Bot: ❌ Legajo no encontrado. Intente nuevamente.")

    # =============================
    # VALIDACIÓN DE FECHAS
    # =============================
    while True:
        fechas = input("👤 Usuario: Ingrese las fechas deseadas (ej. 10-06 al 20-06): ").strip()

        if "-" in fechas or "/" in fechas:
            break

        print("🤖 Bot: ❌ Formato de fechas inválido. Intente nuevamente.")

    # =============================
    # VALIDACIÓN DE DÍAS
    # =============================
    while True:
        try:
            dias_solicitados = int(input("👤 Usuario: Ingrese la cantidad de días solicitados: ").strip())

            if dias_solicitados <= 0:
                print("🤖 Bot: ❌ La cantidad de días debe ser mayor que cero.")
            else:
                break

        except ValueError:
            print("🤖 Bot: ❌ Debe ingresar un número válido.")

    dias_disponibles = empleados[legajo]["dias_disponibles"]

    print(f"🤖 Bot: 📊 Días disponibles para {empleados[legajo]['nombre']}: {dias_disponibles}")

    if dias_solicitados <= dias_disponibles:

        print("🤖 Bot: ✅ Solicitud enviada a RRHH para revisión...")

        # =============================
        # VALIDACIÓN DE RESPUESTA RRHH
        # =============================
        while True:
            decision = input("👩‍💼 RRHH: ¿Aprobar solicitud? (si/no): ").strip().lower()

            if decision == "si":
                print("🤖 Bot: 🎉 Vacaciones aprobadas. ¡Disfrute su descanso!")
                break

            elif decision == "no":
                print("🤖 Bot: ❌ Solicitud rechazada por RRHH.")
                break

            else:
                print("🤖 Bot: ❌ Debe responder únicamente 'si' o 'no'.")

    else:
        print("🤖 Bot: ❌ Saldo insuficiente de días. Solicitud rechazada.")


if __name__ == "__main__":
    solicitar_vacaciones()