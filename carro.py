import veiculo
class Carro(veiculo.Veiculo):
  """Classe que representa um carro."""
  def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
    super().__init__(cor, tipo_combustivel, potencia)
    self.qtd_portas = qtd_portas

  def abastecer(self, qtd_combustivel):
   # print("o método abastecer da classe Carro foi chamado.")
    self._qtd_combustivel += qtd_combustivel

  def pintar(self, nova_cor):
    if nova_cor == 'rosa':
      print("Carro não pode ser pintado de rosa.")
    else:
      super().pintar(nova_cor)