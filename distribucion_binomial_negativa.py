import argparse
import math


def calc_combinations(n, k):
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n-k)
    num_combinations = n_fac / (k_fac * n_minus_k_fac)
    return num_combinations


def calc_comp_equal(x, r, p):
    x_plus_r_minus_1 = x + r - 1
    r_minus_1 = r - 1
    comb_de_funcion = calc_combinations(x_plus_r_minus_1, r_minus_1)
    q = 1 - p
    return comb_de_funcion * (p ** r) * (q ** x)


def calc_comp_greater_or_equal(x, r, p):
    return 1 - calc_comp_less(x, r, p)


def calc_comp_greater(x, r, p):
    return 1 - calc_comp_less_or_equal(x, r, p)


def calc_comp_less_or_equal(x, r, p):
    prob = 0
    for x_actual in range(0, x + 1):
        prob += calc_comp_equal(x_actual, r, p)
    return prob


def calc_comp_less(x, r, p):
    prob = 0
    for x_actual in range(0, x):
        prob += calc_comp_equal(x_actual, r, p)
    return prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='distribucion_binomial_negativa', description='Obtiene la probabilidad que x fallas sucedan para tener "r" éxitos en una distribución binomial negativa')
    parser.add_argument(
        '-r', type=int, help='Número de éxitos que se buscan', required=True)
    parser.add_argument(
        '-x', type=int, help='Número de fallas hasta tener "r" número de éxitos', required=True)
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
    valor_esperado = (args.r * (1 - args.p)) / args.p
    varianza = (args.r * (1 - args.p)) / (args.p ** 2)
    deviacion_estandar = varianza ** (1/2)
    prob = func_comparaciones[args.comparacion](args.x, args.r, args.p)
    print(
        f"""
        Probabilidad de que P(x {args.comparacion} {args.x}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
