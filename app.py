def generar_matriz_y_vector(resultado):
    matriz_A = []
    vector_b = []
    ecuaciones = resultado.splitlines()

    for ecuacion in ecuaciones:
        termino = ecuacion.split("=")
        if len(termino) == 2:
            ecuacion_izquierda = termino[0].strip()
            ecuacion_derecha = termino[1].strip()
            
            try:
                vector_b.append(int(ecuacion_derecha))
            except ValueError:
                continue 

            coeficientes = {'x': 0, 'y': 0, 'z': 0}

            for var in ['x', 'y', 'z']:
                # Modificación para ignorar mayúsculas y minúsculas
                match = re.search(r'([+-]?\d*)(' + var + r')', ecuacion_izquierda, re.IGNORECASE)
                if match:
                    coef = match.group(1)
                    if coef == '' or coef == '+':
                        coeficientes[var.lower()] = 1
                    elif coef == '-':
                        coeficientes[var.lower()] = -1
                    else:
                        coeficientes[var.lower()] = int(coef)
            
            matriz_A.append([coeficientes['x'], coeficientes['y'], coeficientes['z']])

    return matriz_A, vector_b
