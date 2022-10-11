class Pessoa:
  def __init__(self, nome, CPF, cidade):
    self.nome = nome
    self.CPF = CPF
    self.cidade = cidade

  def mostrarPessoa(self):
    print("Nome: " + self.nome + "\nCPF: " + self.CPF + "\nCidade: " + self.cidade)