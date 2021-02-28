from flask import Flask, render_template, request
import pickle
import os
app = Flask(__name__)
model=pickle.load(open('model','rb'))
clusters=pickle.load(open('clusters','rb'))
users=pickle.load(open('users','rb'))

@app.route('/',methods=['GET'])
def home():
    return 'Welcome to Matchmaking'

@app.route('/text', methods=['POST'])
def index(): 
    j=request.get_json()
    #To get the responses of the user in a list,either the next line or the one after that is to be executed.Since I did not make a UI, I could
    #not test both options but only the first one. In case of error, comment the 1st line and uncomment the second one.
    l=list(j.values())
    # l=list(j[0].values())
    print(l)

    g=l[0]
    l1=[]
    for i in l[1:]:
        l1.append(int(i))

    pred=model.predict([l1])
    pred=clusters[pred[0]]
    f=users[pred]
    pred=[i for i in f if i[-2]!=g]
    output=[]
    for i in pred:
        output.append(i[-1])

    final="The recommended users for you are:\n"
    for i in output:
        final=final+i+"\n"

    return final


if __name__ == "__main__":
    app.run(debug=True)