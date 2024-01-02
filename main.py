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
from  modalidades import Modalidades
from atleta import Atleta
from platform import system
import os
import time
import jsonpickle
from paralisias import Paralisias

def main():#Responsavel por rodar todos o codigo.
    limpar_terminal()
    menu_principal()

#-----------------------------------==[Menus]==-----------------------------------
def menu_principal():#Mostra o menu e chama as funções responsaveis por cada codigo digitado no menu.
    dict_atletas = ler_atletas()
    codigo_menu = 1
    while codigo_menu != 6:
        imprimir_tela_principal()
        codigo_menu = validar_menu((input('              Opção do menu: ')))
        limpar_terminal()
        if codigo_menu == 1:
            cadastrar_atleta(dict_atletas)
        elif codigo_menu == 2:
            menu_edicao(dict_atletas)
        elif codigo_menu == 3:
            imprimir_cadastrados(dict_atletas)
        elif codigo_menu == 4:
            menu_relatorios(dict_atletas)
        elif codigo_menu == 5:
            imprimir_tela_ajuda()
        else:
            sair_cadastro(dict_atletas)

def menu_edicao(dict_atletas):#Mostra o menu de educao e chama as funções responsaveis por cada codigo digitado no menu.
    codigo_edicao = 0
    while codigo_edicao != 3:
        imprimir_tela_edicao(dict_atletas)
        codigo_edicao = validar_menu_edicao(input(f'                             Opção do menu: '))
        if codigo_edicao == 1:
            limpar_terminal()
            atualizar_cadastro(dict_atletas)
        elif codigo_edicao == 2:
            limpar_terminal()
            remover_cadastro(dict_atletas)
        else:
            limpar_terminal()
            print('Voltando para o menu principal!')
            time.sleep(0.5)
        limpar_terminal()

def menu_atualizar_cadastro(dict_atletas,nome_atualizar):#Mostra o menu de atualização do cadastro e chama as funções responsaveis por cada codigo digitado no menu.
    atleta = dict_atletas[nome_atualizar]
    atributos = ["Nome","Idade","Sexo","Paralisia","Covid","Modalidade","Medalhas"]
    dicas = ['Apenas letras','Entre 6 ~ 120 anos','[M] Masculino [F] Feminino','Entre [0~9]','[S] Sim [N] Não','Entre [0~21]']

    imprimir_tela_atualizacao_cadastro()
    print(f"Atualizando o cadastro [{atleta.nome.title()}]")
    codigo_menu = validar_menu_atualizar(input('Digite uma opção: '))
    while codigo_menu != 9:
        limpar_terminal()
        if codigo_menu == 1:   
            atualizar_atributo = input((f"Digite a(o) {atributos[codigo_menu-1]}:\n")).lower()
            atualizar_nome(atualizar_atributo,dict_atletas,nome_atualizar,atleta,atributos,codigo_menu)
        elif codigo_menu < 7:
            if codigo_menu == 4:
                imprimir_paralisias()

            if codigo_menu == 6:
                imprimir_modalidades()

            atualizar_atributo = input((f"{dicas[codigo_menu-1]}\nDigite a(o) {atributos[codigo_menu-1]}:\n"))
            limpar_terminal()
            setar_cadastro(atleta,atributos[codigo_menu-1],atualizar_atributo)

        elif codigo_menu == 7:
            medalhas = colher_medalhas()
            limpar_terminal()
            setar_cadastro(atleta,atributos[codigo_menu-1],medalhas)

        elif codigo_menu == 8:
            del dict_atletas[nome_atualizar]
            atleta = cadastrar_atleta(dict_atletas)

        imprimir_tela_atualizacao_cadastro()
        print(f"Atualizando o cadastro [{atleta.nome.title()}]")
        codigo_menu = validar_menu_atualizar(input('Digite uma opção: '))

def menu_relatorios(dict_atletas):#Mostra o menu de relatorios e chama as funções responsaveis por cada codigo digitado no menu.
    imprimir_tela_relatorios()
    codigo_menu = validar_menu_relatorios(input('Digite uma opção: '))
    while codigo_menu != 6:
        limpar_terminal()
        if codigo_menu == 1:
            imprimir_relatorio1(dict_atletas)
        elif codigo_menu == 2:
            imprimir_relatorio2(dict_atletas)
        elif codigo_menu == 3:
            imprimir_relatorio3(dict_atletas)
        elif codigo_menu == 4:
            imprimir_relatorio4(dict_atletas)
        else:
            imprimir_relatorio5(dict_atletas)
        limpar_terminal()
        imprimir_tela_relatorios()
        codigo_menu = validar_menu_relatorios(input('Digite uma opção: '))
        limpar_terminal()

