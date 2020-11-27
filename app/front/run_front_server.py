from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import StringField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    sentence = StringField('sentence', validators=[DataRequired()])

app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(sentence):
    body = {'sentence': sentence}

    myurl = "http://0.0.0.0:5000/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    # print(jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    # return response
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    # print(response)
    response = json.loads(response)
    # print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['sentence'] = request.form.get('sentence')

        try:
            response = str(get_prediction(data['sentence']))
            print('response after get_prediction')
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)