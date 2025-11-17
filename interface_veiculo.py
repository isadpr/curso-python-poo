from abc import ABC, abstractmethod

"""
Python não possui interfaces formais como em outras linguagens, 
mas podemos usar classes abstratas para definir interfaces.

Interfaces são usadas para garantir que certas classes implementem
métodos específicos, promovendo consistência e facilitando a manutenção.
"""

class InterfaceVeiculo(ABC): 
  """Interface que define os métodos que um veículo deve implementar."""
  @abstractmethod
  def abastecer(self, qtd_combustivel):
    # não pode ser implementado aqui
    pass

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @abstractmethod
  def acelerar(self, velocidade=10):
    pass

  @abstractmethod
  def pintar(self, nova_cor):
    pass