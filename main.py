from password_manager import *


password_file = 'data/passwords.json'

def main():
    validador = True
    
    while validador:
        passwords = load_data(password_file)
        
        print('Selecione uma opção:')
        print('[1] Salvar nova senha')
        print('[2] Deletar senha existente')
        print('[3] Alterar senha existente')
        print('[4] Sair')

        opcao = input('Digite o número da opção desejada: ')

        if opcao == '1':
            add_entry(passwords)  
            save_data(passwords, password_file)
            print('Dados salvos com sucesso!')

        elif opcao == '2':
            delete_entry(passwords)  
            save_data(passwords, password_file)

        elif opcao == '3':
            site_to_edit = input('Digite o site que deseja alterar: ')
            change_info(passwords, site_to_edit)  
            save_data(passwords, password_file)

        elif opcao == '4':
            validador = False  

        else:
            print('Opção inválida, tente novamente.')

        
        if validador:
            continuar = input('Deseja continuar? [S]im / [N]ão: ').upper()
            if continuar == 'N':
                validador = False

if __name__ == '__main__':
    try:
        main()
    except json.decoder.JSONDecodeError:
        print('Arquivo criptografado, descriptografe usando sua chave gerada')
        print('Para duvidas leia o README.md')
