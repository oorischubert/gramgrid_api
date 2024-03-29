import json
from flask import Flask, jsonify, request
#from flask_cors import CORS, cross_origin #for web 

FindMistakesData = [
{'correct':'My mother always wakes up early and goes to the gym in the morning.',
'incorrect': 'My mother always wake up early and go to the gym at the morning.'},
{'correct': 'Her gym is near our house. She tries to go there three times a week',
'incorrect': 'Her gym _ near our house. She trys to go there three times a week.'},
{'correct':'Tali does her homework and studies hard for quizzes. She __ a good student.',
'incorrect': 'Tali do her homework and study hard for quizzes. She is a good student.'},
{'correct':'The children fly to Israel every summer. They visit their family in Haifa.',
'incorrect': "The children's flies to israel every summer. They visits their family at haifa."}  
]

VerbData = [
{'sentence': 'She ____ orange juice every morning.', 'answer' : 'drinks', 'words' : ['drink', 'drinks', 'is drinking']},
{'sentence': 'Be quiet! The baby ____!.', 'answer' : 'is sleeping', 'words' : ['sleep', 'sleeps', 'is sleeping']},
{'sentence': 'Sam and John ____ tennis every Sunday?', 'answer' : 'play', 'words' : ['plays', 'play', 'are playing']},
]

# creating the instance of flask application
app = Flask(__name__)
#CORS(app)

@app.route('/fm',methods = ['GET', 'POST'])
#@cross_origin(maxAge = 3600) #web auth
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
#@cross_origin(maxAge = 3600) #web auth
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