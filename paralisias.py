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
class Paralisias(enum.Enum):#Classe de paralisias para salvar qual o atleta tem atraves de uma numeração.
    def __str__(self):
        return self.name
    Ataxica  = 0
    Cerebral  = enum.auto()
    Paraplégico  = enum.auto()
    Tetraplégico  = enum.auto()
    Amputado  = enum.auto()
    Visual = enum.auto()
    Intelectual = enum.auto()
    Involuntaria = enum.auto()
    Tensao_muscular = enum.auto()
    Baixa_estatura = enum.auto()


