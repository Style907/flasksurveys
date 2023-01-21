from flask import Flask, request, render_template, redirect
from surveys import satisfaction_survey
#from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
#app.config['SECRET_KEY'] = "oh-so-secret"

#debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_instructions():

    instructions = satisfaction_survey.instructions

    return render_template("home.html", instructions=instructions )


@app.route('/questions/<id>')
def show_question(id):
    id = int(id)
    question = satisfaction_survey.questions[id]

    return render_template("questions.html", question=question)

@app.route('/thankyou')
def thanks():

    return render_template('thankyou.html')

@app.route('/answers', methods=['POST'])
def get_answer():
    
    answer = request.form["choice"]
    responses.append(answer)
    id = len(responses)

    if id < len(satisfaction_survey.questions):
        return redirect(f"/questions/{id}")
    else: return redirect('/thankyou')

