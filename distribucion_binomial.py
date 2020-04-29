import argparse
import math


def calc_combinations(n, k):
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n-k)
    num_combinations = n_fac / (k_fac * n_minus_k_fac)
    return num_combinations


def calc_comp_equal(n, x, p):
    q = 1 - p
    return calc_combinations(n, x) * (p ** x) * (q ** (n - x))


def calc_comp_greater_or_equal(n, x, p):
    prob = 0
    for x_actual in range(x, n + 1):
        prob += calc_comp_equal(n, x_actual, p)
    return prob


def calc_comp_greater(n, x, p):
    prob = 0
    for x_actual in range(x + 1, n + 1):
        prob += calc_comp_equal(n, x_actual, p)
    return prob


def calc_comp_less_or_equal(n, x, p):
    prob = 0
    for x_actual in range(0, x + 1):
        prob += calc_comp_equal(n, x_actual, p)
    return prob


def calc_comp_less(n, x, p):
    prob = 0
    for x_actual in range(0, x):
        prob += calc_comp_equal(n, x_actual, p)
    return prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='distribucion_binomial', description='Obtiene la probabilidad que x suceda en una distribución binomial')
    parser.add_argument(
        '-n', type=int, help='Número de experimentos', required=True)
    parser.add_argument(
        '-x', type=int, help='Número de éxitos que se buscan', required=True)
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
    valor_esperado = args.n * args.p
    varianza = valor_esperado * (1 - args.p)
    deviacion_estandar = varianza ** (1/2)
    prob = func_comparaciones[args.comparacion](args.n, args.x, args.p)
    print(
        f"""
        Probabilidad de que P(x {args.comparacion} {args.x}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
