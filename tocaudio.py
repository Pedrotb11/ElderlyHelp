from playsound import playsound
import os
from gtts import gTTS
import pyttsx3

def tocaudio():
	#with open('frase_inicial.txt', 'r') as arquivo:
		#for linha in arquivo:
	frase = gTTS("""Se eh usa primeira vez usando o app, configure em trocar dados.
		Qual serviço gostaria de contactar? Escolha o número:
		1- Chamar Parente
		2- Samu
		3- Bombeiro
		4- chamar carro pro medico
		5- Trocar dados""", lang='pt-br')
	frase.save('audio.mp3')
	playsound('audio.mp3')
	os.remove('audio.mp3')
	#with open('frase_inicial.txt', 'r') as arquivo:
		#frase = gTTS(arquivo, lang='pt-br', slow=False)
		##arq = os.path.join(os.getcwd(), 'fala.mp3')
		#frase.save(arq)
		#playsound.playsound(arq)
		#os.remove('arq')


		#s = pyttsx3.init()
		#data = arquivo
		#s.say(data)
		#s.runAndWait()