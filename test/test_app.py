from app import calcular_prioridad

def test_calcular_prioridad():
    # Prueba con días abiertos negativos
    assert calcular_prioridad(3) == "Normal"

def test_prioridad_alta():
 # Prueba con días abiertos mayores a 5
    assert calcular_prioridad(6) == "Alta"
def test_prioridad_normal():  
    # Prueba con días abiertos iguales a 5
    assert calcular_prioridad(5) == "Normal"
def test_prioridad_error():  
    # Prueba con días abiertos menores a 5
    assert calcular_prioridad(3) == "Normal"