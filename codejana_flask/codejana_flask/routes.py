from codejana_flask import app, db
from flask import render_template, url_for, redirect, flash
from codejana_flask.forms import SignUpForm, LoginForm
from codejana_flask.models import User

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html',title='Home')

@app.route('/about')
def about():
    return render_template('About.html',title='About')

@app.route('/account')
def account():
    return render_template('Account.html',title='Account')


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form=SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}', category="success")
        return redirect(url_for('login'))
    return render_template('signUp.html', title='Sign Up', form=form)



@app.route('/login', methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if form.email.data==user.email and form.password.data==user.password:
            flash(f'Login successfull for {form.email.data}', category='success')
            return redirect(url_for('account'))
        else:
            flash(f'Login unsuccessfull for {form.email.data}', category='danger')
            return redirect(url_for('login'))
 
    return render_template('login.html', title='Login', form=form)


