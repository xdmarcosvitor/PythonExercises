from aluno import Aluno
from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, pronome, componente, salario, formacao):
        super().__init__(nome, idade, pronome)

        self.componente = componente
        self.salario = salario
        self.formacao = formacao

    def atribuir_nota(self):
        pass

    def lancar_nota(self, aluno: Aluno, nota:float):
        if isinstance(aluno, aluno):
              aluno.nota = nota
        else:
              print('Erro:aluno não é Aluno')

