# Listagem Segura de Diretórios em Python

Este projeto demonstra uma vulnerabilidade comum de segurança em Python — a injeção de comandos — e como mitigá-la utilizando práticas seguras ao trabalhar com entrada de dados do usuário e comandos do sistema.

## Problema

Quando utilizamos `os.system()` ou funções semelhantes que executam comandos do sistema em Python, o tratamento inadequado da entrada do usuário pode levar à **injeção de comandos**, permitindo que um atacante execute comandos arbitrários no sistema.

### Exemplo de Código Vulnerável:
- `codigo_vulneravel.py`: Sem segurança

### Exemplo de Entrada Maliciosa:
Se o usuário inserir:
; del C:\important_file.txt

O comando executado será:
dir C:\tmp\; del C:\important_file.txt

Isso pode deletar arquivos importantes ou realizar outras ações perigosas, dependendo das permissões do usuário.