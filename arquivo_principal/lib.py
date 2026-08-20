import json

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

        salvar_dados(lista)
    
        continuar = str(input('Deseja Continuar [S/N]: ')).upper().strip()
        
        if continuar == 'N':
            break

def excluir_aluno(lista):
     listar_aluno(lista)
     excluir = int(input('Deseja exluir qual aluno? '))
     lista.pop(excluir - 1)
     salvar_dados(lista)


        
def listar_aluno(lista):      
    print('\n---ALUNOS CADASTRADOS---')   
    for c, aluno in enumerate(lista, start=1):   
        print(f'[{c}] Nome: {aluno["nome"]}')
        print(f'Aula: {aluno["aula"]}')
        print(f'Horário: {aluno["horario"]}h')
        print('-'*25)
        
   
def salvar_dados(alunos):
     with open('alunos.json','w') as arquivo:
          # Abre/cria o arquivo "alunos.json".
          # 'w' significa "write" (escrita).
          # Se o arquivo não existir, ele será criado.
          # Se já existir, o conteúdo anterior será substituído.
          # "as arquivo" guarda o arquivo aberto na variável "arquivo".
          json.dump(alunos, arquivo, indent=4,ensure_ascii=False) # ensure_ascii - Não transforme os caracteres Unicode em códigos \uXXXX. Pode salvar os caracteres normalmente
          '''O QUE VOU SALVAR,
            ONDE VOU SALVAR,
            COMO VOU FORMATAR'''

def carregar_dados():
     try:
        with open('alunos.json','r') as arquivo:
            alunos = json.load(arquivo)
            return alunos
     except FileNotFoundError:
          return []
     
  
       