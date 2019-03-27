from app import app
import os
import click

@app.cli.group()
def translate():
    """ Translation and localization commands """
    pass
    
@translate.command()
def update():
    """ update all languages """ 
    if os.system("pybabel extract -F babel.cfg -k _l -o message.pot ."):
        raise RuntimeError('Extract command failed')
    if os.system("pybabel update -i message.pot -d app/translations"):
        raise RuntimeError('update command failed')
    #os.remove('message.pot')

@translate.command()
def compile():
    """ Compile all languages """ 
    if os.system("pybabel compile -d app/translations"):
        raise RuntimeError('Compile command failed')

@translate.command()
@click.argument('lang')
def init(lang):
    """ Initialize a new  language """ 
    if os.system("pybabel extract -F babel.cfg -k _l -o message.pot ."):
        raise RuntimeError('Extract command failed')
    if os.system("pybabel init -i message.pot -d app/translations -l"+ lang):
        raise RuntimeError('Init  command failaed')
    #os.remove('message.pot')
    
