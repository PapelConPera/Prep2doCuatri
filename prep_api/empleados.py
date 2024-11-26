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
          """SELECT first_name, last_name, employee_id
             FROM employees;"""
    ).fetchall()
    return render_template('empleados.html', empleado=lista_empleado)

@bp.route('/<int:id>/')
def detalle(id):
    db = get_db()
    consulta = """
            SELECT first_name, last_name, employee_id, department_id, phone_number
            FROM employees
            WHERE department_id  = ?"""

    resultado = db.execute(consulta, (id,))
    empleado= resultado.fetchone()



    pagina = render_template('detalleEmpleados.html', empleado=empleado)

    return pagina