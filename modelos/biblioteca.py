from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import ItemBiblioteca

class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False #Atributo privado
        self._avaliacao = []
        self._itens = []
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
    
    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
            
    def exibir_item(self):
        print(f"Itens da Bibilioteca {self.nome}")
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, "isbn"):
                msg_livro = f"{i}. (Livro) Titulo {item._titulo} ; Autor: {item._autor} ; Preco {item._preco} ; ISBN: {item.isbn}"
                print(msg_livro)
            else:
                msg_revista = f"{i}. (Revista) Titulo {item._titulo} ; Autor: {item._autor} ; Preco {item._preco} ; Edicao: {item.edicao}"
                print(msg_revista)