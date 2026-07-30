#Filmes e series tem as seguintes características

#Filme: Nome, ano, duração, curtir
#Séries: Nome, ano, temporadas, curtir


#Classe mamãe, classe principal
#super classe!!!!!!
class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtir = 0

    @property
    def valor_curtir(self):
        return self._curtir
    
    @property
    def valor_nome(self):
        return self._nome
        
    def curtida(self):
        self._curtir += 1

class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f"{self.valor_nome} - {self.ano} - {self.duracao} Minutos - {self._curtir} Curtidas\n"

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.valor_nome} - {self.ano} - {self.temporadas} Temporadas - {self._curtir} Curtidas\n"

#Instanciar é salvar em uma variável

aventuras_superman = Series("Minhas Aventuras com Superman", 2023, 3)
aventuras_superman.curtida()

avatar = Filmes("Avatar", 2009, 177)




filmes_series = [aventuras_superman, avatar]

for programas in filmes_series:
    programas.imprime()
    















