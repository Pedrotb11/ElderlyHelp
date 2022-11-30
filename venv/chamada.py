from twilio.rest import Client
#Nao prossegui com a logica deste codigo adiante pq
#minha conta é de teste e não tive tempo de alterar.
#Mas basicamente teria IFs, pra cada numero escolhido no main

account_sid = 'venv'
auth_token = 'venv'
numero_twilio = 'venv'
meu_numero = 'venv'

nome = "fulana"

mensagem = f"""
<Response>
<Say language="pt-BR">
{nome}, está precisando de ajuda. por favor, vá a sua casa
verificar se está tudo bem.
</Say>
</Response>
"""

client = Client(account_sid, auth_token)

ligacao = client.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)