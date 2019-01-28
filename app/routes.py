from app import app
from flask import render_template,flash,redirect,url_for

from app.forms import LoginForm
@app.route("/")
@app.route("/index")

def index():
    user={'username':'Daniel'}
    posts = [{
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!' }]
    return render_template('index.html',title='Home',user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])

def login():
    form=LoginForm()
    #form.validate_on_submit() returns True if methods=POST, False if methods=GET 
    if form.validate_on_submit():
        flash('User {} Login, remember me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)
