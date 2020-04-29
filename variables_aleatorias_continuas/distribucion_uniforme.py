import argparse
import math
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='distribucion_uniforme', description='Saca la probabilidad de que algo suceda en una distribución uniforme')
    parser.add_argument(
        '-A', type=float, help='Límite menor de función', required=True)
    parser.add_argument(
        '-B', type=float, help='Límite mayor de función', required=True)
    parser.add_argument(
        '--x_inferior', type=float, help='límite inferior de probabilidad a buscar', required=True)
    parser.add_argument(
        '--x_superior', type=float, help='límite superior de probabilidad de buscar', required=True)
    args = parser.parse_args()

    h = 1 / (args.B - args.A)
    valor_esperado = (args.A + args.B) / 2
    varianza = ((args.B - args.A) ** 2) / 12
    deviacion_estandar = varianza ** (1/2)
    lim_inferior = args.A if args.x_inferior < args.A else args.x_inferior
    lim_superior = args.B if args.x_superior > args.B else args.x_superior
    if (args.A > args.B) or (args.x_inferior > args.x_superior) or (lim_inferior > lim_superior):
        print(
            'Error: Los argumentos son inválidos: límites menores mayor que superiores')
        sys.exit()
    prob = h * (lim_superior - lim_inferior)
    print(
        f"""
        Probabilidad de que P({args.x_inferior} < x < {args.x_superior}) = {prob:.5f};
        Valor esperado [E(x)] = {valor_esperado:.5f};
        Varianza [V(x)] = {varianza:.5f};
        Desviación Estandar [σ]= {deviacion_estandar:.5f}
        """)
