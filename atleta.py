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
from modalidades import *
from paralisias import *
class Atleta():#Classe reponsavel pela contrução dos dados dos atletas em um ojbeto
    def __init__(self,nome,idade,sexo,paralisia,covid,modalidade,medalhas):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.paralisia = paralisia
        self.covid = covid
        self.modalidade = modalidade
        self.medalhas = medalhas
    #============================ Nome #Responsavel pela validação do nomes passado para os atributos.
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,value):
        assert isinstance(value,str),"Não foi passado uma string no nome, por favor entre em contato com o suporte!"
        assert not value.isdigit(),"Apenas letras no nome, por favor!"
        assert len(value.replace(' ','')) > 3,"O nome é muito pequeno. Digite seu nome completo!"
        self._nome = value.lower()
    #============================ Idade #Responsavel pela validação da idade passada para os atributos.
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,value):
        assert isinstance(value,str),"Não foi passado uma string na idade, por favor entre em contato com o suporte!"
        assert value.isdigit(),"Digite somente números na idade porfavor!"
        assert int(value) > 5 and int(value) < 120,"A idade deve estar entre 6 e 120 anos"
        self._idade = int(value)
    #============================ Sexo #Responsavel pela validação do sexo passado para os atributos.
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self,value):
        assert isinstance(value,str),"Não foi passado uma string no sexo, por favor entre em contato com o suporte!"
        assert value.upper() == 'F' or value.upper() == 'M',"Por favor em sexo digite apenas F ou M"
        self._sexo = value.upper()
    #============================ Paralisia #Responsavel pela validação das paralisias passadas para os atributos.
    @property
    def paralisia(self):
        return self._paralisia
    
    @paralisia.setter
    def paralisia(self,value):
        assert isinstance(value,str),"Não foi passado uma string na paralisia, por favor entre em contato com o suporte!"
        assert value.isdigit(),"Digite somente números nas paralisias porfavor!"
        assert int(value) >= 0 and int(value) <= 10,"O número da paralisia deve estar entre 0 e 9"
        self._paralisia = Paralisias(int(value))
    #============================ Covid #Responsavel pela validação do covid passado para os atributos.
    @property
    def covid(self):
        return self._covid
    
    @covid.setter
    def covid(self,value):
        assert isinstance(value,str),"Não foi passado uma string no covid, porfavor entre em contato com o suporte!"
        assert value.upper() == 'S' or value.upper() == 'N',"Por favor na parte do Covid digite apenas S ou N"
        self._covid = True if value.upper() == 'S' else False
    #============================ Modalidades #Responsavel pela validação das modalidades passadas para os atributos.
    @property
    def modalidade(self):
        return self._modalidade
    
    @modalidade.setter
    def modalidade(self,value):
        assert isinstance(value,str),"Não foi passado uma string na modalidade, porfavor entre em contato com o suporte!"
        assert value.isdigit(),"Digite somente números nas modalidades porfavor!"
        assert int(value) >= 0 and int(value) <= 22,"O número da modalidade deve estar entre 0 e 21"
        self._modalidade = Modalidades(int(value))
    #============================ Medalhas #Responsavel pela validação das medalhas passadas para os atributos.
    @property
    def medalhas(self):
        return self._medalhas
    
    @medalhas.setter
    def medalhas(self,value):
        assert isinstance(value,list),"Não foi passado uma lista nas medalhas, porfavor entre em contato com o suporte!"
        assert value[0].isdigit() and value[1].isdigit() and value[2].isdigit(),"Digite somente números nas medalhas, por favor!"
        value = list(map(int,value))
        assert (value[0] >= 0 or value[0] <= 10)  or (value[1] >= 0 or value[1] <= 10) or (value[2] >= 0 or value[2] <= 10),"Você digitou um valor errado nas medalhas, por favor verifique!"
        self._medalhas = value
                
    def __repr__(self):
        modalid = str(self.modalidade.name).replace('_',' ')
        return f"Nome: [{self.nome.title()}]\nIdade: [{self.idade}]\nSexo: [{'Feminino' if self.sexo.upper() == 'F' else 'Masculino'}]\nParalisia: [{self.paralisia.name.replace('_',' ')}]\nCovid: [{'Sim' if self.covid else 'Não'}]\nModalidade: [{modalid}]\nMedalhas: [{self.medalhas[0]} Ouro] [{self.medalhas[1]} Prata] [{self.medalhas[2]} Bronze]"

        