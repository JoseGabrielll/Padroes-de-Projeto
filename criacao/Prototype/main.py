import copy

class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
def main():
    perfil_original = Perfil('Gabriel', 23) #Criando o objeto original
    perfil_clone = copy.deepcopy(perfil_original)
    perfil_clone2 = copy.copy(perfil_original)

    print(perfil_original.nome, perfil_original.idade)
    print(perfil_clone.nome, perfil_clone.idade)
    print(perfil_clone2.nome, perfil_clone2.idade)


if __name__ == '__main__':
    main()
