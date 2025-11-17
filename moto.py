import veiculo  

class Moto(veiculo.Veiculo):
  """Classe que representa uma moto."""
  def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
    super().__init__(cor, tipo_combustivel, potencia)
    self.qtd_passageiros = qtd_passageiros

  def abastecer(self, qtd_combustivel):
    # print("o método abastecer da classe Carro foi chamado.")
    if self._qtd_combustivel >= 30:
      print("O tanque da moto já está cheio.")
    else:
      self._qtd_combustivel += qtd_combustivel

  def pintar(self, nova_cor):
    if nova_cor == 'azul':
      print("Moto não pode ser pintada de azul.")
    else:
      super().pintar(nova_cor)