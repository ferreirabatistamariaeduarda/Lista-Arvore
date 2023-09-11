class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)

    def caminho_ate_no(self, valor_alvo):
        caminho = []

        def encontrar_caminho(no, valor_alvo):
            if no is None:
                return False

            caminho.append(no.valor)

            if no.valor == valor_alvo:
                return True

            if (encontrar_caminho(no.esquerda, valor_alvo) or encontrar_caminho(no.direita, valor_alvo)):
                return True

            caminho.pop()
            return False

        encontrado = encontrar_caminho(self.raiz, valor_alvo)

        if encontrado:
            return caminho
        else:
            return []

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

valor_alvo = int(input("Digite o valor alvo: "))

caminho = arvore.caminho_ate_no(valor_alvo)

if caminho:
    print(f'Caminho até o nó {valor_alvo}: {caminho}')
else:
    print(f'O nó {valor_alvo} não foi encontrado na árvore.')
