import carro, moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.acelerar(20)
print(f"O carro está ligado? {uno_vermelho.ligado}")
print(f"Quantidade de combustível no carro: {uno_vermelho.qtd_combustivel}")
print(f"Velocidade do carro: {uno_vermelho.velocidade}")

moto_vermelha = moto.Moto("vermelha", "Gasolina", 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(15)
moto_vermelha.acelerar(30)
print(f"A moto está ligada? {moto_vermelha.ligado}")
print(f"Quantidade de combustível na moto: {moto_vermelha.qtd_combustivel}")
print(f"Velocidade da moto: {moto_vermelha.velocidade}")