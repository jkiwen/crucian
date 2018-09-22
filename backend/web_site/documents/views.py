from flask import Flask,render_template
from flask_classy import FlaskView

class ListView(FlaskView):
    
    route_base = '/documents'

    def index(self):
        return render_template('base.html')

