from flask import Flask, jsonify, request
import json

server = Flask(__name__)


@server.route('/api1', methods=['POST'])
def api1_request():
    print(request.get_json())
    d = {"result": {"status": "requested"}, "request_data": request.get_json()}
    json_data = json.dumps(d)
    return json_data, {"Content-Type": "application/json"}

@server.route('/api2', methods=['POST'])
def api2_request():
    print(request.get_json())
    d = {"result": {"status": "requested"}, "request_data": {"checkData1": "one"}}
    json_data = json.dumps(d)
    return jsonify(json_data), {"Content-Type": "application/json"}


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=25252)