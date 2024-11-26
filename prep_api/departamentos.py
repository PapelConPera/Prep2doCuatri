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
          """SELECT department_name , department_id
             FROM departments"""
    ).fetchall()
    return render_template('departamento.html', departamentos=lista_departamentos)

@bp.route('/detalle/<int:id>/')
def detalle(id):
    db = get_db()
    consulta1 = """
        SELECT department_name , department_id
        FROM departments
        WHERE department_id = ?"""

    resultado = db.execute(consulta1, (id,))
    lista_departamentos = resultado.fetchone()

    consulta2 = """  
        SELECT first_name , last_name , employee_id
        FROM employees
        WHERE department_id = ?"""
    
    resultado2 = db.execute(consulta2, (id,))
    lista_empleados = resultado2.fetchall()
    

    pagina = render_template('detalleDeparta.html', departamento=lista_departamentos, empleado = lista_empleados)

    return pagina
