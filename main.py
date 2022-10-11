import pessoa as p;
import conta as c;
import historico as h;

pessoa1 = p.Pessoa("Vinicius","644512","São Paulo")
pessoa1.mostrarPessoa()

conta1 = c.Conta("1234","Vinicius",40000,200000)
conta2 = c.Conta("5678","Victor",20000,100000)

conta1.deposito()
conta1.saque()
conta1.transferencia(conta2)
conta1.historico_transacoes(conta1.historico)