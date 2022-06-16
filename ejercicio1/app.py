from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dado')
def randomNum():
  num = randint(1, 6)
  return render_template('dado.html', num = str(num))

@app.route('/dado/<n>')
def randomNumQuantity(n):
  n = int(n)
  lista = []
  if n < 0 or n > 10:
    return 'El número seleccionado no es válido'
  else:
    i = 0
    while i < n:
      lista.append(randint(1, 6))
      i += 1
    return render_template('dadoNum.html', nums = lista)

def generarFecha(año, mes):
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
      dia = randint(1, 31)
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dia = randint(1, 30)
  elif mes == 2:
    if año%4 != 0:
      dia = randint(1, 28)
    else:
      dia = randint(1, 29)
  return '%i/%i/%i' % (dia, mes, año)

@app.route('/fecha')
def randomDate():
  año = randint(1970, 2100)
  mes = randint(1, 12)
  return render_template('fecha.html', fecha = generarFecha(año, mes))
@app.route('/fecha/<y>')
def randomDateYear(y):
  año = int(y)
  mes = randint(1, 12)
  if año < 0:
    return 'Un año no puede ser un número negativo'
  return render_template('fechaAño.html', fecha = generarFecha(año, mes))
    
@app.route('/fecha/<y>/<m>')
def randomDateYearMonth(y, m):
  año = int(y)
  mes = int(m)
  if año < 0:
    return 'Un año no puede ser un número negativo'
  elif mes < 0 or mes > 12:
    return 'Ese no es un número posible para un mes'
  return render_template('fechaAñoMes.html', fecha = generarFecha(año, mes))

@app.route('/color')
def randomColour():
  posiblesColoresFont = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'orange', 'brown']
  posiblesColoresTexto = ['rojo', 'azul', 'verde', 'amarillo', 'negro', 'violeta', 'naranja', 'marrón']

  num = randint(0, 7)
  
  return render_template('color.html', codigoColor = posiblesColoresFont[num], textoColor = posiblesColoresTexto[num])

app.run(host='0.0.0.0', port=81)