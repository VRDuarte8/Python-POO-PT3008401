from historico import Historico as h;

class Conta(h):
  def __init__(self, numero, cliente, saldo, limite):
    self.numero = numero
    self.cliente = cliente
    self.saldo  = saldo
    self.limite = limite
    self.historico = []

  def deposito(self):
    valor = int(input("Valor a depositar: "))
    self.saldo += valor
    print("Valor depositado. Saldo atual: " + str(self.saldo))
    self.armazena_transacoes(self.historico,"Tipo: Depósito / Valor: " + str(valor))

  def saque(self):
    valor = int(input("Valor a sacar: "))
    self.saldo -= valor
    print("Valor sacado. Saldo atual: " + str(self.saldo))
    self.armazena_transacoes(self.historico,"Tipo: Saque / Valor: " + str(valor))

  def transferencia(self, recebedor):
    valor = int(input("Valor a transferir: "))
    self.saldo -= valor
    recebedor.saldo += valor
    print("Transação concluída. Saldo atual: " + str(self.saldo))
    self.armazena_transacoes(self.historico,"Tipo: Transferência / Valor: " + str(valor))