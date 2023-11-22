from residencias.classes import Residencia, Apartamento

def main():
    residencia_1 = Residencia(4, 20.5, "Rua das Flores", "25/09/2023")
    print(residencia_1)
    print("----------------------")
    apartamento_1 = Apartamento(5, 23.5, "Rua Augusta", "17/06/2004",4)
    print(apartamento_1)

if __name__ == "__main__":
    main()



