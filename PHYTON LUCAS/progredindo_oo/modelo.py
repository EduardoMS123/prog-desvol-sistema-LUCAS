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


#nomePL = Nome da Playlist
class Playlist():
    def __init__(self, nomePL, elementos):
        self.nomePL = nomePL
        self._elementos = elementos

    @property
    def  listagem(self):
        return self._elementos
        
    
    def __getitem__(self, item):
        return self._elementos[item]
    
    def __len__(self):
        return len(self._elementos)


#Instanciar é salvar em uma variável

#Series
aventuras_superman = Series("Minhas Aventuras com Superman", 2023, 3)
casa_coruja = Series("Casa da Coruja", 2020, 3)

#Filmes
avatar = Filmes("Avatar", 2009, 177)
chromaticaBall = Filmes("Chromatica Ball", 2024, 118)

#Curtidas
aventuras_superman.curtida()
avatar.curtida()
avatar.curtida()
avatar.curtida()
chromaticaBall.curtida()
chromaticaBall.curtida()
chromaticaBall.curtida()
chromaticaBall.curtida()
chromaticaBall.curtida()
chromaticaBall.curtida()
casa_coruja.curtida()
casa_coruja.curtida()
casa_coruja.curtida()
casa_coruja.curtida()
casa_coruja.curtida()
casa_coruja.curtida()


filmes_series = [avatar, chromaticaBall, aventuras_superman, casa_coruja]
plFim_de_semana = Playlist("Fim de Semana", filmes_series)

#print(f"Tamanho da Playlist: {plFim_de_semana}")
print(f"Está na lista?{avatar in plFim_de_semana}")
print(plFim_de_semana[1])

#for programas in plFim_de_semana:
   #print(programas)
    

#Python Data Model
#Inicialização: __init__
#Representação: __str__,__repr__
#Containers/Sequência: __contains__, __iter__,__len__,__getitem__
#Numéricas: __add__,__sub__,__mul__,__mod__

#Python Data Model exemplos
#Inicialização: obj = Novo()
#Representação: print(obj),str(obj),repr(obj)
#Containers/Sequência: len(obj),item in obj, for in obj,obj[2:3]
#Numéricas: obj+outro_obj, obj*obj









