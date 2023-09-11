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

    def encontrar_nos_filhos(self, no_pai):
        if no_pai is None:
            return []

        filhos = []

        if no_pai.esquerda:
            filhos.append(no_pai.esquerda)

        if no_pai.direita:
            filhos.append(no_pai.direita)

        return filhos

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

valor_alvo = int(input("Digite o valor do nó alvo: "))

def encontrar_no_por_valor(no_atual, valor_alvo):
    if no_atual is None:
        return None
    if no_atual.valor == valor_alvo:
        return no_atual
    if valor_alvo < no_atual.valor:
        return encontrar_no_por_valor(no_atual.esquerda, valor_alvo)
    return encontrar_no_por_valor(no_atual.direita, valor_alvo)

no_alvo = encontrar_no_por_valor(arvore.raiz, valor_alvo)

if no_alvo:
    filhos_do_no = arvore.encontrar_nos_filhos(no_alvo)

    if filhos_do_no:
        valores_dos_filhos = [no.valor for no in filhos_do_no]
        print(f'Nós filhos de {no_alvo.valor}: {valores_dos_filhos}')
    else:
        print(f'{no_alvo.valor} não tem nós filhos na árvore. Portanto, é uma folha')
else:
    print(f'O nó com valor {valor_alvo} não foi encontrado na árvore.')
