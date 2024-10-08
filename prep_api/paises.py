from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from prep_api.db import get_db

bp = Blueprint('paises', __name__,url_prefix='/paises')

@bp.route('/')
def index():
    db = get_db()
    lista_pais = db.execute(
          """SELECT country_name as paises
             FROM countries;"""
    ).fetchall()
    return render_template('pais.html', pais=lista_pais)