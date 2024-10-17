import os
import subprocess

def funcao_segura():
    # Verifica se o diretório existe antes de listar o conteúdo
    caminho = os.path.join("C:\\tmp", input_usuario) 
    if not os.path.isdir(caminho):
        print("Diretório inválido.")
        return

    # Utiliza subprocess para executar o comando de forma segura
    try:
        subprocess.run(["dir", caminho], shell=False, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar o diretório: {e}")

input_usuario = input("Digite um diretório: ")
funcao_segura()

