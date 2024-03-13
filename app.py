import os 

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')
print('Eu quero testar o git')

# Por padrão o python salva o input como uma String

opcao_escolhida = int (input ('Escolha uma opção: '))   
#opcao_escolhida = int (opcao_escolhida)

def finalizar_app():
    os.system('cls')
    # os.system('clear') - Caso do MacOs
    print('Finalizando o app\n')




if opcao_escolhida == 1: 
    print('Cadastre seu restaurante')
elif opcao_escolhida == 2: 
    print('Listar restaurante')
elif opcao_escolhida == 3: 
    print('Ativa restaurante')
else: 
    finalizar_app()