'''*---------------------------------------------------------*"
                * Fatec São Caetano do Sul *
                    * Atividade B2-2 *
        * Autor: 1681432612026 - Luiza Lima Cremonezi*
* Objetivo:Realizar filas de impressão com filtro de prioridade*
                   * Data: 28/04/2026 *
*---------------------------------------------------------*'''

aluno = []
adm = []
reorganizada = []

def adicionar():
    tipo = input("Tipo do(ALUNO ou ADM): ").upper()
    nome = input("Nome do arquivo: ")
    paginas = int(input("Total de páginas: "))
   

    if tipo not in ["ALUNO", "ADM"]:
        print("Use ADM ou ALUNO.")
        return

    item = {
        "nome": nome,
        "paginas": paginas,
        "tipo": tipo
    }

    if tipo == "ADM":
        adm.append(item)
    else:
        aluno.append(item)

    print(f"Arquivo adicionado na fila {tipo}!")

def reorganizar():
    global reorganizada

    if reorganizada:
        print("Espere os arquivos da fila reorganizada serem consumidos.")
        return

    reorganizada.extend(adm)
    reorganizada.extend(aluno)

    adm.clear()
    aluno.clear()

    print("Fila de impressão reorganizad")

def listar():
    print("\n*- FILA ADM -*")
    if adm:
        for item in adm:
            print(f"{item['nome']} * {item['paginas']} páginas * {item['tipo']}")
    else:
        print("Nenhum arquivo")

    print("\n*- ALUNO -*")
    if aluno:
        for item in aluno:
            print(f"{item['nome']} * {item['paginas']} páginas * {item['tipo']}")
    else:
        print("Nenhum arquivo")

    print("\n*- FILA FINAL -*")
    if reorganizada:
        for item in reorganizada:
            print(f"{item['nome']} * {item['paginas']} páginas * {item['tipo']}")
    else:
        print("Nenhum arquivo")

def consumir():
    if not fila_final:
        print("Reorganize primeiro.")
        return

    atual = fila_final.pop(0)

    print("\nImprimindo/...\n")
    print(f"Arquivo: {atual['nome']}")
    print(f"Páginas: {atual['paginas']}")
    print(f"Tipo: {atual['tipo']}")
    print("\nImpressão concluída!\n")


while True:
    print("\n*-- MENU --*")
    print("1 * adicinar arquivo")
    print("2 * reorganizar filas")
    print("3 * listar fils")
    print("4 * consumir")
    print("0 * exit")

    op = input("digite a opçao: ")

    if op == "1":
        adicionar()

    elif op == "2":
        reorganizar()

    elif op == "3":
        listar()

    elif op == "4":
        consumir()

    elif op == "0":
        print("encerrando...")
        break

    else:
        print("não existente!")