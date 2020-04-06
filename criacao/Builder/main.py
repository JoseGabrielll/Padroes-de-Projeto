from grupo import PessoaFisica, PessoaJuridica
from criador_de_grupo import CriadorGrupos

def main():
    pessoa1 = PessoaFisica('Alex', 30)
    pessoa2 = PessoaFisica('Felipe', 28)
    pessoa3 = PessoaJuridica('Paula', 25)

    grupo1 = CriadorGrupos('Grupo Teste')
    grupo1.AdicionaPessoaFisica(pessoa1)
    grupo1.AdicionaPessoaJuridica(pessoa2)
    grupo1.AdicionaPessoaJuridica(pessoa3)


    grupo1.ImprimePessoas(grupo1.lista)
    #print(grupo1.lista[0].nome, grupo1.lista[0].cpf)
    

if __name__ == "__main__":
    main()