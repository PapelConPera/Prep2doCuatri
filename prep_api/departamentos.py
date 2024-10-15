from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from prep_api.db import get_db

bp = Blueprint('departamentos', __name__,url_prefix='/departamentos')

@bp.route('/')
def index():
    db = get_db()
    lista_departamentos = db.execute(
          """SELECT department_name as departamentos
             FROM departments;"""
    ).fetchall()
    return render_template('departamento.html', departamentos=lista_departamentos)