# from class_residencias.classes import Residencia, Apartamento, Casa
class Person():
    ...
def main():
    # casa_1 = Casa(6, 33.5, "Rua Francisca",True)
    # print(casa_1.alugado_em)
    # casa_1.alugar()
    # print(casa_1.alugado_em)
    # print(casa_1)
    ...

if __name__ == "__main__":
    main()

#FORMA DE COLOCAR UM DICIONÁRIO DENTRO DO BANCO
person_data = {'name': 'João'}
joao = Person(**person_data)
joao.save()


