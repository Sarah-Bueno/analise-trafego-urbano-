"""
Faça um programa em Python para cadastrar os veículos de uma locadora de
automóveis. Inicialmente, o programa deve solicitar o cadastro dos veículos e,
ao final, exibir todos os veículos cadastrados. Para cada veículo, representado
por um dicionário, devem ser cadastradas as seguintes informações:
▪ Placa;
▪ Marca;
▪ Modelo;
▪ Cor.
Quando o usuário informar “0” como placa, o cadastro deve ser encerrado e
os veículos devem ser listados.

"""
placa = input("informe a placa: ")

A = []

while placa != "0":
    Marca = input("informe a marca: ")
    Modelo = input("informe a modelo: ")
    Cor = input("informe a cor: ")

    locadora = {
        "Placa": placa,
        "Marca": Marca,
        "Modelo": Modelo,
        "Cor": Cor,
    }
    A.append(locadora)
    placa = input("informe a placa: ")

for veiculo in A:
    print(veiculo)
