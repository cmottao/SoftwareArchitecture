from repositories import grade_repository

def list_grades():
    return grade_repository.get_all()

def create_grade(student_name, subject, score):
    grade_repository.add(student_name, subject, score)

def delete_grade(grade_id):
    grade_repository.delete_by_id(grade_id)
