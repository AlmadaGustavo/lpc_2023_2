import random
import string

objetivo = ''
tamanho_obj = 0
letras = string.ascii_uppercase + ' ' + string.punctuation
geracoes = 100
populacao = 100
geracoes_total = []

melhor_string = {
    'string': '',
    'pontuacao': 0,
    'base_para_nova_geracao': ''
}


def string_aleatoria(tamanho_obj2):
    return ''.join(random.choice(letras) for _ in range(tamanho_obj2))


def criar_string_inicial():
    geracoes_total.append([string_aleatoria(tamanho_obj) for _ in range(populacao)])


def nova_geracao(melhor):
    nova_geracao = ''
    for i in range(tamanho_obj):
        if objetivo[i] == melhor[i]:
            nova_geracao += melhor[i]
        else:
            nova_geracao += '*'
    melhor_string['base_para_nova_geracao'] = nova_geracao


def trocar_caracteres(string, index, char):
    return string[:index] + char + string[index + 1:]


def substituir_letras_sem_correspondencia():
    tempo_string = melhor_string['base_para_nova_geracao']
    for i, letra in enumerate(tempo_string):
        if letra == '*':
            tempo_string = trocar_caracteres(tempo_string, i, random.choice(letras))
    return tempo_string


def criar_nova_geracao():
    nova_geracao(melhor_string['string'])
    geracoes_total.append([substituir_letras_sem_correspondencia() for _ in range(populacao)])


def pontuacao_string(string):
    pontuacao = 0
    for i in range(tamanho_obj):
        if objetivo[i] == string[i]:
            pontuacao += 1
    return pontuacao


def att_melhor_string(string, pontuacao):
    melhor_string['string'] = string
    melhor_string['pontuacao'] = pontuacao


def checar_combinacoes():
    ultima_geracao = geracoes_total[-1]
    for string in ultima_geracao:
        pontuacao = pontuacao_string(string)
        if pontuacao > melhor_string['pontuacao']:
            att_melhor_string(string, pontuacao)


def printar_melhor_string():
    print('Geração ' + str(len(geracoes_total)))
    print('Melhor combinação atual ' + melhor_string['string'])


def macaco(objetivo2):
    global objetivo
    objetivo = objetivo2
    global tamanho_obj
    tamanho_obj = len(objetivo2)
    criar_string_inicial()
    checar_combinacoes()
    printar_melhor_string()
    for _ in range(geracoes):
        if melhor_string['string'] == objetivo:
            print('Script completado. Feito em ' + str(len(geracoes_total)) + ' gerações')
            return ''
        criar_nova_geracao()
        checar_combinacoes()
        printar_melhor_string()


if __name__ == '__main__':
    macaco(input('Insira a frase alvo para o macaco digitar: ').upper())
