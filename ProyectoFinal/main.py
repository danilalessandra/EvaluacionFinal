from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre_result = total_sin_descuento_result = descuento_aplicado_result = total_con_descuento_result = None

    if request.method == 'POST':
        # Procesar los datos del formulario 1 aquí
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        # Calcular descuento
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_sin_descuento = tarros * 9000
        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        # Pasar los resultados a la plantilla
        nombre_result = nombre
        total_sin_descuento_result = total_sin_descuento
        descuento_aplicado_result = descuento_aplicado
        total_con_descuento_result = total_con_descuento

    return render_template('ejercicio1.html',
                           nombre_result=nombre_result,
                           total_sin_descuento_result=total_sin_descuento_result,
                           descuento_aplicado_result=descuento_aplicado_result,
                           total_con_descuento_result=total_con_descuento_result)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        # Procesar los datos del formulario 2 aquí
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        # Verificar usuario y contraseña
        usuarios = {'juan': 'admin', 'pepe': 'user'}
        if nombre in usuarios and usuarios[nombre] == contraseña:
            mensaje = f"Bienvenido {'Administrador' if nombre == 'juan' else 'Usuario'} {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)


