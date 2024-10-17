import os

def funcao_nao_segura():
    os.system("dir C:\\tmp\\{}".format(input_usuario))

input_usuario = input("Digite um diretório: ")
funcao_nao_segura()


"""
Entrada esperada: dir C:\tmp\exemplo

O usuário pode digitar "exemplo" como entrada, o que fará o comando ser executado assim:

bash
Copy code
dir C:\tmp\exemplo
Esse comando listará os arquivos e diretórios dentro de C:\tmp\exemplo.

Outra entrada válida seria arquivos, que resultaria no comando:

bash
Copy code
dir C:\tmp\arquivos
Entradas inesperadas ou perigosas:
Entrada maliciosa: Se o usuário tentar injetar comandos, como:
bash
Copy code
; del C:\important_file.txt
O comando executado será:
bash
Copy code
dir C:\tmp\; del C:\important_file.txt
Isso pode deletar arquivos importantes do sistema, dependendo das permissões, porque o ; permite encadear comandos no Windows da mesma forma que no Linux.


"""