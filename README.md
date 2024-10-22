# Gerenciador de Senhas

Este é um gerenciador de senhas simples que permite aos usuários armazenar, editar e excluir informações sobre sites, usuários e senhas. O projeto utiliza criptografia para garantir que os dados sejam mantidos em segurança.

## Funcionalidades

- **Adicionar Senhas:** Salve informações sobre sites, URLs, usuários e senhas.
- **Deletar Senhas:** Remova entradas de senhas existentes.
- **Alterar Senhas:** Modifique informações de senhas, e-mails e usuários.
- **Armazenamento Seguro:** As informações são armazenadas em um arquivo JSON que é criptografado.
- **Autenticação por Senha:** O acesso aos dados é protegido por uma senha.

## Pré-requisitos

Para executar este projeto, você precisará ter o Python instalado em sua máquina. Além disso, será necessário instalar a biblioteca `cryptography`. Você pode fazer isso usando o seguinte comando:

```bash
pip install cryptography
```

# Estrutura de Diretórios

```bash
project/
│
├── data/
│   ├── passwords.json       # Arquivo onde as senhas são armazenadas
│   └── secret.key           # Chave de criptografia (não deve ser exposta publicamente)
│
├── utils.py                  # Código para encriptar e desencriptar JSON
├── password_manager.py       # Código principal do gerenciador de senhas
└── main.py                   # Arquivo de execução do programa
```

# Como usar

1. Executar o Programa: Para iniciar o gerenciador de senhas, execute o seguinte comando no terminal:

```bash
python main.py
```

2. Opções Disponíveis: Após iniciar o programa, você verá um menu com as seguintes opções:

* [1] Salvar nova senha

* [2] Deletar senha existente

* [3] Alterar senha existente

* [4] Sair


3. Adicionar Senhas: Escolha a opção de adicionar uma nova senha e forneça as informações solicitadas.


4. Deletar Senhas: Selecione a opção para deletar senhas e siga as instruções.


5. Alterar Senhas: Para alterar senhas existentes, escolha a opção correspondente e siga as instruções.


6 - Proteção por Senha: Ao iniciar o programa, você será solicitado a inserir uma senha para acessar as informações armazenadas.

## Como Gerar a Chave de Criptografia

Para garantir que apenas você tenha acesso às suas senhas criptografadas, é necessário gerar uma chave de criptografia. Você pode fazer isso com o seguinte comando Python:

```python
from cryptography.fernet import Fernet

# Gera uma nova chave
key = Fernet.generate_key()

# Salva a chave em um arquivo
with open("data/secret.key", "wb") as key_file:
    key_file.write(key)

print("Chave de criptografia gerada e salva em 'data/secret.key'")
```

# Instruções:
1. Execute o código acima em um arquivo Python separado (por exemplo, utils.py).

2. Verifique o diretório data/: a chave será salva no arquivo secret.key.

3. Mantenha a chave em segredo: Nunca compartilhe este arquivo em repositórios públicos ou com outras pessoas. Se alguém tiver acesso a esta chave, poderá descriptografar suas senhas.

OBS: codigo para encriptar de desencriptar o JSON esta no utils.py

# Segurança

Importante: Nunca compartilhe sua chave de criptografia (`secret.key`) ou suas senhas em um repositório público. Armazene essas informações em um local seguro.

# Contribuições

Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para abrir uma "issue" ou enviar um "pull request