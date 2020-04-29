import argparse
import math


def calc_comp_equal(x, p):
    q = 1 - p
    return p * (q ** (x - 1))


def calc_comp_greater_or_equal(x, p):
    return 1 - calc_comp_less(x, p)


def calc_comp_greater(x, p):
    return 1 - calc_comp_less_or_equal(x, p)


def calc_comp_less_or_equal(x, p):
    prob = 0
    for x_actual in range(1, x + 1):
        prob += calc_comp_equal(x_actual, p)
    return prob


def calc_comp_less(x, p):
    prob = 0
    for x_actual in range(1, x):
        prob += calc_comp_equal(x_actual, p)
    return prob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='distribucion_geometrica', description='Obtiene la probabilidad que haya un éxito en el experimento "x"')
    parser.add_argument(
        '-x', type=int, help='Número de fallas hasta tener el primer éxito', required=True)
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
    valor_esperado = 1 / args.p
    varianza = (1 - args.p) / (args.p ** 2)
    deviacion_estandar = varianza ** (1/2)
    prob = func_comparaciones[args.comparacion](args.x, args.p)
    print(
        f"""
        Probabilidad de que P(x {args.comparacion} {args.x}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
