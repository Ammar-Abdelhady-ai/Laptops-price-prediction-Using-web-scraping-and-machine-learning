from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('D:\\New folder\\model.txt')


def extract_client_from_request(req_data):
    client = []
    Processor = req_data['Processor']
    screen = req_data['Screen Size(inch)']
    ram = req_data['RAM(GB)']
    graphics = req_data['Graphics Card']
    ssd = req_data['SSD(GB)']
    hdd = req_data['HDD(GB)']
    os = req_data['OS']
    normal = req_data['Normal']

    # evaluation
    try:
        if (Processor.includes("cpu") or
            Processor.includes("intel") or Processor.includes("xeon") or
            Processor.includes(" e") or Processor.includes("i3") or
            Processor.includes("i5") or Processor.includes("i7") or
            Processor.includes("i9") or Processor.includes("amd") or
            Processor.includes("ryzen") or Processor.includes("r3") or
            Processor.includes("r 3") or Processor.includes("r5") or
            Processor.includes("r 5") or Processor.includes("r7") or
            Processor.includes("r 7") or Processor.includes("m1")):
                pass
        else:
            return jsonify({"Processor error": "please a valid Processor model"})

        if (Graphics_Card.length >= 2 and (Graphics_Card.includes("gpu") or
            Graphics_Card.includes("nividia") or Graphics_Card.includes("rtx") or
            Graphics_Card.includes("gtx") or Graphics_Card.includes("geforce") or
            Graphics_Card.includes("quadro") or Graphics_Card.includes("amd") or
            Graphics_Card.includes("radeon") or Graphics_Card.includes("rx") or
            Graphics_Card.includes("vega") or Graphics_Card.includes("intel") or
            Graphics_Card.includes("iris") or Graphics_Card.includes("hd") or
            Graphics_Card.includes("m1") or Graphics_Card.includes("graphic"))):
            pass
        else:
            return jsonify({"Processor error": "please a valid Graphics Card model"})

        if ssd > 128 and ssd <= 4000:
            pass
        else:
            return jsonify({"ssd error": "please number betwwen 128, 40000"})

        if hdd > 128 and hdd <= 4000:
            pass
        else:
            return jsonify({"hdd error": "please number betwwen 128, 40000"})
        if screen >= 8 and screen <= 30:
            pass
        else:
            return jsonify({"screen error": "please inter number betwwen 8, 30"})
        if type(ram) == int:
            if ram >= 2 and ram <= 64:
                pass
        else:
            return jsonify({"ram error": "please number betwwen 2, 64"})

    except:
        return jsonify({"error": "Server Error"})
    return client


@app.route('/predict', methods=['POST'])
def predict():
    client = [extract_client_from_request(request.json)]
    prediction = model.predict(client)[0]
    return jsonify({'price is': prediction})


if __name__ == '__main__':
    app.run()
