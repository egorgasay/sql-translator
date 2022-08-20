import random

from flask import Flask, render_template
from complete_translate import translator
from forms import CommonForm

app = Flask(__name__)


def app_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    randArray = []
    for i in chars:
        randArray.append(chars[random.randint(0,len(chars)-1)])
    return ''.join(randArray)

app.config['SECRET_KEY'] = app_secret_key()


@app.route('/', methods=['POST', 'GET'])
def index():
    form = CommonForm()
    source_db = form.source_db.data
    text = form.text.data
    if text:
        text = translator(text, source_db)
        text2 = text.split('\n')
        ready = []
        for line in text2:
            ready.append([word for word in line[:-1].split(' ')])

        return render_template('index.html', text=ready, form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
