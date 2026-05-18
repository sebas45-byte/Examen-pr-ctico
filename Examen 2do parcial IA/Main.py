#libreria para el sitio web
from flask import Flask, render_template

# importamos el archivo de consultas
import Consultas as cs

#Aqui se denife como la aplicación principal
app = Flask(__name__)

#Este es el sitio que va a mostrar por default cuando se inicie el sitio web
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/peso')
def weight_data():
    peso = cs.carga_de_datos()[0]
    
    freq_abs = cs.formato(cs.frecuencia_absoluta(peso), type='bar', is_text=False)
    freq_rel = cs.formato(cs.frecuencia_relativa(peso), type='donut', is_text=False)
    freq_acum = cs.formato(cs.frecuencia_acumulada(peso), type='bar', is_text=False)
    
    mean, median, mode = cs.pack_med(peso, type='num')
    return render_template('consultas/peso.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

@app.route('/altura')
def height_data():
    altura = cs.carga_de_datos()[1]
    
    freq_abs = cs.formato(cs.frecuencia_absoluta(altura), type='bar', is_text=False)
    freq_rel = cs.formato(cs.frecuencia_relativa(altura), type='donut', is_text=False)
    freq_acum = cs.formato(cs.frecuencia_acumulada(altura), type='bar', is_text=False)
    
    mean, median, mode = cs.pack_med(altura, type='num')
    return render_template('consultas/altura.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

@app.route('/velocidad')
def velocity_data():
    velocidad = cs.carga_de_datos()[2]
    
    freq_abs = cs.formato(cs.frecuencia_absoluta(velocidad), type='bar', is_text=False)
    freq_rel = cs.formato(cs.frecuencia_relativa(velocidad), type='donut', is_text=False)
    freq_acum = cs.formato(cs.frecuencia_acumulada(velocidad), type='bar', is_text=False)
    
    mean, median, mode = cs.pack_med(velocidad, type='num')
    return render_template('consultas/velocidad.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)

@app.route('/color')
def color_data():
    color = cs.carga_de_datos()[3]
    
    freq_abs = cs.formato(cs.frecuencia_absoluta(color), type='bar', is_text=True)
    freq_rel = cs.formato(cs.frecuencia_relativa(color), type='donut', is_text=True)
    freq_acum = cs.formato(cs.frecuencia_acumulada(color), type='bar', is_text=True)
    
    mean, median, mode = cs.pack_med(color, type='str')
    return render_template('consultas/color.html', freq_abs=freq_abs, freq_rel=freq_rel, freq_acum=freq_acum, mean=mean, median=median, mode=mode)


if __name__ == '__main__':
    app.run(debug=True)