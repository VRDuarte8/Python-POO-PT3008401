class Historico:
  def armazena_transacoes(self,historico,texto):
    self.historico.append(texto)
    with open('historico.txt','r+') as arquivo:
      arquivo.write(str(self.historico))
      arquivo.close()
    
  def historico_transacoes(self,historico):
    print("Histórico")
    print(*self.historico, sep = "\n")
    with open('historico.txt') as arquivo:
      print(arquivo.read())