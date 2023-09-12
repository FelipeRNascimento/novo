class Classe_de_Aula():

    nomes_cursos = []
    nomes_alunos = []
    def cursos(self):
        turmas = (input('Deseja inserir um novo curso a lista?\n S/N: ')).upper()
        self.nomes_cursos
        while True:
            if turmas in 'S':
                nova_turma = input('Qual turma deseja adicionar? ')
                nomes_cursos.append(nova_turma)
                turmas = (input('Deseja inserir uma nova turma a lista?\n S/N: ')).upper()
            else:
                break
        return print(f'As turmas disponíveis são:{+self.nomes_cursos}')


    def identificado(self):
        alunos = (input('Deseja inserir um novo nome a lista? \n S/N: ')).upper()
        self.nomes_alunos

        while True:
            if alunos in 'S':
                novo_nome = input('Qual nome deseja adicionar? ')
                nomes_alunos.append(novo_nome)
                alunos = input('Deseja inserir um novo nome a lista. S/N: ').upper()
            else:
                break

        return print(f'Os alunos disponíveis são {self.nomes_alunos}')



v_identificado = Classe_de_Aula()
v_cursos = Classe_de_Aula()


v_identificado.identificado()
print()
v_cursos.cursos()


print("o aluno" +Classe_de_Aula.nomes_alunos[0]+ "faz o curso: "+Classe_de_Aula.nomes_turmas[1])