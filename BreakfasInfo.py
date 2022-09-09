#!/usr/bin/env python
# coding: utf-8

# In[149]:


# obter previsao do tempo
import requests

previsao_tempo = "https://api.hgbrasil.com/weather?array_limit=2&fields=only_results,temp,woeid=449648,forecast,max,min,date&key=1e6cdd6e"
requisicao1 = requests.get(previsao_tempo)
print(requisicao1.json())


# In[150]:


# obter cotacao do dolar
cotacao = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
requisicao2 = requests.get(cotacao)
print(requisicao2.json())


# In[151]:


# enviar email diario com as infos acima


# In[152]:


import smtplib
import email.message

def enviar_email():  
    corpo_email = f"""
    <p>Bom dia!</p>
    <p>A previsao do tempo para hoje é a seguinte:</p>
    <p>{requisicao1.json()}</p>
    <p>A cotacao do dolar, Euro e Bitcoin é:</p>
    <p>{requisicao2.json()}</p>
    <p>Tenha um bom dia!</p>
    <p>Att, 
    Kelisson (da ©UifalusiTech)</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Informações do dia pra você"
    msg['From'] = 'kelisson.rodrigues7@gmail.com'
    msg['To'] = 'kelisson.rodrigues7@gmail.com'
    password = 'opvonkzbllccigsq' #sua senha do gmail (a mesma do email remetente)
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[153]:


enviar_email()


# In[ ]:


# Agendar envio diario de emails com as infos acima com agendador de tarefas do Windows

