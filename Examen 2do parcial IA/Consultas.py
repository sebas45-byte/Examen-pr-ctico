import pandas as pd

def carga_de_datos():
    #Primero cargamos el archivo
    df=pd.read_csv('Datos recopilados.csv')

    #Ahora hacemos la limpieza para quitar los espacios sin datos
    peso = df['Peso'].dropna()
    altura = df['Altura'].dropna()
    velocidad = df['Velocidad'].dropna()
    color = df['Color'].dropna()

    return peso, altura, velocidad, color

#Con el archivo limpio, ahora podemos hacer las consultas

#Todas las consultas que se piden en la tarea
def frecuencia_absoluta(variable):
    return variable.value_counts()

def frecuencia_relativa(variable):
    
    freq_rel=variable.value_counts(normalize=True).sort_index()

    
    freq_rel=freq_rel.round(2)
    return freq_rel
def frecuencia_acumulada(variable):
    Fa=variable.value_counts().sort_index().cumsum()
    return Fa

#Ahora la mediana, moda y media (cosas mas sencillas gracias) Pd: no fue tan facil como pense
def pack_med(variable, type='num'):

    if type == 'str':
        mean = 'N/A'
        median = "N/A"
        mode = variable.mode()[0]  #la moda puede tener varios valores, pero solo usamos el primero
    elif type == 'num':
        #calculamos la media, mediana y moda de la columna si son datos numerics
        mean = round(variable.mean(), 2)  #redondeamos a 2 decimales
        median = round(variable.median(), 2)  #redondeamos a 2 decimales
        mode = variable.mode()[0]  #lo mismo que antes, la moda puede tener varios valores, pero solo usamos el primero
    
    return mean, median, mode

def formato(data, type='bar', is_text=False):
        
    elements = []
    
    for v, c in data.items():
        # Si es texto, envolvemos el valor en comillas simples, si no, lo dejamos tal cual
        v_formatted = f"'{v}'" if is_text else v

        if type == 'bar':
            elements.append(f"{{x: {v_formatted}, y: {c}}}")
        elif type == 'donut':
            elements.append(f"{{label: {v_formatted}, value: {c}}}")
            
    # Unimos todos los elementos con una coma y los envolvemos en corchetes []
    script = "[" + ",".join(elements) + "]"
    
    return script