'''
Autor: José Gabriel de Almeida Pontes
Componente Curricular: EXA-854 MI-Algoritmos
Concluido em: 01/12/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
'''
import enum
class Modalidades(enum.Enum):#Classe de modalides para salvar qual o atleta participou atraves de uma numeração.
    def __str__(self):
        return self.name
    Atletismo = 0
    Badminton = enum.auto()
    Basquetebol_em_cadeira_de_rodas = enum.auto()
    Bocha = enum.auto()
    Canoagem = enum.auto()
    Ciclismo = enum.auto()
    Esgrima_em_cadeira_de_rodas  = enum.auto()
    Futebol_de_5  = enum.auto()
    Goalball  = enum.auto()
    Hipismo  = enum.auto()
    Judô  = enum.auto()
    Levantamento_de_peso  = enum.auto()
    Natação  = enum.auto()
    Remo  = enum.auto()
    Rugby_em_cadeira_de_rodas  = enum.auto()
    Taekwondo  = enum.auto()
    Tênis_de_mesa  = enum.auto()
    Tênis_em_cadeira_de_rodas  = enum.auto()
    Tiro  = enum.auto()
    Tiro_com_arco  = enum.auto()
    Triatlo  = enum.auto()
    Voleibol_sentado  = enum.auto()
