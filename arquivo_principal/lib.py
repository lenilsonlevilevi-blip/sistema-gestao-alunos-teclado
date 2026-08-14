def coletar_dados_do_aluno():
    
        nome = str(input('Digite o nome do aluno: '))
        dia_da_aula = str(input('Digite o dia da aula: '))
        horario = int(input('Digite o horario da aula: '))

        return{
        'nome':nome,
        'aula': dia_da_aula,
        'horario': horario
        }

       

def cadastrar_aluno(lista):
    while True:
        novo_aluno = coletar_dados_do_aluno()
        lista.append(novo_aluno)
    
        continuar = str(input('Deseja Continuar [S/N]: ')).upper().strip()
        
        if continuar == 'N':
            break
        
def listar_aluno(lista):      
    print('\n---ALUNOS CADASTRADOS---')    
    for aluno in lista:      
        print(f'Nome: {aluno["nome"]}')
        print(f'Aula: {aluno["aula"]}')
        print(f'Horário: {aluno["horario"]}h')
        print('-'*25)
        
   

    
