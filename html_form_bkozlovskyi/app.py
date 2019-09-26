from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/response', methods=['POST'])
def response():
    form_name = request.form.get("form_name")
    form_email = request.form.get("form_email")
    form_message = request.form.get("form_message")
    return render_template("index.html", name=form_name, email=form_email, msg=form_message)

if __name__ == '__main__':
    app.run()