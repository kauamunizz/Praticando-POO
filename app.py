# from modelos import biblioteca
from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista


biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_interior = Biblioteca("Biblioteca do Interior")

livro1 = Livro("1984", "George Orwell", 30.0, "085-2884")
revista1 = Revista("National Geographic", "Joe Doe", 15.0, "Quinta")

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)

livro1.aplicar_desconto()
revista1.aplicar_desconto()

# biblioteca_cidade.altera_ativo()

# biblioteca_cidade.receber_avalicao("Mariana", 8.5)
# biblioteca_cidade.receber_avalicao("Kaua", 9.5)

def main():
    print(vars(livro1))
    print(vars(revista1))
    biblioteca_cidade.exibir_item()
    # Biblioteca.listar_biblioteca()

if __name__ == "__main__":
    main()