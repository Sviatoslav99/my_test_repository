# @Unknow_User
from flask import Flask, escape, request, render_template
from deck import Deck

app = Flask(__name__)
deck = Deck()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Sviatoslav Buzian TS-72'

@app.route('/first')
def first():
    num_0 = None
    num_1 = 124
    num_2 = 123
    name = request.args.get("name", "World")
    return f'{num_0}, {num_1}, {num_2}'


@app.route('/second', methods = ['GET', 'POST'])
def second():
    #import pdb; pdb.set_trace()

    if request.method == 'GET':
        return render_template ('./third.html')
    if request.method == 'POST':
        test = request.form.get('text')
        print (test)
        return f'{test}'


@app.route('/third', methods=['GET','POST'])
def third():
    if  request.method == 'GET':
        return render_template('./index1.html')
    if request.method == 'POST':
        if "shuffle" in request.form:
            deck.shuffle()
            message = "Deck was shuffled"
        elif "pop" in request.form:
            message = deck.pop()
        elif "get_random" in request.form:
            message = deck.get_random()
        else:
            num = request.form.get("index")
            message = deck.index(num)
        return render_template('index1.html', content=message, deck=str(deck))



if __name__ == '__main__':
    app.run('0.0.0.0')
