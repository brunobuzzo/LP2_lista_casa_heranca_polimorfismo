class Aluno():


    def __init__(self, nome, curso, tempo_sem_dormir):
        self.nome = nome
        self.curso = curso
        self.tempo_sem_dormir = tempo_sem_dormir

    def estudar(self, horas_estudo):
        self.tempo_sem_dormir = self.tempo_sem_dormir + horas_estudo
        return None

    def dormir(self, horas_de_sono):
        if self.tempo_sem_dormir < horas_de_sono:
            self.tempo_sem_dormir = 0
        else:
            self.tempo_sem_dormir = self.tempo_sem_dormir - horas_de_sono
        return horas_de_sono


if __name__ == '__main__':

    nome = input('Infome o seu nome: ')
    curso = input('Informe o seu curso: ')
    tempo_sem_dormir = int(input('Quantas horas sem dormir? '))

    aluno1 = Aluno(nome, curso, tempo_sem_dormir)

    print('O ', aluno1.nome, ' esta à ',aluno1.tempo_sem_dormir, ' horas sem dormir')


    aluno1.dormir(11)
    

    aluno1.estudar(13)

    print('O ', aluno1.nome, ' esta à ',aluno1.tempo_sem_dormir, ' horas sem dormir')









