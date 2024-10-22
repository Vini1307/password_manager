import json
from os.path import isfile

# Função para salvar dados no json
def save_data(passwords, file):
    with open(file, 'w', encoding='utf-8') as data:
        json.dump(passwords, data, indent=2, separators=(',' ,': '), sort_keys=False)
        
    
def load_data(file):
    if isfile(file):
        with open(file, 'r', encoding='utf-8') as data:
            return json.load(data)
    else:
        temporario = []
        return temporario
    
def add_entry(passwords):
  
    site_data = input('Digite o site a ser salvo: ')
    url_link = input('Cole a url do site aqui: ')
    mail_data = input('Digite o seu email: ')
    user_data = input('Digite o usuario a ser salvo: ')
    password_data = input('Digite a senha a ser salva: ')

    # Cria um novo dicionario
    if site_data.strip() != '':
        if url_link.strip() != '':
            if mail_data.strip() != '':
                if user_data.strip() != '':
                    if password_data.strip() != '':
                        new_dic = {
                            'site': site_data,
                            'url': url_link,
                            'email':  mail_data,
                            'user': user_data,
                            'password': password_data
                        }
                        passwords.append(new_dic)
                    else:
                        print('Digite uma senha valida!')
                else:
                    print('Digite um usuario valido!')
            else: 
                print('Digite um email valido')
        else:
            print('Digite uma ULR valida!')
    else:
        print('Digite um site valido')
        
    print('Dados salvos com sucesso!')
    
    print()
    print()
    
def change_info(passwords, site_to_edit):
    change_info = input('O que você quer alterar ? \n[E]mail [S]enha [U]ser: ').upper()
    
    if change_info == 'S':
            for entry in passwords:
                if entry['site'] == site_to_edit:
                    new_password = input('Digite a sua nova senha: ')
                    entry['password'] = new_password
                    print(f'Senha do site "{site_to_edit}" foi alterada com sucesso!')
                    return passwords
            
        
    elif change_info == 'E':
        for entry in passwords:
            if entry['site'] == site_to_edit:
                new_mail = input('Digite o seu novo email: ')
                entry['email'] = new_mail
                print(f'Email do site {site_to_edit} foi alterado com sucesso!')
                return passwords

       
    elif change_info == 'U':
        for entry in passwords:
            if entry['site'] == site_to_edit:
                new_user = input('Digite o seu novo usuário: ')
                entry['user'] = new_user
                print(f'Usuário do site {site_to_edit} foi alterado com sucesso!')
                return passwords
        
    else:
        print('Opção inválida! Tente novamente.')
        return passwords
    print(f'Site {site_to_edit} não encontrado.')
    
    

def delete_entry(passwords):
    all_sites = []
    
    for entry in passwords:
        all_sites.append(entry['site'])
        
    print('Sites salvos: ')
    
    for site in all_sites:
        print(site)  
        
    print()
    site_to_remove = input('Digite o site a ser removido: ')
    
    for i, entry in enumerate(passwords):
        if entry['site'] == site_to_remove:
            del passwords[i]
            print(f'Dados do site {site_to_remove} foram removidos')
            break
    else:
        print(f'{site_to_remove} não existe')
        print()
    
    save_data(passwords,  'data/passwords.json')
        

    
        
   
