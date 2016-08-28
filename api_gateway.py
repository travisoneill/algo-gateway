import requests
from flask import Flask, request, redirect, json, jsonify

# ports = {
#     'node': "8001",
#     'flask': "8002",
#     'static': "8003"
# }
#
# services = {
#     'javascript': 'node',
#     'python': 'flask'
# }

app = Flask(__name__)

@app.route('/test')
def hello():
    print('Hello!  Api Gateway is running.')
    return('Hello!  Api Gateway is running.')

@app.route('/')
def reroute():
    # res = requests.get('http://localhost:' + ports['static']+ '/' )
    # print(res)
    # return res.content
    return('Hello!  Api Gateway is running.')

# @app.route('/<path:params>')
# def root(params):
#     if params == '':
#         res = requests.get('http://localhost:' + ports['static']+ '/' )
#         return res.content
#     else:
#         url = 'http://localhost:' + ports['static']+ '/' + params
#         return redirect(url, code=302, Response=None)
#
# @app.route('/api/algos', methods=['POST'])
# def send():
#     incoming_data = request.get_json()
#     print("INCOMING")
#     print(incoming_data)
#     print("JSON")
#     print(json.dumps(incoming_data))
#     test_params = incoming_data['lengthArr']
#     responses = []
#     final_data = {}
#     print(request.is_json)
#     for key, request_data in incoming_data.items():
#         if key[0:4] != 'data':
#             continue
#         language = request_data['language']
#         server = services[language]
#         request_url = 'http://localhost:' + ports[server] + request.path
#         outgoing_data = {'lengthArr': test_params, 'request_data': request_data}
#         headers = {'Content-Type' : 'application/json'}
#         res = requests.post(request_url, data=json.dumps(outgoing_data), headers=headers)
#         print(res)
#         final_data[key] =  json.loads(res.content)
#         print(jsonify(final_data))
#     return jsonify(final_data)

#gunicorn
#tornado

if __name__  == "__main__":
    app.run()
