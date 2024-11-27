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
    #agregar los salarios y los emails
    consulta = """
        SELECT e.first_name, e.last_name, e.employee_id, e.department_id, e.phone_number, e.salary, e.hire_date, d.department_name, j.job_title
        FROM employees e
        JOIN departments d ON e.department_id = d.department_id
        JOIN jobs j ON e.job_id = j.job_id
        WHERE e.employee_id = ? """

    resultado = db.execute(consulta, (id,))
    empleado= resultado.fetchone()



    pagina = render_template('detalleEmpleados.html', empleado=empleado)

    return pagina