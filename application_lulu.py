from flask import Flask, render_template, request, redirect
app = Flask(__name__)

app.vars = {}
app.questions = {}
app.questions['How many eyes do you have?']=('1','2','3')
app.questions['Which fruit do you like best?']=('banana','mango','pineapple')
app.questions['Do you like cupcakes?']=('yes','no','maybe')

app.nquestions = len(app.questions)


@app.route('/index_lulu', methods=['GET', 'POST'])
def index_lulu():
    nquestions = app.nquestions
    time_of_reward = '4pm'
    if request.method == 'GET':
        return render_template('userinfo_lulu.html', num = nquestions, time = time_of_reward)
    else:
        # request is a POST
        app.vars['name'] = request.form['name_lulu']
        app.vars['age'] = request.form['age_lulu']
        
        f = open('%s_%s.txt' % (app.vars['name'], app.vars['age']), 'w')
        f.write('Name: %s\n' % (app.vars['name']))
        f.write('Age: %s\n' % (app.vars['age']))
        f.close()
        
        return redirect('/main_lulu')
        
@app.route('/main_lulu')
def main_lulu():
    if len(app.questions) == 0: 
        return render_template('end_lulu.html')
    return redirect('next_lulu')


@app.route('/next_lulu', methods = ['GET'])
def next_lulu():
    n = app.nquestions - len(app.questions) + 1
    q = app.questions.keys()[0]
    a1, a2, a3 = app.questions.values()[0]
    
    # Save the current question to be used in the POST method
    app.current_question = q
    
    return render_template('layout_lulu.html', num = n, question = q, ans1 = a1, ans2 = a2, ans3 = a3)
    
@app.route('/next_lulu', methods = ['POST'])
def next_lulu2():
    '''
    Here, we will collect the data from the user.
    Then, we return to the main function, so that it can tell us whether to 
    display another question page, or just show us the end page
    '''
    f = open('%s_%s.txt' % (app.vars['name'], app.vars['age']), 'a') # a is for append at the bottom of file
    f.write('%s\n' % (app.current_question))
    f.write('%s\n' % (request.form['answer_from_layout_lulu'])) # this was the 'name' on layout.html
    f.close()
    
    # Remove the question from the dictionary
    del app.questions[app.current_question]
    return redirect('/main_lulu')

if __name__ == '__main__':
    app.run(debug=True)