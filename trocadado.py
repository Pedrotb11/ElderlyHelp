
ender: str = ""
endermed: str = ""
numerpa: str = ""
nome: str = "" #para as mensagens

def trocadado (resp2):

	if(resp2 == "1"):
			msg = "troca endereço"
	elif (resp2 == "2"):
			msg = "troca endereço do médico"
	elif (resp2 == "3"):
			msg = "troca numero do parente"
	else:
			msg = "esta não é uma opção"

	return print(msg)