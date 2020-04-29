import argparse
import math


def calc_comp_equal(x, l):
    return ((math.e ** (-l)) * (l ** x) / math.factorial(x))


def calc_comp_greater_or_equal(x, l):
    return 1 - calc_comp_less(x, l)


def calc_comp_greater(x, l):
    return 1 - calc_comp_less_or_equal(x, l)


def calc_comp_less_or_equal(x, l):
    prob = 0
    for x_actual in range(0, x + 1):
        prob += calc_comp_equal(x_actual, l)
    return prob


def calc_comp_less(x, l):
    prob = 0
    for x_actual in range(0, x):
        prob += calc_comp_equal(x_actual, l)
    return prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='distribucion_poisson', description='Obtiene la probabilidad de que algo sucedia en una medida de tiempo según su lambda')
    parser.add_argument(
        '-x', type=int, help='Número de sucesos que esperamos por unidad de tiempo', required=True)
    parser.add_argument(
        '-l', type=float, help='Lambda: tasa en la que sucede algo', required=True)
    parser.add_argument('-c', '--comparacion', help="Ingresa el tipo de comparación: P(X=x)",
                        choices=['=', '>=', '<=', '<', '>'], required=True)
    args = parser.parse_args()
    func_comparaciones = {
        '=': calc_comp_equal,
        '>=': calc_comp_greater_or_equal,
        '>': calc_comp_greater,
        '<=': calc_comp_less_or_equal,
        '<': calc_comp_less,
    }
    valor_esperado = args.l
    varianza = args.l
    deviacion_estandar = varianza ** (1/2)
    prob = func_comparaciones[args.comparacion](args.x, args.l)
    print(
        f"""
        Probabilidad de que P(x {args.comparacion} {args.x}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
