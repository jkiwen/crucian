from flask import render_template,g
from flask_classy import FlaskView


class ListView(FlaskView):
    route_base = '/documents'

    def index(self):
        return render_template('views/list.html')