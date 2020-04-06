from abc import abstractmethod

class Tema(object):
    @abstractmethod
    def cor(self):
        pass

class TemaEscuro(Tema):
    def cor(self): #aqui seriam configurados as propriedades do tema
        return 'Tema escuro'

class TemaClaro(Tema):
    def cor(self):
        return 'Tema claro'

class PaginaWeb(object):
    def __init__(self, tema):
        self.tema = tema
    
    def conteudo_pag(self):
        print('O tema da pagina é: ', self.tema.cor())

def main():

    tema_escuro = TemaEscuro()
    tema_claro = TemaClaro()

    pagina1 = PaginaWeb(tema_escuro)
    pagina2 = PaginaWeb(tema_claro)

    pagina1.conteudo_pag()
    pagina2.conteudo_pag()


if __name__ == '__main__':
    main()
        