#-----------------------------------===========-----------------------------------

#-----------------------------------==[Arquivos(Leitura/Gravação)]==-----------------------------------
def ler_atletas():#Ler os atletas cadastrados previamente se existir um arquivo.
    nomeArquivo = "atletas.json"
    dic = {}
    if os.path.exists(nomeArquivo):
        arquivo = open(nomeArquivo, "r")
        lerArquivo = arquivo.read()
        if not lerArquivo == '':#Verifica se tem algo escrito, pra não quebrar
            try: #Só uma garantia maior pro codigo não quebrar.
                dic = jsonpickle.decode(lerArquivo)
            except: pass
        arquivo.close()
    return dic  

def salvar_atletas(dict_atletas):#Função para salvar todos os atletas em .json.
    nomeArquivo = "atletas.json"
    arquivo = open(nomeArquivo,"w")
    arquivo.write(jsonpickle.encode(dict_atletas, indent=2,)) 
    arquivo.close()
#-----------------------------------================================-----------------------------------

#-----------------------------------==[Validações]==-----------------------------------
def validar_menu(entrada):#Valida as opções do menu.
    while not entrada.isdigit() or (int(entrada) < 1 or int(entrada) > 6):
        entrada = input('     Opção invalida! Digite novamente: ')
    return int(entrada)

def validar_menu_edicao(entrada):#Valida as opções do menu de edição.
    while not entrada.isdigit() or (int(entrada) < 1 or int(entrada) > 3):
        entrada = input('                       Opção invalida! Digite novamente: ')
    return int(entrada)

def validar_menu_atualizar(entrada):#Valida as opções do menu de atualização de cadastro.
    while not entrada.isdigit() or (int(entrada) < 1 or int(entrada) > 9):
        entrada = input('Opção invalida! Digite novamente: ')
    return int(entrada)

def validar_menu_relatorios(entrada):#Valida as opções do menu de relatorios.
    while not entrada.isdigit() or (int(entrada) < 1 or int(entrada) > 6):
        entrada = input('Opção invalida! Digite novamente: ')
    return int(entrada)
#-----------------------------------================-----------------------------------

#-----------------------------------==[Procedimentos]==-----------------------------------
def limpar_terminal():#Limpa o terminal a depender do sistema.
    os.system('cls' if system().lower() == 'windows' else 'clear')

def coletar_dados_atlletas(dict_atletas):#Função para pegar os dados do usuario.
        nome_atleta = input('Nome:\n').lower()
        while nome_atleta in dict_atletas.keys():
            limpar_terminal()
            nome_atleta = input('Já existe esse cadastro, digite outro Nome:\n').lower()
        limpar_terminal()

        idade_atleta = input('Idade: [6-120]:\n')
        limpar_terminal()

        sexo_atleta = input('Sexo do atleta: [F] Feminino ou [M] Masculino\n')
        limpar_terminal()

        imprimir_paralisias()
        paralisia_atleta = input('Qual a paralisia do atelta: [0-11]\n')
        limpar_terminal()

        covid_atleta = input('O atleta teve covid: [S] Sim ou [N] Não\n')
        limpar_terminal()

        imprimir_modalidades()  
        modaldiade_atleta = input('Qual a modalidade do atleta: [0-21]\n')
        limpar_terminal()       

        medalhas_atleta = colher_medalhas()
        return nome_atleta,idade_atleta,sexo_atleta,paralisia_atleta,covid_atleta,modaldiade_atleta,medalhas_atleta

def criar_atleta(dict_atletas,nome_atleta,idade_atleta,sexo_atleta,paralisia_atleta,covid_atleta,modaldiade_atleta,medalhas_atleta):#Cria um atelta e joga no dicionario com base no dados coletados.
        try:
            atleta = Atleta(nome_atleta,idade_atleta,sexo_atleta,paralisia_atleta,covid_atleta,modaldiade_atleta,medalhas_atleta)
            dict_atletas[atleta.nome] = atleta
            limpar_terminal()
            return atleta
        except Exception as erro:
            limpar_terminal()
            print(erro)

