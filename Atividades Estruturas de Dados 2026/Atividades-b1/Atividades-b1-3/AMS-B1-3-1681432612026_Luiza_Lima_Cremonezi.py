
'''*---------------------------------------------------------*"
                * Fatec São Caetano do Sul *
                    * Atividade B1-3 *
        * Autor: 1681432612026 - Luiza Lima Cremonezi*
     * Objetivo: Usando pilhas em uma  Calculadora RPN *
                   * Data: 30/03/2026 *
*---------------------------------------------------------*'''

def eh_numero(valor):
    """Verifica se o valor informado pode ser convertido para um número válido."""
    try:
        float(valor)
        return True
    except ValueError:
        return False


def calculadora_rpn(expressao, mostrar_passos=False):
    pilha = []
    pilha_expr = []  

    
    elementos = expressao.split()

    for elemento in elementos:

        if eh_numero(elemento):
            pilha.append(float(elemento))
            pilha_expr.append(elemento)

 
        elif elemento in ['+', '-', '*', '/']:

          
            x = pilha.pop()
            y = pilha.pop()

         
            x_expr = pilha_expr.pop()
            y_expr = pilha_expr.pop()

         
            if elemento == '+':
                resultado = y + x
            elif elemento == '-':
                resultado = y - x
            elif elemento == '*':
                resultado = y * x
            elif elemento == '/':
                if x == 0:
                    raise ZeroDivisionError("Erro: não é possível dividir por zero.")
                resultado = y / x

           
            nova_expr = f"({y_expr} {elemento} {x_expr})"

            pilha.append(resultado)
            pilha_expr.append(nova_expr)

        else:
            raise ValueError(f"Erro: operador ou valor inválido -> '{elemento}'")

        if mostrar_passos:
            print(f"Passo com '{elemento}':")
            print("  Valores na pilha:", pilha)
            print("  Expressões geradas:", pilha_expr)
            print()

    if len(pilha) != 1:
        raise ValueError("Erro: a expressão RPN informada é inválida.")

    return pilha[0], pilha_expr[0]


print("=== Calculadora de Notação Polonesa Reversa (RPN) ===")
print("Exemplo de uso: 5 5 + 2 *")
print("Digite 'sair' para finalizar o programa.\n")

while True:
    expressao = input("Informe a expressão RPN: ")

    if expressao.lower() == "sair":
        print("Programa finalizado com sucesso.")
        break

    try:
        resultado, expr = calculadora_rpn(expressao, mostrar_passos=True)
        print(f"Resultado obtido: {resultado}")
        print(f"Forma algébrica equivalente: {expr}\n")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}\n")