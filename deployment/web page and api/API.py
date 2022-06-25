from flask import Flask, request, jsonify
import joblib
import re

app = Flask(__name__)

model = joblib.load('best_model.h5')

try:

    os = {
        "mac": 0, 
        "windows": 2, 
        "free": 1
    }

    # -----------

    gaming = {
        "gaming": 0, 
        "normal": 1
    }

except:
    print("Value error check value of OS or Normal is correct or not and try agane")

def extract_client_from_request(req_data):
    client = []
    client.append(req_data['Processor'])
    client.append(req_data['Screen Size(inch)'])
    client.append(req_data['RAM(GB)'])
    client.append(req_data['Graphics Card'])
    client.append(req_data['SSD(GB)'])
    client.append(req_data['HDD(GB)'])
    client.append(os[req_data['OS'].lower()])
    client.append(gaming[req_data['Normal'].lower()])

    
    return client



@app.route('/predict', methods=['POST'])
def predict():
    try:
        client = [extract_client_from_request(request.json)]

        client = extract_client_from_request(request.json)

        if re.findall("core i\d|exon", client[0].lower()) or re.findall("[amd|ryzen] \d \d+", client[0].lower()) or re.findall("m1", client[0].lower()):
            pass
        else:
            return jsonify({'processor error': "enter correct processor as intel core i7 core i7 1000u or amd ryzen 5 3600x or M1 chip 8 core"})



        if float(client[1]) > 8 and float(client[1]) < 30:
            pass
        else:
            return jsonify({"inter correct number between 8 and 30 inch inScreen Size"})

      

        if float(client[2]) >= 1 and float(client[2]) <= 64:
            pass
        else:
            return jsonify({"inter correct number between 1 and 64 GB in RAM"})


        
        if int(client[4]) >= 0 or int(client[5]) <= 0 or (int(client[4]) >= 0 and int(client[5]) <= 0):
            pass

        else:
            return jsonify({"inter correct number  in ssd or hdd or at least of of them and other inter in it zero"})
        

    except:
        return jsonify({"Value error" :"check value of OS or Normal is correct or not and try agane"})

    try:

        prediction = model.predict([client])[0]
        return jsonify({'price is': prediction})

    except:
        return jsonify({"error": "server error"})



if __name__ == '__main__':
    app.run()
