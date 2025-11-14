class Veiculo():
  """Classe que representa um veículo."""

  def __init__(self, cor, tipo_combustivel, potencia):
    """
    Método construtor da classe.
    
    - O parâmetro `self` representa a INSTÂNCIA que está sendo criada.
      Sempre que criamos um objeto, como em: carro = Veiculo(...)
      o `self` passa a ser uma referência para esse objeto.

    - As linhas `self.algo = algo` criam atributos dentro da instância.
      Ou seja, cada objeto terá sua própria cor, tipo de combustível etc.
    """

    # Atributos da instância (propriedades do objeto que está sendo criado)
    self.__cor = cor                       # atributo "cor" do objeto
    self.__tipo_combustivel = tipo_combustivel  # atributo "tipo_combustivel"
    self.__potencia = potencia             # atributo "potencia"

    # Atributos com valores iniciais
    self._qtd_combustivel = 0             # começa sem combustível (protected -> acesso na subclasse)
    self.__ligado = False                  # começa desligado
    self.__velocidade = 0                  # velocidade inicial

  def __del__(self):
    """
    Método destrutor: executado quando o objeto é removido da memória.
    Geralmente não é muito utilizado em Python,
    mas está aqui apenas para fins didáticos.
    """
    print("O objeto veículo foi destruído da memória.")

  def pintar(self, nova_cor):
    """Pinta o veículo com uma nova cor."""
    self.__cor = nova_cor
    print(f"O veículo foi pintado de {nova_cor}.")

  @property
  def cor(self):
    """Retorna a cor do veículo."""
    return self.__cor

  def abastecer(self, qtd_combustivel):
    """
    Abastece o veículo com a quantidade informada.

    - `self` novamente é a referência ao objeto que chamou o método.
      Exemplo: carro.abastecer(20) → self é o objeto 'carro'.
    """
    self._qtd_combustivel += qtd_combustivel
    print(f"O veículo foi abastecido com {qtd_combustivel} litros.")

  def ligar(self):
    """Liga o veículo, caso ainda esteja desligado."""
    if self.__ligado:
      print("O veículo já está ligado.")
    else:
      self.__ligado = True
      print("O veículo foi ligado.")

  def desligar(self):
    """Desliga o veículo, caso esteja ligado."""
    if not self.__ligado:
      print("O veículo já está desligado.")
    else: 
      self.__ligado = False
      print("O veículo foi desligado.")

  def acelerar(self, velocidade=10):
    """
    Acelera o veículo.

    - Só é possível acelerar se o veículo estiver ligado.
    - Usamos `self.velocidade` para alterar a velocidade da instância,
      ou seja, a velocidade daquele objeto específico.
    """
    if self.__ligado:
      self.__velocidade += velocidade
      print(f"O veículo acelerou {velocidade} km/h. Velocidade atual: {self.__velocidade} km/h.")
    else:
      print("O veículo está desligado. Não é possível acelerar.")
