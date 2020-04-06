'''
Cria um método e expõe ele ao cliente para que ele possa criar objetos
Necessário quando se necessita criar o mesmo objeto várias vezes durante o codigo
'''
from abc import abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#Classe abstrada para criação de um perfil 
class Perfil(Pessoa):    
    @abstractmethod
    def CriarPerfil(self):
        pass

#Classe Perfil pode ser utilizada para criação de um perfil mais complexo
class PerfilFacebook(Perfil):
    def CriarPerfil(self):
        print('Perfil do facebook criado')

class PerfilTwitter(Perfil):
    def CriarPerfil(self):
        print('Perfil do Twitter criado')
    

def main():
    #Listas para armazenar os perfis criados
    lista_perfil_facebook = []
    lista_perfil_twitter = []

    #Criando um perfil do tipo facebook e adicionando na lista
    perfilp1 = PerfilFacebook('Ana', 32)
    perfilp1.CriarPerfil()
    lista_perfil_facebook.append(perfilp1)

    perfilp3 = PerfilFacebook('Felipe', 30)
    perfilp3.CriarPerfil()
    lista_perfil_facebook.append(perfilp3)

    #Criando um perfil do tipo Twitter e adicionando na lista
    perfilp2 = PerfilTwitter('José', 20)
    perfilp2.CriarPerfil()
    lista_perfil_twitter.append(perfilp2)

    print('Lista de pessoas no facebook:')
    for pessoa in lista_perfil_facebook:
        print(pessoa.nome, pessoa.idade)

    print('Lista de pessoas no Twitter:')
    for pessoa in lista_perfil_twitter:
        print(pessoa.nome, pessoa.idade)

if __name__ == '__main__':
    main()