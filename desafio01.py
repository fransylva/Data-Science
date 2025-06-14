import statistics

empresas = {
    "Empresa 1": [2500, 2800, 3000, 9500, 12000],
    "Empresa 2": [5000, 5200, 5300, 5400, 5500],
    "Empresa 3": [1000, 2000, 8000, 15000, 20000],
    "Empresa 4": [3500, 4000, 4200, 4300, 6000],
    "Empresa 5": [1200, 1500, 1800, 2500, 10000]
}

def media(valores):
    print(f'Média: {statistics.mean(valores):.2f}')

def moda(valores):
    try:
        print(f'Moda: {statistics.mode(valores):.2f}')
    except:
        print('Moda: Sem moda (valores únicos)')

def mediana(valores):
    print(f'Mediana: {statistics.median(valores):.2f}')

def desvio_padrao(valores):
    print(f'Desvio Padrão: {statistics.stdev(valores):.2f}')

def amplitude(valores):
    print(f'Amplitude: {max(valores) - min(valores):.2f}')

def variancia(valores):
    print(f'Variância: {statistics.variance(valores):.2f}')

def analisar_empresas(dados):
    for nome_empresa, valores in dados.items():
        print(f'\nEstatísticas para {nome_empresa.upper()}:')
        media(valores)
        mediana(valores)
        moda(valores)
        desvio_padrao(valores)
        amplitude(valores)
        variancia(valores)
analisar_empresas(empresas)