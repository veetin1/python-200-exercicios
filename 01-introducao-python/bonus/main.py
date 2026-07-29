from datetime import date #Biblioteca utilizada para obter o ano atual

def saudacao():
    print('Olá, Mundo!')

def input_name():
    nome = input('Qual o seu nome?')
    print('Seu nome é:', nome)

def indentacao():
    numero = 10
    if numero >= 10:
        saudacao()
    else:
        print('NUMERO MUITO GRANDE!')

def somar():
    a = int(input('Digite um numero:'))
    b = int(input('Digite outro numero:'))
    soma = a + b
    print(soma)

def calculo_idade():
    ano_nascimento = int(input('Digite o ano de nascimento:'))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print('Sua idade é:', idade)

if __name__ == '__main__':
    saudacao()
    input_name()
    indentacao()
    somar()
    calculo_idade()