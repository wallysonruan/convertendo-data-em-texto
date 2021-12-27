import os, datetime, re

#FUNÇÕES AUXILIARES:

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

#FUNÇÕES DE VALIDAÇÃO:

def regEx(regEx, texto):
    if len(re.findall(regEx,texto)) > 0:
        return True
    else:
        return False

def isDezena(data):
    if regEx("[0-9].[0]", str(float(data)/10)):
        return True
    else:
        return False

def inputValidacao(data):
    if not regEx("[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4}", data) and (
            len(data) < 6 or len(data) > 10):
        return False
    else:
        return True

'''O objeto strptime reconhece o tipo de data (dia, mês, ano) baseado no formato informado e, em seguida, é possível retornar um tipo exato. O benefício dele é não precisar tratar a data em casos como 01/../.... ou 1/../...., pois se colocar "01" ele retorna "1".'''
def dia(data):
    return str(datetime.datetime.strptime(data, "%d/%m/%Y").day)

def mes(data):
    return str(datetime.datetime.strptime(data, "%d/%m/%Y").month)

def ano(data):
    try:
        return str(datetime.datetime.strptime(data, "%d/%m/%Y").year)
    except:
        return str(datetime.datetime.strptime(data, "%d/%m/%y").year)

#FUNÇÕES QUE CONVERTEM O TEXTO:

def diaExtenso(data):
    if int(dia(data)) > 10 and int(dia(data)) < 20:
        return dicionario["pt-BR"]["unidades-Irregulares"][dia(data)]
    else:
        if dia(data) == "1":
            return dicionario["pt-BR"]["unidades-Irregulares"][dia(data)]
        else:
            return dicionario["pt-BR"]["unidades"][dia(data)]

def mesExtenso(data):
    return dicionario["pt-BR"]["meses"][mes(data)]

def anoExtenso(data):
    '''Se o ano fornecido tiver apenas dois caracteres, a ano() retornará:
        se a década fornecida for menor do que a década atual: será retornado o século anterior atual;
        se for maior, será retornado o século anterior'''

    data = ano(data)

    if regEx("[1-9][0]{1,4}", data): #a000
        if regEx("[1][0]{1,4}", data):
            return dicionario["pt-BR"]["milhar-Irregular"][data[0]]
        else:
            return f'{dicionario["pt-BR"]["unidades"][data[0]]} mil'

#DADOS AUXILIARES:

dicionario = {"pt-BR": {"unidades": {"1": "um", "2": "dois", "3": "três", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito", "9": "nove"}, "unidades-Irregulares": {"1": "primeiro", "11": "onze", "12": "doze", "13": "treze", "14": "quatorze", "15": "quinze", "16": "dezesseis", "17": "dezessete", "18": "dezoito", "19": "dezenove"}, "dezenas": {"10": "dez", "20": "vinte", "30": "trinta", "40": "quarenta", "50": "cinquenta", "60": "sessenta", "70": "setenta", "80": "oitenta", "90": "noventa"}, "centenas": {"1": "cem", "2": "duzentos", "3": "trezentos", "4": "quatrocentos", "5": "quinhentos", "6": "seiscentos", "7": "setecentos", "8": "oitocentos", "9": "novecentos"}, "milhar-Irregular": {"1": "mil"}, "centena-Irregular": {"1": "cento"}, "meses": {"1": "janeiro", "2": "fevereiro", "3": "março", "4": "abril", "5": "maio", "6": "junho", "7": "julho", "8": "agosto", "9": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"}}}

print(diaExtenso("01/07/2000") + " de " + mesExtenso("01/07/2000") + " de " + anoExtenso("01/07/2000"))
