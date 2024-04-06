from professor import Professor
from aluno import Aluno
from sala import Sala
from reserva import Reserva

class Menu:
    def __init__(self) -> None:
        self.imprimir_principal()
        self.opcao_principal(int(input()))
    
    def cadastrar_aluno(self):
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite a idade do aluno: '))
        pronome = input('Digite o pronome: ')
        turma = input('Digite a turma: ')

        novo_aluno = Aluno(
            nome,
            idade,
            pronome,
            turma
        )
        print('Aluno cadastrado com sucesso.')
        return novo_aluno
        
    def cadastrar_professor(self):
        nome = input('Digite o nome do professor: ')
        idade = int(input('Digite a idade do professor: '))
        pronome = input('Digite o pronome do professor: ')
        componente = input('Digite o componente: ')
        salario = input('Digite o salário: ')
        formacao = input('Digite a formacao: ')
    
        novo_professor = Professor(
            nome,
            idade,
            pronome,
            componente,
            salario,
            formacao
        )
        
        print('Professor cadastrado com sucesso.')
        return novo_professor

    def cadastrar_sala(self):
        descricao = input('Digite uma descrição: ')
        capacidade = input('Informe a capacidade: ')
    
        nova_sala = Sala(
            descricao,
            capacidade
        )
        print('Sala cadastrada com sucesso.')
        return nova_sala
    
    def reservar_sala(self, professor, sala):
        print(f'{sala} reservada para professor {professor}.')


main = Menu()
