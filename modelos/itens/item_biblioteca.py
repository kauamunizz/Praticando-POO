from abc import ABC, abstractclassmethod

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
        
    @abstractclassmethod
    def aplicar_desconto(self):
        pass