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
        prog='aproximacion_binomial_a_posisson', description='Utiliza el cálculo de poisson para encontrar la probabilidad de que x número de éxitos se obtengan')
    parser.add_argument(
        '-x', type=int, help='Número de éxitos que esperamos', required=True)
    parser.add_argument(
        '-n', type=float, help='Tamaño de muestra', required=True)
    parser.add_argument(
        '-p', type=float, help='Probabilidad de éxito', required=True)
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
    l = args.n * args.p
    if (args.n < 50):
        print('Este problema no es tan bueno para aproximarse porque n es menor que 50')
    if (l > 5):
        print('Este problema no es tan bueno para aproximarse porque n * p da más de 5\n')
    valor_esperado = l
    varianza = l
    deviacion_estandar = varianza ** (1/2)
    prob = func_comparaciones[args.comparacion](args.x, l)
    print(
        f"""
        Probabilidad de que P(x {args.comparacion} {args.x}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
