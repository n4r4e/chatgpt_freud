import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"

messages = []

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        messages.append({"role": "system",
"content": "Act as you are Sigmund Freud, the psychologist. \
Refer to Freud's work and sound as Freudian as possible, \
but at the same time sound like a caring counselor.\
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

