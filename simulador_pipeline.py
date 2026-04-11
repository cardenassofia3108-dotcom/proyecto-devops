import random

pipeline = [
    {"nombre": "Build", "estado": None},
    {"nombre": "Test", "estado": None},
    {"nombre": "Security Scan", "estado": None},
    {"nombre": "Deploy", "estado": None},
    {"nombre": "Monitoring", "estado": None}
]

def ejecutar_pipeline():
    print("Ejecutando pipeline...\n")

    fallo = False

    for etapa in pipeline:
        if not fallo:
            etapa["estado"] = random.choice(["success", "fail"])
            print(f"{etapa['nombre']}: {etapa['estado']}")

            if etapa["estado"] == "fail":
                fallo = True
        else:
            etapa["estado"] = "skipped"
            print(f"{etapa['nombre']}: skipped")

    print("\nResultado final:")
    if fallo:
        print("Pipeline FALLÓ")
    else:
        print("Pipeline EXITOSO")

ejecutar_pipeline()
