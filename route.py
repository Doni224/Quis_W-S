from flask import Flask
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/isi/BB', methods=['POST'])
def BB():
    berat_kg = float(request.form.get('berat_badan'))
    tinggi_m = float(request.form.get('tinggi_badan'))
    BMI = berat_kg/(tinggi_m/100)**2
    #Hitung Berat badan
    if BMI < 18.5:
        ket = "Kurus"
    elif BMI > 18.5 and BMI < 25:
        ket = "Normal"
    elif BMI > 25 and BMI < 40:
        ket = "Berlebihan"
    else:
        ket = "Bahaya"

    data = {'ket': ket}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=False, port=4000)