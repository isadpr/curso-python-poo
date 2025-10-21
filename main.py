import carro

uno_vermelho = carro.Carro("vermelho", 4, "Flex", 1.0, 0, False, 0)
uno_vermelho.ligar()
help(uno_vermelho.abastecer)
uno_vermelho.abastecer(20)
uno_vermelho.acelerar(20)
print(f"O carro está ligado? {uno_vermelho.ligado}")
print(f"Quantidade de combustível no carro: {uno_vermelho.qtd_combustivel}")
print(f"Velocidade do carro: {uno_vermelho.velocidade}")