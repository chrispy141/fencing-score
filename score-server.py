from flask import Flask, jsonify, request

app = Flask(__name__)

scores = {}

def print_scores():
	for score in scores.keys():
		print(score + ": " + str(scores[score]))

@app.route('/score')
def get_incomes():
  return jsonify(incomes)


@app.route('/hit', methods=['POST'])
def add_hit():
  recv = request.get_json()
  id = recv["id"]
  if id in scores.keys(): 
     scores[id] = scores[id] + 1
  else:
     print("New Contender! " + id)
     scores[id] = 1
  print_scores()
  return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
