import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        messages.append({"role": "system",
"content": "Act as if you are Sigmund Freud, the psychologist, all the time. \
Refer to Freud's work and talk like him as much as possible, \
but also act like a friendly counselor.\
Keep your answers are not too long, no more than two or three sentences."})

        input = request.form["input"]
        messages.append({"role": "user", "content": input})

        print(messages)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        answer = response.choices[0]["message"]["content"]
        messages.append({"role": "assistant", "content": answer})

        return redirect(url_for("index", result=answer))

    result = request.args.get("result")
    return render_template("index.html", result=result)

