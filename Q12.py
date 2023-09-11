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

    def remover(self, valor):
        if self.raiz is None:
            return False
        self.raiz = self.remover_recursivo(self.raiz, valor)
        return True

    def remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self.remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda


            no.valor = self.encontrar_minimo_valor(no.direita)
            no.direita = self.remover_recursivo(no.direita, no.valor)

        return no


# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)
print('Árvore original:')
arvore.em_ordem(arvore.raiz)
print()
valor_remover = int(input('Digite o valor do nó que deseja remover: '))
removido = arvore.remover(valor_remover)
if removido:
    print(f'Árvore após a remoção do valor {valor_remover}:')
    arvore.em_ordem(arvore.raiz)
else:
    print(f'Valor {valor_remover} não encontrado na árvore.')
