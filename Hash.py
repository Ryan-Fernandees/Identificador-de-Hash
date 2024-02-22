import os
import hashlib

def calcular_hash_arquivo(nome_arquivo, algoritmo='sha256'):
    hash_alg = hashlib.new(algoritmo)

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

    with open(caminho_arquivo, 'rb') as f:
        while True:
            bloco = f.read(4096)
            if not bloco:
                break
            hash_alg.update(bloco)

    # Retorna o hash em formato hexadecimal
    return hash_alg.hexdigest()

# Nome do arquivo que você deseja calcular o hash.
# Importante que o arquivo esteja na mesma pasta do projeto
nome_arquivo = 'teste.txt'

hash_resultante = calcular_hash_arquivo(nome_arquivo)

print("Hash do arquivo é:", hash_resultante)
