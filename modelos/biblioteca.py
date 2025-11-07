from modelos.avaliacao import Avaliacao

class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False #Atributo privado
        self._avaliacao = []
        Biblioteca.bibliotecas.append(self)
    
    def __str__(self):
        return self.nome
    
    @classmethod #decorator
    def listar_biblioteca(cls):
        print(f"{'Nome da Biblioteca'.ljust(25)}  - {'Nota media'.ljust(25)} - {'status'}")
        for lib in Biblioteca.bibliotecas:
            print(f"{lib.nome.ljust(25)}  - {str(lib.media_avaliacao).ljust(25)} {lib.ativo}")
            
    def altera_ativo(self):
        self._ativo = not self._ativo
        
    # Encapsulamento
    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"
    
    def receber_avalicao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media