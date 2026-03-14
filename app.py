def calcular_prioridad(dias_abiertos):
    """Calcula la prioridad de un caso basado en los días abiertos."""
    if dias_abiertos < 0:
        return "Error: Dias negativos"
    elif dias_abiertos > 5:
        return "Alta"
    else:
        return "Normal"
