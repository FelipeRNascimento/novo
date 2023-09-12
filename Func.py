alunos = (input('Deseja inserir um novo nome a lista? \n S/N: ')).upper()
nomes = []

while True:
    if alunos in 'S':
        novo_nome = input('Qual nome deseja adicionar? ')
        nomes.append(novo_nome)
        alunos = input('Deseja inserir um novo nome a lista. S/N: ').upper()
    else:
        break

print(nomes)
