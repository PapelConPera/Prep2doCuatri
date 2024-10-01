from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from prep_api.db import get_db

bp = Blueprint('empleados', __name__,url_prefix='/empleados')

@bp.route('/')
def index():
    db = get_db()
    lista_empleado = db.execute(
          """SELECT first_name as nombre, last_name as apellido
             FROM employees;"""
    ).fetchall()
    return render_template('empleados.html', empleado=lista_empleado)