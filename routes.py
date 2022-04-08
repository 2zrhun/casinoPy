


from flask import Flask,render_template,url_for,request,session,redirect
from error import eror, bet_eror
from module_tirage import premier_tirage, deuxieme_tirage,machine,choix_cartes
from module_gain import gain

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
        session['wallet'] = int(request.form['wallet'])
        print(session['wallet'])
        return redirect(url_for('board'))

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/board',methods=['POST'])
def tirage1():

    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h',
    '10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d',
    '6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d',
    '2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c',
    'J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s',
    '7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    
    session['bet'] =int( request.form['bet'])
    if session['bet'] > session['wallet']:
        session['eror-form'] = bet_eror
        return render_template('board.html')
    else:
        tirage1 , deck1 = premier_tirage(deck)
        session['tirage1'] = tirage1
        session['deck1'] = deck1
        

        return redirect(url_for('game'))

@app.route('/board/game')
def game():
    
    return render_template('game.html')


@app.route('/board/game', methods=['POST'])
def check_card():
    
    if request.method == 'POST':
        session['tet']=request.form.getlist('i')
        print(session['tet'])
        tirage_final= deuxieme_tirage(session['tet'],session['deck1'])
        session['g'],res= gain(tirage_final,int(session['bet']))
        session['wallet'] = session['wallet'] + int( session['g'])
        session['message'] = res

        if int(session['wallet']) == 0:
            session['message'] = "you lost"
            return redirect(url_for('board')) 

       
        
        
    return render_template('game2.html',tr2=tirage_final)
    
        

@app.route('/board/game/game2', methods=['POST','GET'])
def card2():
    
    return render_template('game2.html')



@app.route('/end',methods=['POST','GET'])
def end():
    return render_template('end.html')


if __name__ == '__main__':
    app.run(debug=True)