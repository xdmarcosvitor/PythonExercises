from pessoa import Pessoa

class Aluno(Pessoa):
    
    def __init__(self, nome, idade, pronome, turma):
        super().__init__(nome, idade, pronome)

        self.turma = turma
        self.nota = 0
        self.frequencia = 0

    def estudar(self):
        return 'ta pago!'