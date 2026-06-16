"""
Faça um programa em Python para controlar os veículos de um estacionamento.

Inicialmente, o programa deve solicitar o cadastro dos veículos que entraram no estacionamento e, ao final, exibir todos os registros cadastrados.

Para cada veículo, representado por um dicionário, devem ser cadastradas as seguintes informações:
▪ Placa;
▪ Modelo;
▪ Horário de entrada;
▪ Horário de saída.

O programa deve calcular o tempo que o veículo permaneceu no estacionamento e o valor a pagar.

Considere que cada hora custa R$ 5,00.

Quando o usuário informar “0” como placa, o cadastro deve ser encerrado e os veículos devem ser listados.
"""

A = []

placa = input("informe a placa de seu veículo: ")


while placa != "0":

    modelo = input("informe o modelo de seu veículo: ")
    HE = input("informe o horário de entrada: ")
    HS = input("informe o horário de sáida: ")

    partes = HE.split(":")
    hora = int(partes[0])
    minuto = int(partes[1])

    partes2 = HS.split(":")
    hora2 = int(partes2[0])
    minuto2 = int(partes2[1])

    calculo1 = (hora * 60) + minuto
    calculo2 = (hora2 * 60) + minuto2
    pago = 0


    tempo = calculo2 - calculo1

    div = tempo // 60

    if tempo % 60 == 0:
        permanencia = div
        pago = div * 5
    else:
        permanencia = div + 1
        pago = (div + 1) * 5

    estacionamento = {
        "placa": placa,
        "modelo": modelo,
        "Horário de entrada": HE,
        "Horário de saída": HS,
        "Tempo": permanencia,
        "Valor á ser pago": pago,
    }
    A.append(estacionamento)
    placa = input("informe a placa de seu veículo: ")


for estacionamento in A:
    print(estacionamento)

