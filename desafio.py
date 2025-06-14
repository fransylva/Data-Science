#Você é um profissional em transição de carreira e está avaliando novas oportunidades de emprego.
#Utilize estatísticas como média, moda, mediana e desvio padrão, amplitude, variância para analisar as faixas salariais oferecidas por diferentes empresas e tomar uma decisão embasada.***
#Explique sua escolha com base nos dados analisados

#Verifique isso através dos salários:

empresas = {
    "Empresa 1": [2500, 2800, 3000, 9500, 12000],
    "Empresa 2": [5000, 5200, 5300, 5400, 5500],
    "Empresa 3": [1000, 2000, 8000, 15000, 20000],
    "Empresa 4": [3500, 4000, 4200, 4300, 6000],
    "Empresa 5": [1200, 1500, 1800, 2500, 10000]
}

import statistics

def média(lista):
    média_ = statistics.mean(lista)
    print('Média:', média_)

def moda(lista):
    moda_ = statistics.moda(lista)
    print('Moda:',moda_)

def mediana(lista):
    mediana_ = statistics.median(lista)
    print('Mediana:', mediana_)

def desvio_padrao(lista):
    desvio = statistics.stdev(lista)
    print('Desvio Padrão:', desvio)

def amplitude(lista):
    menor = min(lista)
    maior = max(lista)
    amplitude = maior - menor 
    print('Amplitude:', amplitude)

def variancia(lista):
    variancia = statistics.variance(lista)
    print('Variância:', variancia)

