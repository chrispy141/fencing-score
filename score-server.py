from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/score')
def get_incomes():
  return jsonify(incomes)


@app.route('/hit', methods=['POST'])
def add_hit():
  print(request)
  recv = request.get_json()
  print(recv)
  print(recv['id'])
  return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
