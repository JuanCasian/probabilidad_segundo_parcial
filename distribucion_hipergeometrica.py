import argparse
import math


def calc_combinations(n, k):
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n-k)
    num_combinations = n_fac / (k_fac * n_minus_k_fac)
    return num_combinations


def calc_comp_equal(x, n, M, N):
    M_comb_x = calc_combinations(M, x)
    N_minus_M_comb_n_minus_x = calc_combinations(N-M, n-x)
    N_comb_n = calc_combinations(N, n)
    return (M_comb_x * N_minus_M_comb_n_minus_x) / N_comb_n


def calc_comp_greater_or_equal(x, n, M, N):
    prob = 0
    for x_actual in range(x, n + 1):
        prob += calc_comp_equal(x_actual, n, M, N)
    return prob


def calc_comp_greater(x, n, M, N):
    prob = 0
    for x_actual in range(x + 1, n + 1):
        prob += calc_comp_equal(x_actual, n, M, N)
    return prob


def calc_comp_less_or_equal(x, n, M, N):
    prob = 0
    for x_actual in range(0, x + 1):
        prob += calc_comp_equal(x_actual, n, M, N)
    return prob


def calc_comp_less(x, n, M, N):
    prob = 0
    for x_actual in range(0, x):
        prob += calc_comp_equal(x_actual, n, M, N)
    return prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='distribucion_hipergeometrica', description='Obtiene la probabilidad que x suceda en una distribución hipergeométrica')
    parser.add_argument(
        '-n', type=int, help='Tamaño de muestra', required=True)
    parser.add_argument(
        '-N', type=int, help='Tamaño de la población completa', required=True)
    parser.add_argument(
        '-x', type=int, help='Número de éxitos que se buscan', required=True)
    parser.add_argument(
        '-M', type=float, help='Cantidad de éxitos que hubo en la población completa', required=True)
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
    valor_esperado = args.n * (args.M / args.N)
    varianza = valor_esperado * \
        (1-(args.M / args.N)) * ((args.N - args.n) / (args.N - 1))
    deviacion_estandar = varianza ** (1/2)
    prob = func_comparaciones[args.comparacion](args.x, args.n, args.M, args.N)
    print(
        f"""
        Probabilidad de que P(x {args.comparacion} {args.x}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
