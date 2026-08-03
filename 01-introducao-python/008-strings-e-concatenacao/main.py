def entrada_de_dados():
      nome = input('Digite seu nome: ')
      sobrenome = input('Digite seu sobrenome: ')

      contatena_nomes = str(nome + ' ' + sobrenome)

      print("Bem vindo!" + contatena_nomes + " aqui vc encontra conteudo de qualidade!")

if __name__ == '__main__':
    entrada_de_dados()