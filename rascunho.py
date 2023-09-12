class Classe_de_Aula():

    def cursos(self):
        turmas = (input('Deseja inserir um novo curso a lista?\n S/N: ')).upper()
        nomes = []

        while True:
            if turmas in 'S':
                nova_turma = input('Qual turma deseja adicionar? ')
                nomes.append(nova_turma)
                turmas = (input('Deseja inserir uma nova turma a lista?\n S/N: ')).upper()
            else:
                break
        return print(nomes)



cl = Classe_de_Aula()
cl.cursos()