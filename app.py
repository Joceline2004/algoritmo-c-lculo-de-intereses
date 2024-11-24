from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        tipo_deuda = request.form['tipoDeuda']
        capital = float(request.form['capital'])
        tasa_interes = float(request.form['tasaInteres'])
        tiempo = float(request.form['tiempo'])
        tipo_interes = request.form['tipoInteres']

        # Ajustar la tasa de interés según las políticas
        if tipo_deuda == 'Tarjeta':
            tasa_interes += 5
        elif tipo_deuda == 'Crédito' and tiempo < 1:
            tasa_interes -= 1

        # Calcular el interés
        if tipo_interes == 'Simple':
            interes = capital * (tasa_interes / 100) * tiempo
        elif tipo_interes == 'Compuesto':
            interes = capital * ((1 + (tasa_interes / 100))**tiempo - 1)

        return render_template('index.html', interes=interes)

    return render_template('index.html', interes=None)

if __name__ == '__main__':
    app.run(debug=True)
