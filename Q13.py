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

    def nos_no_nivel(self, nivel_desejado):
        if self.raiz is None:
            return []

        nos_nivel = []
        fila = [(self.raiz, 0)]

        while fila:
            no, nivel_atual = fila.pop(0)

            if nivel_atual == nivel_desejado:
                nos_nivel.append(no.valor)

            if nivel_atual < nivel_desejado:
                if no.esquerda:
                    fila.append((no.esquerda, nivel_atual + 1))
                if no.direita:
                    fila.append((no.direita, nivel_atual + 1))

        return nos_nivel

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(1)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(6)

nivel_desejado = int(input("Digite o nível desejado: "))

nos_nivel = arvore.nos_no_nivel(nivel_desejado)
print(f"Nós no nível {nivel_desejado}: {nos_nivel}")
