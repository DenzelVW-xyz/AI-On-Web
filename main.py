from flask import Flask, render_template, request
from ollama import chat, ChatResponse

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def home():

    userrequest = None
    airespData = "I'm waiting for an input!"

    if request.method == "POST":       
        userrequest = request.form.get("fname")

        response: ChatResponse = chat('tinyllama', messages=[
            {
                'role' : 'user',
                'content' : userrequest,
            },
        ])

        airespData = response['message']['content']
    
    return render_template("index.html", airesp=airespData)

if __name__ == "__main__":
    app.run(debug=True)