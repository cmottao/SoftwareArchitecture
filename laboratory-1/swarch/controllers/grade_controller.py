from flask import Blueprint, render_template, request, redirect, url_for
from services import grade_service

grade_bp = Blueprint('grade_bp', __name__)

@grade_bp.route('/')
def index():
    grades = grade_service.list_grades()
    return render_template('grade_list.html', grades=grades)

@grade_bp.route('/add', methods=['POST'])
def add():
    student = request.form['student_name']
    subject = request.form['subject']
    score = float(request.form['score'])
    grade_service.create_grade(student, subject, score)
    return redirect(url_for('grade_bp.index'))

@grade_bp.route('/delete/<int:grade_id>')
def delete(grade_id):
    grade_service.delete_grade(grade_id)
    return redirect(url_for('grade_bp.index'))