def cadastrar_atleta(dict_atletas):#Função para juntar toda a parte relacionada ao cadastro de um atleta.
    limpar_terminal()
    atleta = None
    while atleta is None:
        nome_atleta,idade_atleta,sexo_atleta,paralisia_atleta,covid_atleta,modaldiade_atleta,medalhas_atleta = coletar_dados_atlletas(dict_atletas)
        atleta = criar_atleta(dict_atletas,nome_atleta,idade_atleta,sexo_atleta,paralisia_atleta,covid_atleta,modaldiade_atleta,medalhas_atleta)
    print('Cadastrado com sucesso!')
    time.sleep(0.9)
    limpar_terminal()
    return atleta

def imprimir_cadastrados(dict_atletas):#Imprimi todos os cadastros existentes.
    for num,nome in enumerate(sorted(dict_atletas.keys())):
        print(f"[{num}]\n{dict_atletas[nome]}")
    enter = input('Pressione enter para continuar...')
    limpar_terminal()

def sair_cadastro(dict_atletas):#Sai do cadastro e chama a função de salvar os dados de todos os atletas.
    print(f"Guardando os dados...")
    salvar_atletas(dict_atletas)
    time.sleep(1.5)
    limpar_terminal()
    print('Dados guardados com sucesso! Ze&Cadastros.')

def remover_cadastro(dict_atletas):#Remove um atleta do dicionarios de atletas.
    nome_remover = input('Digite o nome do Atleta\n').lower()
    if nome_remover in dict_atletas.keys():
        del dict_atletas[nome_remover]
        limpar_terminal()
        print('Atleta removido com sucesso!')
        time.sleep(0.9)
    else:
        limpar_terminal()
        print('Esse nome não existe no nosso banco de dados!\nTalvez seja valido você consultar os cadastros no menu principal!')
        time.sleep(3)

def atualizar_cadastro(dict_atletas):#Função para juntar todos as funções relacionadas a alteração dos dados.
    nome_atualizar = input('Digite o nome do Atleta\n').lower()
    limpar_terminal()
    if nome_atualizar in dict_atletas.keys():
        menu_atualizar_cadastro(dict_atletas,nome_atualizar)
        limpar_terminal()
        print('Retornando...!')
        time.sleep(0.9)
    else:
        print('Esse nome não existe no nosso banco de dados!\nTalvez seja valido você consultar os cadastros no menu principal!')
        time.sleep(3)

def setar_cadastro(obj,atributo,novo_valor):#Função para setar o atributo da classe no objeto.
    try:
        setattr(obj,atributo.lower(),novo_valor)
        limpar_terminal()
        print(f'{atributo} atualizado(a) com sucesso!')
    except Exception as erro:
        print(erro)

def colher_medalhas():#Colhe as medalhas e joga pra função de coleta de dados.
    medalhas = ['Ouro','Prata','Broze']
    return [input(f'Quantas medalhas de {medalha} o atleta obteve: [0-10]\n') for medalha in medalhas]

def imprimir_modalidades():#Imprimi todas as modalidades para mostrar na hora da pergunta.
    for num,modaliade in enumerate(Modalidades):
        if (num+1)%2 == 0:
            print(f"[{num}] {str(modaliade).replace('_',' ')}")
        else:
            print(f"[{num}] {str(modaliade).replace('_',' ')}",end=' // ')
    print()

def imprimir_paralisias():#Imprimi todas as paralisias para mostrar na hora da pergunta.
    for num,paralisia in enumerate(Paralisias):
        if (num+1)%2 == 0:
            print(f"[{num}] {str(paralisia).replace('_',' ')}")
        else:
            print(f"[{num}] {str(paralisia).replace('_',' ')}",end=' // ')
    print()

def atualizar_nome(atualizar_atributo,dict_atletas,nome_atualizar,atleta,atributos,codigo_menu):#Função especifica para atualização do nome do usuario para alterar na chave do dicionario.
    if not atualizar_atributo in dict_atletas.keys():
        setar_cadastro(atleta,atributos[codigo_menu-1],atualizar_atributo)
        dict_atletas[atualizar_atributo] = dict_atletas.pop(nome_atualizar)
    else:
        limpar_terminal()
        print(f"Já existe esse nome em nosso banco de dados!")
#-----------------------------------===================-----------------------------------

#-----------------------------------==[Questões]==-----------------------------------
def realizar_relatorio1(dict_atletas):#Responsavel por fazer todo o processo logico do relatorio 1.
    sexo_fem = [0 for i in range(22)]
    sexo_masc = [0 for i in range(22)]
    for atleta in dict_atletas.values():
        if atleta.sexo.lower() == 'f':
            sexo_fem[atleta.modalidade.value] += 1
        else:
            sexo_masc[atleta.modalidade.value] += 1
    return sexo_masc,sexo_fem

