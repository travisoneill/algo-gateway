import requests
from flask import Flask, request, redirect, json, jsonify, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/test')
def hello():
    print('Hello!  Api Gateway is running.')
    return('Hello!  Api Gateway is running.')

@app.route('/')
def root():
    return send_from_directory('', 'index.html')

@app.route('/api/algos', methods=['POST'])
def send():
    urls = {
        'node': 'https://flask-algo.appspot.com',
        'flask': 'https://tough-hull-141417.appspot.com'
    }
    services = {
        'javascript': 'node',
        'python': 'flask'
    }

    incoming_data = request.get_json()
    print("INCOMING")
    print(incoming_data)
    print("JSON")
    print(json.dumps(incoming_data))
    test_params = incoming_data['lengthArr']
    responses = []
    final_data = {}
    print(request.is_json)
    for key, request_data in incoming_data.items():
        if key[0:4] != 'data':
            continue
        language = request_data['language']
        server = services[language]
        request_url = urls[server] + request.path
        outgoing_data = {'lengthArr': test_params, 'request_data': request_data}
        headers = {'Content-Type' : 'application/json'}
        res = requests.post(request_url, data=json.dumps(outgoing_data), headers=headers)
        print(res)
        final_data[key] =  json.loads(res.content)
        print(jsonify(final_data))
    return jsonify(final_data)

if __name__  == "__main__":
    app.run()
