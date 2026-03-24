'''*---------------------------------------------------------*"
                * Fatec São Caetano do Sul *
                    * Atividade B1-1 *
        * Autor: 1681432612026 - Luiza Lima Cremonezi*
   * Objetivo:Fazer funcionalidades de um catálogo de filmes*
                   * Data: 24/02/2026 *
*---------------------------------------------------------*'''

catalogo = {}

def adicionar_filme ( id_filme , titulo , diretor ) :
 if id_filme in catalogo:
  print ("Id indisponível.")

 else: catalogo[id_filme] = {"titulo": titulo,"diretor": diretor}
 print("Filme adicionado!")

def buscar_filme ( id_filme ) :
   filme = catalogo.get(id_filme)

   if id_filme not in catalogo:
      print ("ID não cadastrado.")   

   else:
    print("Titulo:", filme["titulo"])
    print("Diretor:", filme["diretor"])

def remover_filme ( id_filme ) : 
  if id_filme in catalogo:
   catalogo.pop(id_filme)
   print("Filme removido!")
  else:
   print("ID não cadastrado.")

def listar_todos () :
  if not catalogo:
   print ("\nNão há filmes registrados.")
  else :
   print ("\n*|        Lista de Filmes         | *")
      
  for id_f , dados in catalogo . items () :
   print (f"ID: { id_f } | Titulo : { dados ['titulo']} | Diretor : { dados [ 'diretor' ]}")


adicionar_filme(1, "Rio", "Bob Iger")
adicionar_filme(2, "Enrolados", "Bob Iger")
adicionar_filme(3, "Branca de Neve", "Bob Iger")

listar_todos()

filme_encontrado = buscar_filme(2)
if filme_encontrado:
    print(f"\nFilme encontrado:  |  {filme_encontrado['titulo']}")

remover_filme(2)
listar_todos()