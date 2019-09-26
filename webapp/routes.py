import webapp.CreaCompte as demande
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, logout_user
from webapp import app
from webapp.form import InscriptionForm


@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_anonymous:
        user = {'username': current_user.username}
    else:
        user = {'username': 'Guest'}
    return render_template('index.html', title="Page d'accueil et menu", user=user)


@app.route('/inscription', methods=['get', 'post'])
def inscription():
    formulaire = InscriptionForm()
    if formulaire.validate_on_submit():
        try :
            demande.add_demande(formulaire)
        except ValueError as e:
            flash(e)
        else :
            flash('Enregistrement validée')

    return render_template('inscription.html',title="Inscription", form=formulaire)


@app.route('/login', methods=['get', 'post'])
def login():
  pass


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


