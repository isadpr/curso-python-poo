class Veiculo():
  """Classe que representa um veículo."""
  def __init__(self, cor, tipo_combustivel, potencia):
    self.cor = cor
    self.tipo_combustivel = tipo_combustivel
    self.potencia = potencia
    self.qtd_combustivel = 0
    self.ligado = False
    self.velocidade = 0

  def __del__ (self):
    print("O objeto veículo foi destruído da memória.")

  def abastecer(self, qtd_combustivel):
    """Abastece o veículo com a quantidade de combustível informada."""
    self.qtd_combustivel += qtd_combustivel

  def ligar(self):
    """Liga o veículo."""
    if self.ligado:
      print("O veículo já está ligado.")
    else:
      self.ligado = True

  def desligar(self):
    """Desliga o veículo."""
    if self.ligado == False:
      print("O veículo já está desligado.")
    else: 
      self.ligado = False

  def acelerar(self, velocidade=10):
    """Acelera o veículo na velocidade informada."""
    if self.ligado:
      self.velocidade += velocidade
    else:
      print("O veículo está desligado. Não é possível acelerar.")
