from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello"

@app.route('/whereami')
def whereami():
	return "kdua"

if __name__ == '__main__':
	app.run(host="0.0.0.0")

