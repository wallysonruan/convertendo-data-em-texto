'''Receber uma data numérica e retornar ela em texto'''

#Biblioteca que lida com datas e horários:
from datetime import date

#Objeto que retorna o mês atual em número:
anoAtual = str(date.today().year)

#Dicionários com os números em extenso:
numeros = {"1": "um", "2": "dois", "3": "três", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove","11":"onze","12":"doze","13":"treze","14":"quatorze","15":"quinze","16":"dezesseis","17":"dezessete","18":"dezoito","19":"dezenove"}
dezenas = {"10": "dez", "20": "vinte", "30": "trinta","40":"quarenta","50":"cinquenta","60":"sessenta","70":"setenta","80":"oitenta","90":"noventa"}
centenas = {"1":"cento", "2":"duzentos","3":"trezentos","4":"quatrocentos","5":"quinhentos", "6":"seiscentos", "7":"setecentos", "8": "oitocentos", "9":"novecentos"}
milhares = {"1":"mil", "2":"dois mil"}
meses = {"1":"janeiro","2":"fevereiro","3":"março","4":"abril","5":"maio","6":"junho","7":"julho","8":"agosto","9":"setembro","10":"outubro","11":"novembro","12":"dezembro"}

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

data = input("Escolha uma data ('dd/mm/aaaa'):\n")
data = data.split("/")
print(f'{diaExtenso(data).capitalize()} de {mesExtenso(data)} de {anoExtenso(data)}')
