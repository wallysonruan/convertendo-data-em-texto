'''FUNÇÃO: Receber uma data numérica e retornar ela em texto'''
#--------------------BIBLIOTECAS-------------------------

#Biblioteca que lida com datas e horários:
from datetime import date
#
#Biblioteca que lida com regEx (regular expressions)
import re
#
#Biblioteca que interage com o sistema operacional
from os import system as s

#--------------------FUNÇÕES-------------------------

#Função que limpa o terminal
def clear():
  return s('clear')
#
#Função que, além de verificar o tamanho do input, usa a RegEx acima para validar o input do usuário
def inputValidação(entrada):
  if len(re.findall(dataFormato,entrada)) == 0 and (len(entrada) < 6 or len(entrada) > 10):
    return False
  else:
    return True
#
'''
#Função que trata o dia e retorna seu formato por extenso.
def diaExtenso(dia):
    dia = dia[0]
    if int(dia) == 10 or int(dia) >= 20:
        dia = str(dia[0]+"0")
        return dezenas[dia]
    else:
        if dia[0] != "0":
            if dia == "1":
                return "primeiro"
            else:
                return numeros[dia]

#Função que trata o mês e retorna seu formato por extenso.
def mesExtenso(mes):
    mes = mes[1]
    if mes[0] != "0":
        return meses[mes]
    else:
        return meses[str(mes[1])]

#Função que trata o ano e retorna seu formato por extenso
def anoExtenso(ano):
    ano = ano[2]
    if len(ano) == 4:
        if (ano[1] + ano[2] + ano[3]) == "000":
        	return f'{milhares[ano[0]]}'
        if (ano[2] + ano[3]) == "00":
        	return f'{milhares[ano[0]]} e {centenas[ano[1]]}'
        elif (ano[1] + ano[2]) == "00" and ano[3] != "0":
        	return f'{milhares[ano[0]]} e {numeros[ano[3]]}'
        elif ano[1] == "0" and (ano[2] + ano[3]) != "00":
        	    if ano[3] == "0":
        	    	return f'{milhares[ano[0]]} e {dezenas[ano[2]+"0"]}'
        	    else:
        	    	return f'{milhares[ano[0]]} e {numeros[ano[2] + ano[3]]}'
        else:
        	    if ano[3] != "0":
        	    	return f'{milhares[ano[0]]} {centenas[ano[1]]} e {numeros[ano[2] + ano[3]]}'
        	    else:
        	    	return f'{milhares[ano[0]]} {centenas[ano[1]]} e {dezenas[ano[2]+"0"]} e {numeros[ano[3]]}'
    else:
        if len(ano) == 2:
            if int(ano) > int(anoAtual[2] + anoAtual[3]):
                if ano[1] == "0":
                    return f'{milhares[str(int(anoAtual[0]) - 1)]} {centenas[str(9)]} e {dezenas[ano[0] + "0"]}'
                else:
                    return f'{milhares[str(int(anoAtual[0]) - 1)]} {centenas[str(9)]} e {dezenas[ano[0] + "0"]} e {numeros[ano[1]]}'
            else:
                if anoAtual[1] == "0":
                    return f'{milhares[anoAtual[0]]} e {dezenas[ano[0] + "0"]} e {numeros[ano[1]]}'
                else:
                    return f'{milhares[anoAtual[0]]} {centenas[anoAtual[1]]} e {dezenas[ano[0] + "0"]} e {numeros[ano[1]]}'
'''
#-----------------INFORMAÇÕES ADICIONAIS-----------------

#Dicionario com os números em extenso:
dicionario = {"pt-BR":{
"unidades":
{"1": "um", "2": "dois", "3": "três", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove"},
"uniIrregulares":
{"11":"onze","12":"doze","13":"treze","14":"quatorze","15":"quinze","16":"dezesseis","17":"dezessete","18":"dezoito","19":"dezenove"},
"dezenas":
{"10": "dez", "20": "vinte", "30": "trinta","40":"quarenta","50":"cinquenta","60":"sessenta","70":"setenta","80":"oitenta","90":"noventa"},
"centenas":
{"1":"cento", "2":"duzentos","3":"trezentos","4":"quatrocentos","5":"quinhentos", "6":"seiscentos", "7":"setecentos", "8": "oitocentos", "9":"novecentos"},
"milharIrregular":
{"1":"mil"},
"meses":
{"1":"janeiro","2":"fevereiro","3":"março","4":"abril","5":"maio","6":"junho","7":"julho","8":"agosto","9":"setembro","10":"outubro","11":"novembro","12":"dezembro"}
}}
#RegEx para tratar validar o input do usuário
dataFormato = "[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}|[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2}"

#--------------------PROGRAMA-------------------------

data = input("Escolha uma data:\n")
while inputValidação(data) == False:
    clear()
    data = input("FORMATO DE DATA INVÁLIDO!\n\nEscolha outra data:\n")