def imprimir_relatorio1(dict_atletas):#Imprimi os dados obtidos pelos processos logicos referente ao relatorio 1.
    sexo_masc,sexo_fem = realizar_relatorio1(dict_atletas)
    for modalidade in Modalidades:
        if sexo_masc[modalidade.value] != 0 or sexo_fem[modalidade.value] != 0:
            print(f"[{sexo_fem[modalidade.value]} Fem // {sexo_masc[modalidade.value]} Masc] -- [Total: {sexo_fem[modalidade.value] + sexo_masc[modalidade.value] }] == [{str(modalidade).replace('_',' ')}]")
    print(f'Nº total de atletas [{len(dict_atletas)}]')
    enter = input('Pressione enter para continuar...')

def realizar_relatorio2(dict_atletas):#Responsavel por fazer todo o processo logico do relatorio 2.
    sexo_fem = [0 for i in range(22)]
    sexo_masc = [0 for i in range(22)]
    for atleta in dict_atletas.values():
        if atleta.covid:
            if atleta.sexo.lower() == 'f':
                sexo_fem[atleta.modalidade.value] += 1
            else:
                sexo_masc[atleta.modalidade.value] += 1
    return sexo_masc,sexo_fem

def imprimir_relatorio2(dict_atletas):#Imprimi os dados obtidos pelos processos logicos referente ao relatorio 2.
    sexo_masc,sexo_fem = realizar_relatorio2(dict_atletas)
    for modalidade in Modalidades:
        if sexo_masc[modalidade.value] != 0 or sexo_fem[modalidade.value] != 0:
            print(f"[{sexo_fem[modalidade.value]} Fem // {sexo_masc[modalidade.value]} Masc] -- [Total: {sexo_fem[modalidade.value] + sexo_masc[modalidade.value] }] == [{str(modalidade).replace('_',' ')}]")
    enter = input('Pressione enter para continuar...')

def realizar_relatorio3(dict_atletas):#Responsavel por fazer todo o processo logico do relatorio 3
    medalhas_atleta = [[0,0,0] for i in range(22)]
    for atleta in dict_atletas.values():
        for i in range(3):
            medalhas_atleta[atleta.modalidade.value][i] += atleta.medalhas[i]
    return medalhas_atleta

def imprimir_relatorio3(dict_atletas):#Imprimi os dados obtidos pelos processos logicos referente ao relatorio 3.
    medalhas_atleta = realizar_relatorio3(dict_atletas)
    for modalidade in Modalidades:
        if sum(medalhas_atleta[modalidade.value]) > 0:
            print(f"[{medalhas_atleta[modalidade.value][0]} Ouro] [{medalhas_atleta[modalidade.value][1]} Prata] [{medalhas_atleta[modalidade.value][2]} Bronze] -- [{str(modalidade).replace('_',' ')}]")
    enter = input('Pressione enter para continuar...')

def realizar_relatorio4(dict_atletas):#Responsavel por fazer todo o processo logico do relatorio 4. 
    sexo_fem = [[] for i in range(22)]
    sexo_masc = [[] for i in range(22)]
    for atleta in dict_atletas.values():
        if sum(atleta.medalhas) > 0:
            if atleta.sexo.lower() == 'f':
                sexo_fem[atleta.modalidade.value].append(atleta)
            else:
                sexo_masc[atleta.modalidade.value].append(atleta)
    return sexo_masc,sexo_fem

def imprimir_relatorio4(dict_atletas):#Imprimi os dados obtidos pelos processos logicos referente ao relatorio 4.
    sexo_masc,sexo_fem = realizar_relatorio4(dict_atletas)
    for modalidade in Modalidades:
        if len(sexo_masc[modalidade.value]) != 0:
            print(f"-------[{str(modalidade).replace('_',' ')}] == [Sexo Masculino]-------")
            for i in range(len(sexo_masc[modalidade.value])):
                print(sexo_masc[modalidade.value][i])
        if len(sexo_fem[modalidade.value]) != 0:
            print(f"\n-------[{str(modalidade).replace('_',' ')}] == [Sexo Feminino]-------")
            for i in range(len(sexo_fem[modalidade.value])):
                print(sexo_fem[modalidade.value][i])
    enter = input('Pressione enter para continuar...')

def realizar_relatorio5(dict_atletas):#Responsavel por fazer todo o processo logico do relatorio 5.
    modalidades_atleta = [False for i in range(22)]
    for atleta in dict_atletas.values():
        if not modalidades_atleta[atleta.modalidade.value]:#Só pra n setar True novamente onde já é
            modalidades_atleta[atleta.modalidade.value] = True
    return modalidades_atleta

