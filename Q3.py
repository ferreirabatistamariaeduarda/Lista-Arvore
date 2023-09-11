#3. Implemente um método na classe `Arvore` que verifica se um valor está presente na árvore.

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

    def busca(self, chave):
        valor = self.raiz
        while valor is not None and valor.valor != chave:
            if chave < valor.valor:
                valor = valor.esquerda
            else:
                valor = valor.direita
        return valor


arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)
buscarNum = int(input("Digite o número a ser procurado: "))
no_encontrado = arvore.busca(buscarNum)

if no_encontrado is not None:
    print(f"Nó {buscarNum} encontrado na árvore.")
else:
    print(f"Nó {buscarNum} não encontrado na árvore.")