#Escreva uma função que verifica se uma árvore binária é uma árvore de busca válida.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.valores = []

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

    def in_order_traversal(self, no):
        if no is None:
            return
        self.in_order_traversal(no.esquerda)
        self.valores.append(no.valor)
        self.in_order_traversal(no.direita)

    def arvore_busca_valida(self):
        self.valores = []
        self.in_order_traversal(self.raiz)
        for i in range(1, len(self.valores)):
            if self.valores[i] <= self.valores[i - 1]:
                return False

        return True

arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

if arvore.arvore_busca_valida():
    print("É uma árvore de busca binária válida.")
else:
    print("Não é uma árvore de busca binária válida.")


