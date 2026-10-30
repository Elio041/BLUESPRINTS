from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)

entradas = {
    1: "Introducción a Flask",
    2: "Aprendiendo Blueprints",
    3: "Uso de plantillas HTML"
}

@blog_bp.route('/blog/entrada/<int:id>')
def entrada(id):
    titulo = entradas.get(id, "Entrada no encontrada")
    return render_template('blog/entrada.html', titulo=titulo)