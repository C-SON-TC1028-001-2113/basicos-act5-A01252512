import math
def main():
    #escribe tu código abajo de esta línea
    altura = float(input("Altura de la casa: "))
    angulo = int(input("Angulo en grados: "))
    angulo_rad = math.radians(angulo)

    largo = round(altura/math.sin(angulo_rad))

    print(f'Largo de la escalera: {largo}')

if __name__ == '__main__':
    main()