import json
from flask import Flask, jsonify, request

FindMistakesData = [
{'correct': 'You are not in Boston.', 'incorrect': 'You is not in boston.'},
{'correct': 'I love reading books.', 'incorrect': 'I love read books.'},
{'correct': 'I am very tired.', 'incorrect': 'I is very tired.'},
]

VerbData = [
{'sentence': 'She ____ them.', 'answer' : 'likes', 'words' : ['likes', 'like', 'liked']},
{'sentence': 'It ____ tall.', 'answer' : 'is', 'words' : ['has', 'were', 'is']},
{'sentence': 'who ____ it?', 'answer' : 'ate', 'words' : ['eat', 'ate', 'eating']},
]

# creating the instance of our flask application
app = Flask(__name__)

@app.route('/fm',methods = ['GET', 'POST'])
def downloadRoute0():
    global FindMistakesData
    if(request.method == 'GET'):
        return jsonify(FindMistakesData)

    elif(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        FindMistakesData =request_data
        return ' '

@app.route('/vd',methods = ['GET', 'POST'])
def downloadRoute1():   
    global VerbData
    if(request.method == 'GET'):
        return jsonify(VerbData)
    
    elif(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        VerbData = request_data
        return ' '

if __name__ == "__main__":
    app.run(debug=True)