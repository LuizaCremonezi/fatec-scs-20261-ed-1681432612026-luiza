'''*---------------------------------------------------------*"
                * Fatec São Caetano do Sul *
                    * Atividade B2-3 *
        * Autor: 1681432612026 - Luiza Lima Cremonezi*
* Objetivo:Realizar ávore binária e suas funções respectivas*
                   * Data: 12/05/2026 *
*---------------------------------------------------------*'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    # inserir na arvore
    def inserir(self, valor):

        novoNo = No(valor)

        if self.raiz == None:
            self.raiz = novoNo
            return

        at = self.raiz

        while True:

            if valor < at.valor:

                if at.esq == None:
                    at.esq = novoNo
                    break

                at = at.esq

            else:

                if at.dir == None:
                    at.dir = novoNo
                    break

                at = at.dir

    # buscar um no
    def buscar(self, no, valor):

        if no == None:
            return None

        if no.valor == valor:
            return no

        if valor < no.valor:
            return self.buscar(no.esq, valor)

        else:
            return self.buscar(no.dir, valor)

    # mostrar nos internos
    def imprimir_nos_internos(self):

        print("\nNos internos:")
        self._internos(self.raiz)

    def _internos(self, no):

        if no != None:

            if no.esq != None or no.dir != None:
                print(no.valor)

            self._internos(no.esq)
            self._internos(no.dir)

    # mostrar folhas
    def imprimir_folhas(self):

        print("\nFolhas:")
        self._folhas(self.raiz)

    def _folhas(self, no):

        if no != None:

            if no.esq == None and no.dir == None:
                print(no.valor)

            self._folhas(no.esq)
            self._folhas(no.dir)

    # imprimir por niveis
    def imprimir_niveis(self):

        if self.raiz == None:
            return

        fila = [(self.raiz, 0)]

        nivAt = 0

        print("\nArvore por niveis:")

        while len(fila) > 0:

            no, niv = fila.pop(0)

            if niv != nivAt:
                print()
                nivAt = niv

            print(f"Nivel {niv}: {no.valor}")

            if no.esq:
                fila.append((no.esq, niv + 1))

            if no.dir:
                fila.append((no.dir, niv + 1))

    # calcular altura
    def calcular_altura(self, no):

        if no == None:
            return -1

        altEsq = self.calcular_altura(no.esq)
        altDir = self.calcular_altura(no.dir)

        if altEsq > altDir:
            return altEsq + 1

        else:
            return altDir + 1

    # profundidade do no
    def calcular_profundidade(self, valor):

        return self._prof(self.raiz, valor, 0)

    def _prof(self, no, valor, prof):

        if no == None:
            return -1

        if no.valor == valor:
            return prof

        if valor < no.valor:
            return self._prof(no.esq, valor, prof + 1)

        else:
            return self._prof(no.dir, valor, prof + 1)

    # ancestrais
    def imprimir_ancestrais(self, valor):

        print(f"\nAncestrais do no {valor}:")

        lst = []

        self._ancestrais(self.raiz, valor, lst)

        for x in lst:
            print(x)

    def _ancestrais(self, no, valor, lst):

        if no == None:
            return False

        if no.valor == valor:
            return True

        achou = self._ancestrais(no.esq, valor, lst)

        if achou == False:
            achou = self._ancestrais(no.dir, valor, lst)

        if achou:
            lst.append(no.valor)
            return True

        return False

    # descendentes
    def imprimir_descendentes(self, valor):

        no = self.buscar(self.raiz, valor)

        if no == None:
            print("No nao encontrado")
            return

        print(f"\nDescendentes do no {valor}:")

        self._desc(no.esq)
        self._desc(no.dir)

    def _desc(self, no):

        if no != None:

            print(no.valor)

            self._desc(no.esq)
            self._desc(no.dir)

    # grau do no
    def grau_no(self, valor):

        no = self.buscar(self.raiz, valor)

        if no == None:
            return -1

        grau = 0

        if no.esq != None:
            grau += 1

        if no.dir != None:
            grau += 1

        return grau

    # analisar arvore
    def analisar_arvore(self, valorBusca):

        print("\n===== DIAGNOSTICO DA ARVORE =====")

        if self.raiz != None:
            print(f"\nRaiz: {self.raiz.valor}")

        self.imprimir_nos_internos()

        self.imprimir_folhas()

        self.imprimir_niveis()

        print("\n===== ANALISE DO NO =====")

        no = self.buscar(self.raiz, valorBusca)

        if no == None:
            print("Valor nao encontrado")
            return

        print(f"\nNo analisado: {valorBusca}")

        print("Grau do no:", self.grau_no(valorBusca))

        print("Profundidade:", self.calcular_profundidade(valorBusca))

        print("Altura:", self.calcular_altura(no))

        self.imprimir_ancestrais(valorBusca)

        self.imprimir_descendentes(valorBusca)