def imprimir_relatorio5(dict_atletas):#Imprimi os dados obtidos pelos processos logicos referente ao relatorio 5.
    medalhas_atleta = realizar_relatorio3(dict_atletas)
    modalidades_atleta = realizar_relatorio5(dict_atletas)

    print(f'[{sum(modalidades_atleta)} Participações pelo Brasil]\n')  

    print('Modalidades com medalhas-[ / ',end='')     
    for modalidade in Modalidades:
        if modalidades_atleta[modalidade.value] != 0:
            if sum(medalhas_atleta[modalidade.value]) > 0:
                print(str(modalidade).replace('_',' '),end=' / ')
    print(']\n')

    print('Participação sem medalhas-[ / ',end='')  
    for modalidade in Modalidades:
        if modalidades_atleta[modalidade.value] != 0:
            if sum(medalhas_atleta[modalidade.value]) == 0:
                print(str(modalidade).replace('_',' '),end=' / ')
    print(']\n')

    print(f"[{len(modalidades_atleta) - sum(modalidades_atleta)} Modalidades que o Brasil não participou:]")
    for modalidade in Modalidades:
        if modalidades_atleta[modalidade.value] == 0:
                print(f"[{str(modalidade).replace('_',' ')}]")
    enter = input('Pressione enter para continuar...')

#-----------------------------------==============-----------------------------------

#-----------------------------------==[Telas]==-----------------------------------
def imprimir_tela_principal():#Tela exibida no menu principal.
    print(
        f'+-------------------------------------------------+\n'
        f'│     +=│    Cadastramento Paralimpíada    │=+    │\n'
        f'│                     (UEFS)                      │\n'
        f'│ [1] Cadastrar -=- [3] Cadastrados -=- [5] Ajuda │\n'
        f'│ [2] Editar    -=- [4] Relatórios  -=- [6] Sair  │\n' 
        f'+------------------------------------------------ +'
    )

def imprimir_tela_ajuda():#Tela exibida no menu de ajuda.
    print(
        f'+===============================================================================================================+\n'
        f'│Bem-vindo ao sistema de cadastramento da Paralimpíada!                                                         │\n'
        f'│([1] Cadastrar  ) Rensposavel por cadastrar um atleta.                                                         │\n'
        f'│([2] Editar     ) Rensposavel por editar um cadastro já efetuados.                                             │\n'
        f'│([3] Cadastrados) Rensposavel por mostrar todos os cadastros já efetuados.                                     │\n'
        f'│([4] Relatórios ) Rensposavel por mostrar todos os relatórios de Medalhas, Sexo, Quantidade de atletas, etc.   │\n'
        f'│([5] Ajuda      ) Rensposavel por mostrar o que cada opção do menu faz.                                        │\n'
        f'│([6] Sair       ) Rensposavel por encerrar o sistema.                                                          │\n'
        f'+===============================================================================================================+')
    enter = input('Pressione enter para continuar...')
    limpar_terminal()

def imprimir_tela_edicao(dict_atletas):#Tela exibida no menu de edição.
    limpar_terminal()
    print(
        f'+=============================================================================+\n'
        f'│                    -=--[Edição de cadastro]--=-         Nº DE ATLETAS[{len(dict_atletas)}]    │\n'
        f'│    [1] Atualizar Cadastro [2] Remover cadastro [3] Voltar p/menu            │\n'
        f'+=============================================================================+'
    )

def imprimir_tela_atualizacao_cadastro():#Tela exibida no menu de atualização de cadastro.
    print(
        f'+====================================================================================================+\n'
        f'│                                     -=--[Atualização de cadastro]--=-                              │\n'
        f'│  [1] Nome  // [3] Sexo      // [5] Resultado Covid // [7] Medalhas                    // [9] Sair  │\n'   
        f'│  [2] Idade // [4] Paralisia // [6] Modalidade      // [8] Refazer o cadastro completo //           │\n'
        f'+====================================================================================================+'
    )

def imprimir_tela_relatorios():#Tela exibida no menu de relatorios.
    print(
        f'+====================================================================================================+\n'
        f'│                                     -=--[Relatórios]--=-                                           │\n'
        f'│                     [1] Relatorio 1 // [3] Relatório 3 // [5] Relatório 5                          │\n'   
        f'│                     [2] Relatorio 2 // [4] Relatório 4 // [6] Sair                                 │\n'
        f'+====================================================================================================+'
    )

#-----------------------------------===========-----------------------------------

if __name__ == '__main__':
    main()



        