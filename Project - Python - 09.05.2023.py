# -*- coding: utf-8 -*-

import datetime
import os

# PROCESSAMENTO E SAIDA DE DADOS
def cadastrar_cliente():
    arq = open("Clientes.csv", "a")
    
    nome = input("Digite o nome do cliente: ")
    email = input('Digite o e-mail do cliente: ')
    telefone = informar_telefone()
    endereco = input("Digite o endereço do cliente (Rua e Nº): ")
    arq.write(nome + ';' + email + ';' + telefone + ';' + endereco + '\n')
    
    arq.close()
    
    print("Cliente", nome, "cadastrado com sucesso!")

def fazer_venda():
    arq = open("Vendas.csv", "a")
    cliente = input("Digite o nome do cliente: ")
    dia = informar_data()
    
    while True:
        produto = input("Digite o nome do produto ou '5' para encerrar: ")
        if produto == '5':
            break
        valor = input("Digite o valor da venda: R$")
        quantidade = input("Digite a quantidade de produtos: ")
    
        arq.write(cliente + ';'  + dia + ';' + produto + ';' + quantidade + ';' + valor + ';' '\n')
     
    arq.close()
    
    print("Venda cadastrada com sucesso!")
    
def consultar_cadastro_cliente():
    contador = 0
    flag = 0
    
    cliente = input("Digite o nome do cliente: ")
    arq = open("Clientes.csv", "r")
    
    for line in arq:
        dados = line.strip().split(";")
        if dados[0] == cliente:
            flag = 1
            print(''f"Nome: {dados[0]} - E-mail: {dados[1]} - Telefone: {dados[2]} - Endereço: {dados[3]}")
    contador +=1
    arq.close()
    if flag==0:
        print("cliente nao foi encontrado")
    
def consultar_vendas_cliente():
    valor_total = 0
    contador = 0
    
    
    cliente = input("Digite o nome do cliente: ")
    arq = open("Vendas.csv", "r")
    
    for line in arq:
        dados = line.strip().split(";")
        if dados[0] == cliente:
            if contador == 0:
                print("O cliente", cliente, "efetuou as seguintes compras" )
            print(''f"Data: {dados[1]} - Produto: {dados[2]} - Quantidade: {dados[3]} - Valor: {dados[4]}")
            valor_total += float(dados[4].replace(',', '.'))
            contador +=1
    arq.close()
    if contador==0:
        print("cliente nao foi encontrado")
    else:
        print(''f" O valor total das compras do cliente foi: {valor_total}")
        
def relatorio():
    cliente = None
    valor_total = 0
   
    arq = open("Vendas.csv", "r")
    if os.path.exists('Relatorio.csv'):
        os.remove('Relatorio.csv')
    novo_arq=open('Relatorio.csv', 'w')
    novo_arq.write("Cliente;Data;Produto;Quantidade;Valor;Total;\n") 
    for line in arq:
        dados = line.strip().split(";")
        if cliente != dados[0]:
            valor_total = 0
        cliente = dados[0]
        valor_total += float(dados[4].replace(',', '.'))
        novo_arq.write(''f"{cliente};{dados[1]};{dados[2]};{dados[3]};{dados[4]};{valor_total};\n") 
    print("Relatório gerado! Verifique a planilha para ver o relatório.")          
    arq.close()
    novo_arq.close()
    
def informar_telefone(ocorreu_erro = False):
    if ocorreu_erro == True:
        telefone = input("Telefone inválido, digite o número de telefone novamente: ")
    else:
        telefone = input("Digite o número de telefone (54999990000): ")
    
    try:
        if int(telefone):
            return telefone
    except ValueError:
        return informar_telefone(True)

def informar_data(ocorreu_erro = False):
    if ocorreu_erro == True:
        dia = input("Formato de data inválido digite a data novamente: ")
    else:
        dia = input("Digite a data da compra (dd/mm/yyyy): ")
    
    try:
        if datetime.datetime.strptime(dia,'%d/%m/%Y'):
            return dia
    except ValueError:
        return informar_data(True)
    
# ENTRADA DE DADOS
while True:
    print('-----------------------------------------')
    print("        BEM VINDO AO BOM CONTROLE!       ")
    print("           ESCOLHA UMA OPÇÃO!            ")
    print('-----------------------------------------')
    print("[1] - Cadastrar cliente                  ")
    print('-----------------------------------------')
    print("[2] - Fazer venda                        ")
    print('-----------------------------------------')
    print("[3] - Consultar cadastro de um cliente   ")
    print('-----------------------------------------')
    print("[4] - Consultar compras de um cliente    ")
    print('-----------------------------------------')
    print("[5] - Relatório geral de vendas          ")
    print('-----------------------------------------')
    print("[9] - Sair                               ")
    print('-----------------------------------------')
    
    opcao = int(input("Digite a opção desejada: "))
    print('-----------------------------------------')
    
    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        fazer_venda()
    elif opcao == 3:
        consultar_cadastro_cliente()
    elif opcao == 4:
        consultar_vendas_cliente()
    elif opcao == 5:
        relatorio()
    elif opcao == 9:
        print('Você saiu!')
        break
    else:
        print("Opção inválida!")