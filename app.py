from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hey EQFX team, we have Flask in a Docker container and GKE!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

	