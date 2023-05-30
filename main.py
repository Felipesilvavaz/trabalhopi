#produto = {codigo, nome, quantidade}
class Product:
 def __init__(self, codigo, nome, quantidade):
     self.codigo = codigo
     self.nome = nome
     self.quantidade = quantidade
 def __str__(self):
     return f"codigo: {self.codigo} nome: {self.nome} quantidade: {self.quantidade}"

def getProduct():
    codigo = int(input("digite o codigo: "))
    product = theStore.get(codigo)

    if product == None:
        print("PRODUTO NAO ENCONTRADO")
    return product

def menu():
    print("=" * 20)
    print("-1 sair")
    print("0 cadastrar novo produto")
    print("1 registrar entrada")
    print("2 registrar saida")
    print("3 verificar saldo de produtos")
    print("4 imprimir produtos")

def novoProduto():
    codigo = int(input("digite um codigo numerico: "))
    nome = input("digite um nome: ")
    quantidade = int(input("digite quantidade: "))

    prod = Product(codigo, nome, quantidade)    
    theStore[codigo] = prod

def entrada():
    product = getProduct()
    if product:
        quantidade = int(input("digite quantidade a adicionar: "))
        product.quantidade += quantidade


def saida():
    product = getProduct()
    if product:
        quantidade = int(input("digite quantidade a sair: "))
        while product.quantidade - quantidade < 0:
            quantidade = int(input("digite quantidade a sair: "))
        product.quantidade -= quantidade


def verificarSaldo():
    product = getProduct()
    if product:
        print(product)

def imprimirProduto():
    print("\nPRODUTOS:")
    for x in theStore:
        print(f"{theStore[x]}")

theStore = dict()
def main():
    option = 0
    while option != -1:
        menu()
        option = int(input("digite sua opcao: "))

        if option == 0:
            novoProduto() 
        elif option == 3:
            verificarSaldo()
        elif option == 4:
            imprimirProduto()
        elif option == 1:
            entrada()
        elif option == 2:
            saida()

if __name__ == "__main__":
    main()

