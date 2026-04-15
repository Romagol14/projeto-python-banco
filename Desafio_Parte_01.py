from abc import ABC, abstractmethod
from datetime import datetime

# COMENTÁRIOS DE APRENDIZADO:
# self: conecta o código ao objeto real.
# _: indica que o atributo é privado (Encapsulamento).

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = [] 

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta) 

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco) # Herança Simples
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico() 

    @property # Getter para ler o saldo de forma segura
    def saldo(self):
        return self._saldo

    def sacar(self, valor): 
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print("\n=== Saque realizado! ===")
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado! ===")
            return True
        return False

class Historico:
    def __init__(self):
        self._transacoes = [] 

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

class Transacao(ABC): # Classe Abstrata (Molde)
    @property
    @abstractmethod
    def valor(self): pass

    @abstractmethod
    def registrar(self, conta): pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self): return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
    
    # NOTA DO ALUNO: Consegui entender os conceitos de classe e herança, 
    # mas ainda estou praticando a lógica completa de saque.
