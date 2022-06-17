from flask import Flask, jsonify, request
from flask_restx import Api, Resource, reqparse
import json

server = Flask(__name__)

api = Api(server, version='1.0', title='circle ci 연동 테스트', description='python api', doc='/api-docs')

api1_api = api.namespaces('제공 api', description='api1')
api2_api = api.namespaces('제공 api', description='api2')

@api1_api.route('/api1', methods=['POST'])
def api1_request():
    print(request.get_json())
    d = {"result": {"status": "requested"}, "request_data": request.get_json()}
    json_data = json.dumps(d)
    return json_data, {"Content-Type": "application/json"}


@api2_api.route('/api2', methods=['POST'])
def api2_request():
    print(request.get_json())
    d = {"result": {"status": "requested"}, "request_data": {"checkData1": "one"}}
    json_data = json.dumps(d)
    return jsonify(json_data), {"Content-Type": "application/json"}


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=25252)