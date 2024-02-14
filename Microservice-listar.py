from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_word():
    return jsonify(message="Ola, Mundo")

if __name__ == '__main__': 
    app.run(debug=True, port=5000)  
    

