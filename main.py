from residencias.classes import Residencia, Apartamento, Casa

def main():
    casa_1 = Casa(6, 33.5, "Rua Francisca",True)
    print(casa_1.alugado_em)
    casa_1.alugar()
    print(casa_1.alugado_em)
    print(casa_1)

if __name__ == "__main__":
    main()



