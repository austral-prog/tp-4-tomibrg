def line():
    coef_a = float(input('Ingrese el coeficiente A: '))
    coef_b = float(input('Ingrese el coeficiente B: '))
    coef_x1 = float(input('Ingrese el coeficiente X1: '))
    coef_x2 = float(input('Ingrese el coeficiente X2: '))

    print(f'El coeficiente A de su ecuación de la recta es: {coef_a}')
    print(f'El coeficiente B de su ecuación de la recta es: {coef_b}')
    print(f'El coeficiente X1 de su ecuación de la recta es: {coef_x1}')
    print(f'El coeficiente X2 de su ecuación de la recta es: {coef_x2}\n')
    print(f'Para la siguiente ecuación:\n\tY = {coef_a}X + {coef_b}\n')

    punto_y1 = coef_a*coef_x1 + coef_b
    punto_y2 = coef_a*coef_x2 + coef_b

    print(f'Dados los siguientes puntos:\n\tP1 ({coef_x1}, {punto_y1})')
    print(f'\tP2 ({coef_x2}, {punto_y2})\n')

    dist = ((coef_x2 - coef_x1)**2 + (punto_y2 - punto_y1)**2)**(1/2)
    print(f'La distancia entre ellos es: {dist}')

