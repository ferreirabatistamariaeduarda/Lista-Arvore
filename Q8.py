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

    def travessia_em_niveis(self):
        if self.raiz is None:
            return []

        def _travessia_em_niveis(niveis, nivel_atual):
            proximo_nivel = []
            valores_nivel = []

            for no in nivel_atual:
                valores_nivel.append(no.valor)
                if no.esquerda:
                    proximo_nivel.append(no.esquerda)
                if no.direita:
                    proximo_nivel.append(no.direita)

            niveis.append(valores_nivel)

            if proximo_nivel:
                _travessia_em_niveis(niveis, proximo_nivel)

        niveis = []
        nivel_atual = [self.raiz]
        _travessia_em_niveis(niveis, nivel_atual)

        return niveis

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

resultados = arvore.travessia_em_niveis()

for nivel in resultados:
    print('Valores do nível:', nivel)
