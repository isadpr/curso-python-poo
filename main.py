import carro, moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1.0, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.acelerar(20)
uno_vermelho.pintar("azul")
print(f"A cor do carro é {uno_vermelho.cor}.")

moto_vermelha = moto.Moto("vermelha", "Gasolina", 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
moto_vermelha.acelerar(30)
