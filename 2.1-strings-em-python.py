# -----------------------------------------------
# 1) CRIAÇÃO DE STRINGS
# -----------------------------------------------

# Strings, são textos em python
# Podem ser criadass usando aspas simples ou duplas

texto1 ="Python"
texto2 = 'Curso de Python'
texto3 = "Copa'padrao fifa'"
texto4 = 'Copa "padrão fifa"'

print(texto1, texto2, texto3, texto4)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

# -----------------------------------------------
# 2) STRINGS MULTILINHA
# -----------------------------------------------

# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\
Uso: programa [OPÇÕES]
-h Exibe Ajuda
-U Url do Dataset
"""
print(menu)

# Esse formato é muito usado para:
# - Menus
# - documentação
# - textos longos

# -----------------------------------------------
# 3) CONCATENAÇÃO AUTOMÁTICA
# -----------------------------------------------
# Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto = ("Copa " "2026 " "Neymar é show mesmo?")
print(texto)

# -----------------------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
# -----------------------------------------------
# Uma string funciona como uma sequência de caracteres, cada caractere possui um indice

st = "maracana"
print("Primeira Letra:", st[0])
# só exibir a letra: m

print("ultima letra: ", st[-1])

print("Trecho 1:4:", st[1:4])

print("Do ínicio até 3:", st[:3])

print("Do 2 até o fim:", st[2:])

print("Tamanho", len(st))

