import webbrowser
#import SpeechRecognition as sr
from trocadado import trocadado
from tocaudio import tocaudio
#twilio
#selenium

print("Se é usa primeira vez usando o app, configure em trocar dados")
print("")

tocaudio()

resp = input("""Qual serviço gostaria de contactar? Escolha o número:

1= Chamar Parente
2= Samu
3= Bombeiro
4= chamar carro pro medico
5= Trocar dados

""")

print()

if (resp == "1"):
	print("twilio liga {numerpa}, minha conta é de teste e não pude mudar")

elif (resp == "2"):
	print("twilio liga samu, minha conta é de teste e não pude mudar")

elif (resp == "3"):
	print ("twilio liga bombeiro, minha conta é de teste e não pude mudar")

elif (resp == "4"):
	print ("selenium entra na uber, coloca {ender} e {endermed}")
	#não pedi a informacao do email para nao chamar mesmo um uber já que este é só um exemplo.

elif (resp == "5"):
	trocadado(resp2 = input("""qual dado deseja trocar?
	Escolha um numero:

	1= endereço
	2= endereço do médico
	3= numero do parente

	"""))

else:
  print(resp +" não é uma opção")
