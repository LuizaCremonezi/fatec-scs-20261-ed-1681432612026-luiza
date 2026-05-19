'''*---------------------------------------------------------*"
                * Fatec São Caetano do Sul *
                    * Atividade B2-3 *
        * Autor: 1681432612026 - Luiza Lima Cremonezi*
* Objetivo:Realizar ávore binária e suas funções respectivas*
                   * Data: 12/05/2026 *
*---------------------------------------------------------*'''

# analisar arvore
def analisar_arvore(self, valor_busca):

    print("\n===== DIAGNOSTICO DA ARVORE =====")

    if self.raiz != None:
        print(f"\nRaiz: {self.raiz.valor}")

    self.imprimir_nos_internos()

    self.imprimir_folhas()

    self.imprimir_niveis()

    no = self.buscar(self.raiz, valor_busca)

    if no == None:
        print("\nValor nao encontrado")
        return

    print(f"\nNo analisado: {valor_busca}")

    print("Altura:", self.calcular_altura(no))

    print("Profundidade:", self.calcular_profundidade(valor_busca))

    self.imprimir_ancestrais(valor_busca)

    self.imprimir_descendentes(valor_busca)


# nos internos
def imprimir_nos_internos(self):

    print("\nNos internos:")

    self._internos(self.raiz)

def _internos(self, no):

    if no != None:

        if no.esq != None or no.dir != None:
            print(no.valor)

        self._internos(no.esq)
        self._internos(no.dir)


# folhas
def imprimir_folhas(self):

    print("\nFolhas:")

    self._folhas(self.raiz)

def _folhas(self, no):

    if no != None:

        if no.esq == None and no.dir == None:
            print(no.valor)

        self._folhas(no.esq)
        self._folhas(no.dir)


# imprimir niveis
def imprimir_niveis(self):

    if self.raiz == None:
        return

    fila = [(self.raiz, 0)]

    niv_at = 0

    print("\nArvore por niveis:")

    while len(fila) > 0:

        no, niv = fila.pop(0)

        if niv != niv_at:
            print()
            niv_at = niv

        print(f"Nivel {niv}: {no.valor}")

        if no.esq != None:
            fila.append((no.esq, niv + 1))

        if no.dir != None:
            fila.append((no.dir, niv + 1))


# altura
def calcular_altura(self, no):

    if no == None:
        return -1

    alt_esq = self.calcular_altura(no.esq)

    alt_dir = self.calcular_altura(no.dir)

    if alt_esq > alt_dir:
        return alt_esq + 1

    return alt_dir + 1


# profundidade
def calcular_profundidade(self, valor):

    return self._prof(self.raiz, valor, 0)

def _prof(self, no, valor, prof):

    if no == None:
        return -1

    if no.valor == valor:
        return prof

    if valor < no.valor:
        return self._prof(no.esq, valor, prof + 1)

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
