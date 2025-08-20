#Projeto Frente de Caixa -Sistema de pedidos de uma lanchonete
#==========================================================================         
#SISTEMA DE PEDIDOS
#==========================================================================
#importando a biblioteca OS para limpar a tela
from InquirerPy import prompt

import os
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
limpar_tela()
# print('Carregando tabela de preços... ')
precos = {
    'Sanduiche': {
        'Big Mac': 20.00,
        'Duplo Quarteirão': 25.00,
        'Big Tasty': 22.00
    },
    'Bebida': {
        "Coca-Cola": 5.00,
        'Fanta': 5.00,
        'Del Valle Laranja': 6.00
    },
    'Batata':{
        'Pequena': 7.00,
        'Média': 9.00,
        'Grande': 12.00
    }
}

def pegar_nome_cliente(nome):
    limpar_tela()
    print(f'Registrando nome do cliente... ')
    print(f'Vamos iniciar o pedido cliente: {nome}')

def escolher_opcao_sanduiche():
    while True:
        print('Escolha seu sanduínche: ')
        sanduiche = input(
            '1 - Big Mac: 20.00\n'
            '2 - Duplo Quarteirão: 25.00\n'
            '3 - Big Tasty: 22.00\n'
            'V - Voltar\n'
            'S - Sair '
            
        )
        if sanduiche.upper() == 'V':
            return 'voltar'
        elif sanduiche.upper() == 'S':
            exit()
        opcoes = {
            '1': 'Big Mac', 
            '2': 'Duplo Quarteirão', 
            '3': 'Big Tasty'
            }
        if sanduiche in opcoes:
            return(opcoes[sanduiche])
        print('Opção inválida, tente novamente. ')
        input('Pressione ENTER para teclar novamente... ')

def pegar_sanduiche(tipo_sanduiche):
    print(f'Você escolheu o sanduíche: {tipo_sanduiche}')


def escolher_opcao_bebida():
    while True:
        print('Escolha sua bebida: ')
        bebida = input(
            '1 - Coca-Cola: 5.00\n'
            '2 - Fanta: 5.00\n'
            '3 - Del Valle Laranja: 6.00\n'
            'V - Voltar\n'  'S - Sair '
        )
        if bebida.upper() == 'V':
            return 'voltar'
        elif bebida.upper() == 'S':
            exit()
        opcoes = {
            '1': 'Coca-Cola',
            '2': 'Fanta',
            '3': 'Del Valle Laranja'
            }
        if bebida in opcoes:
            return(opcoes[bebida])
        print('Opção inválida, tente novamente. ')
        input('Pressione ENTER para teclar novamente... ')
        
def pegar_bebida(tipo_bebida):
    print(f'Você escolheu a bebida: {tipo_bebida}')


def escolher_opcao_batata():
    while True:
        print('Escolha sua batata')
        batata = input(
                '1 - Pequena: 7.00\n'
                '2 - Média: 9.00\n'
                '3 - Grande: 12.00\n'
                'V - Voltar\n'
                'S - Sair '
        )
        if batata.upper() == 'V':
            return 'Voltar'
        elif batata.upper() == 'S':
            exit()
        opcoes ={
                '1' : 'Pequena',
                '2' : 'Média',
                '3' : 'Grande'         
        }
        if batata in opcoes:
            return(opcoes[batata])

def pegar_batata(tipo_batata):
    print(f'Você escolheu a batata do tamanho: {tipo_batata}')              

def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    limpar_tela()
    print("Montando combo completo...")
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)


pedido_todos = []

while True:
    limpar_tela()
    nome_cliente = input('Digite seu nome ou "s" para sair: ').capitalize()

    if nome_cliente.upper() == "S":
        exit()

    pegar_nome_cliente(nome_cliente)

    while True:
        menu_principal = {
            "type": "list",
            "name": "opcao",
            "message": "MENU PRINCIPAL",
            "choices": [
                "1 - Somente sanduíche",
            "2 - Somente bebida",
            "3 - Somente batata",
            "4 - Combo",
            "F - Fechar o pedido",
            "V - Voltar",
            "S - Sair"
            ]   
        }
        pedido = prompt(menu_principal)["opcao"][0].upper()  
        if pedido.upper() == 'S':
            exit()
        elif pedido.upper() == 'V':
            break
        
        pedido_cliente = {
            'sanduiche': None, 
            'bebida': None, 
            'batata': None
            }
        
        if pedido == '1':
            print('Você escolheu a opção 1')
            tipo_sanduiche = escolher_opcao_sanduiche()
            if tipo_sanduiche == 'voltar':
                continue
            limpar_tela()
            pegar_sanduiche(tipo_sanduiche)
            pedido_cliente['sanduiche'] = tipo_sanduiche
            input('\nPressione ENTER para continuar ')

        elif pedido == '2':
            print('Você escolheu a opção 2')
            tipo_bebida = escolher_opcao_bebida()
            if tipo_bebida == 'voltar':
                continue
            limpar_tela()
            input('\nPressione ENTER para continuar')
            pegar_bebida(tipo_bebida)
            pedido_cliente['bebida'] = tipo_bebida
        elif pedido == '3':
            print('Você escolheu a opção 3')
            tipo_batata = escolher_opcao_batata()
            if tipo_batata == 'voltar':
                continue
            limpar_tela()
            pegar_batata(tipo_batata)
            pedido_cliente['batata'] = tipo_batata
            input('\nPressione ENTER para continuar ')
        elif pedido == '4':
            tipo_sanduiche = escolher_opcao_sanduiche()
            if tipo_sanduiche == 'voltar':
                continue
            tipo_bebida = escolher_opcao_bebida()
            if tipo_bebida == 'voltar':
                continue
            tipo_batata = escolher_opcao_batata()
            if tipo_batata == 'voltar':
                continue
            montar_combo(nome_cliente, tipo_sanduiche, tipo_bebida, tipo_batata)
            pedido_cliente['sanduiche'] = tipo_sanduiche
            pedido_cliente['bebida'] = tipo_bebida
            pedido_cliente['batata'] = tipo_batata
            input('\nPressione Enter para continuar ')
        elif pedido.upper() == 'F':
            limpar_tela()
            print('Fechando o pedido... ')
            print(f'Cliente: {nome_cliente}')
            
            total = 0
            for index,pedido in enumerate(pedido_todos, start= 1): 
                print(f'\n Pedido {index} ')
                if pedido['sanduiche']:
                    print(f"{pedido['sanduiche']} - R$ {precos['Sanduiche'][pedido['sanduiche']]:.2f}")
                    total += precos['Sanduiche'][pedido['sanduiche']]
                if pedido['bebida']:
                    print(f"{pedido['bebida']} - R$ {precos['Bebida'][pedido['bebida']]:.2f}")
                    total += precos['Bebida'][pedido['bebida']]
                if pedido['batata']:
                    print(f"{pedido['batata']} - R$ {precos['Batata'][pedido['batata']]:.2f}")
                    total += precos['Batata'][pedido['batata']]
        
            print(f'\n $ O total do pedido é R$ {total}')
            pedido_todos = []
            print('\nPedido fechado com sucesso!')
            input('\nPressione ENTER para voltar ao menu... ')
        else:
            print('Opção inválida, tente novamente.')
            input('\nPressione ENTER para continuar... ')
        
        pedido_todos.append(pedido_cliente)
        
    






            




    







