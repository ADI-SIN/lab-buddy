from flask import Flask

app = Flask(__name__)

# Global variable block


# Blobal Classes block


# Helper functions block





# Endpoints block

@app.route('/', methods=['GET'])
def home():
	return 'Welcome to Lab Buddy'


# API runner
app.run(host='0.0.0.0',debug=True,port=9898)