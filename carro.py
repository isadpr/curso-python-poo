class Carro():
  """Classe que representa um carro."""
  def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, ligado, velocidade):
    self.cor = cor
    self.qtd_portas = qtd_portas
    self.tipo_combustivel = tipo_combustivel
    self.potencia = potencia
    self.qtd_combustivel = qtd_combustivel
    self.ligado = ligado
    self.velocidade = velocidade

  def abastecer(self, qtd_combustivel):
    """Abastece o carro com a quantidade de combustível informada."""
    self.qtd_combustivel += qtd_combustivel

  def ligar(self):
    """Liga o carro."""
    if self.ligado:
      print("O carro já está ligado.")
    else:
      self.ligado = True

  def desligar(self):
    """Desliga o carro."""
    if self.ligado == False:
      print("O carro já está desligado.")
    else: 
      self.ligado = False

  def acelerar(self, velocidade=10):
    """Acelera o carro na velocidade informada."""
    if self.ligado:
      self.velocidade += velocidade
    else:
      print("O carro está desligado. Não é possível acelerar.")
