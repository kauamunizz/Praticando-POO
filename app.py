# from modelos import biblioteca
from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_interior = Biblioteca("Biblioteca do Interior")

biblioteca_cidade.altera_ativo()

biblioteca_cidade.receber_avalicao("Mariana", 8.5)
biblioteca_cidade.receber_avalicao("Kaua", 9.5)

def main():
    Biblioteca.listar_biblioteca()

if __name__ == "__main__":
    main()