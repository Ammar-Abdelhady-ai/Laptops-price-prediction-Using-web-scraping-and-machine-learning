from flask import Flask, render_template, url_for, request, jsonify
import joblib, sqlite3, time

app = Flask(__name__)
model = joblib.load('est_model.h5')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        extract_client_from_request = []
        extract_client_from_request.append(request.form['Processor'])
        extract_client_from_request.append(request.form['Screen_Size_inch'])
        extract_client_from_request.append(request.form['RAM_GB'])
        extract_client_from_request.append(request.form['Graphics_Card'])
        extract_client_from_request.append(request.form['SSD_GB'])
        extract_client_from_request.append(request.form['HDD_GB'])
        extract_client_from_request.append(request.form['OS'])
        extract_client_from_request.append(request.form['Normal'])
        client = [extract_client_from_request]
        prediction = model.predict(client)[0]
        time.sleep(0.5)

        return jsonify({'result': 'success', 'prediction': round(prediction, 2)})

@app.route("/view", methods=['GET', 'POST'])
def view():
    if request.method == 'GET':
        return render_template("view.html")
    else:
        max = request.form['maximum'] + ".0"
        min = request.form['minimum'] + ".0"
        conn = sqlite3.connect('C:\\Users\\Ammar\\Desktop\\deployment\\web page and api\\clear.sqlite')
        conn.row_factory = dict_factory
        #conn.row_factory = lambda cursor, row: row[0]
        c = conn.cursor()
        list = conn.execute('SELECT * FROM clear WHERE "price EG" > :min AND "price EG" < :max', {'max' : max,'min' : min}).fetchall()
        return jsonify({'list': list})
    

if __name__ == "__main__":
    app.run(debug=True)
