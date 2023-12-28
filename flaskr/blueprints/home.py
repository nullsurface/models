import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('home', __name__, url_prefix='/')

# a simple page that says hello
@bp.route('/', methods=('GET', 'POST'))
def hello():
    return render_template("home.html")
