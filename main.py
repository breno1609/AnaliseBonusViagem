# Passo a Paso de Solução
# 1 Abrir os 6 arquivos em Excel
# 2 Anlisar se algum vendedor bateu 55 mil
# 3 Se for maior que 55 mil, envia um SMS para o vendedor

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf3b8efa14afc8750049f20cbab77a503"
# Your Auth Token from twilio.com/console
auth_token  = "1e6ee9257017add3410b785c16cec257"
client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if(tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5571992561130",
            from_="+15706092699",
            body= f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


