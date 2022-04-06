from flask import Flask,render_template,url_for,request,session,redirect
from error import eror, bet_eror
from module_tirage import premier_tirage, deuxieme_tirage

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def check_age():
    user_age = int(request.form['age'])
    if user_age < 18:
        session['eror-form'] = eror
        return render_template('index.html')
    else:
        session['wallet'] = request.form['wallet']
        return redirect(url_for('board'))

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/board',methods=['POST'])
def tirage1():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    session['bet'] = request.form['bet']
    if session['bet'] > session['wallet']:
        session['eror-form'] = bet_eror
        return render_template('board.html')
    else:
        session['tirage1'], session['deck1'] = premier_tirage(deck)
        return redirect(url_for('game'))

# @app.route('/game')
# def game():
#     return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)