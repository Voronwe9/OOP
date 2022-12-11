class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def average_raters(self):
        grades_sum = 0
        for course_grades in self.grades.values():
            quantity = 0
            for grade in course_grades:
                quantity += grade
            course_average = quantity / len(course_grades)
            grades_sum += course_average
            return f'{grades_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        some_student += f'Средняя оценка за задание: {self.average_raters()}\n'
        some_student += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        some_student += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return some_student

    def __gt__(self, student):
        if not isinstance(student, Student):
            pass
        return self.average_raters() > student.average_raters()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}

class Lecturer(Mentor):
    def average_raters(self):
        grades_sum = 0
        for course_grades in self.rates.values():
            quantity = 0
            for grade in course_grades:
                quantity += grade
            course_average = quantity / len(course_grades)
            grades_sum += course_average
            return f'{grades_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nЧитает курс: {self.courses_attached}\n'
        some_lecturer += f'Средняя оценка за лекции: {self.average_raters()}\n'
        return some_lecturer

    def __gt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            pass
        return self.average_raters() > lecturer.average_raters()

class Reviewer(Mentor):
    # перенесли функцинал ментора в ревьювера. А необходимо было переносить?
    # Ревьювер бы его унаследовал, но тогда его унаследовал бы и Лектор?! именно для этого мы его переносим в ревьювера?
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\nПроверяет курс: {self.courses_attached}\n'
        return some_reviewer




def grades_stud (students_list, cours):
    grades_sum = 0
    iterations = 0
    for stud in students_list:
        if cours in stud.grades.keys():
            stud_sum = 0
            for grades in stud.grades[cours]:
                stud_sum += grades
            stud_mid = stud_sum / len(stud.grades[cours])
            grades_sum += stud_mid
            iterations += 1
    if grades_sum == 0:
        return f'Оценок нет!'
    else:
        return f"{grades_sum / iterations:.2f}"
        
def grades_lecturers (lecturer_list, cours):
    grades_sum = 0
    iterations = 0
    for lectur in lecturer_list:
        if cours in lectur.rates.keys():
            stud_sum = 0
            for grades in lectur.rates[cours]:
                stud_sum += grades
            stud_mid = stud_sum / len(lectur.rates[cours])
            grades_sum += stud_mid
            iterations += 1
    if grades_sum == 0:
        return f'Оценок нет!'
    else:
        return f"{grades_sum / iterations:.2f}"
    
# Студенты

student_1 = Student('Olga', 'Maslenikova', 'female')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2 = Student('Anton', 'Barynin', 'male')
student_2.courses_in_progress += ['Python', 'Git']
student_3 = Student('Vasy', 'Petrov', 'male')
student_3.courses_in_progress += ['Git']
student_3.finished_courses += ['Python']

students_list = [student_1, student_2, student_3 ]

# Проверяющие 

reviewer_1 = Reviewer('Amma', 'Garis')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Anna', 'Moris')
reviewer_2.courses_attached += ['Git'] 

reviewer_list = [reviewer_1, reviewer_2]

# Лекторs

lecturer_1 = Lecturer('Potto', 'Griss')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Otto', 'Biss')
lecturer_2.courses_attached += ['Git']

lecturer_list = [lecturer_1, lecturer_2]

# Студенты оценивают
student_1.rate_lecture(lecturer_1, 'Python', 5)
student_2.rate_lecture(lecturer_1, 'Python', 8)
student_3.rate_lecture(lecturer_1, 'Python', 2)
student_1.rate_lecture(lecturer_2, 'Git', 3)
student_2.rate_lecture(lecturer_2, 'Git', 2)
student_3.rate_lecture(lecturer_2, 'Git', 8)



# Проверяющие оценивают

reviewer_1.rate_hw(student_1, 'Python', 3)    
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_3, 'Python', 5)

reviewer_2.rate_hw(student_1, 'Git', 5)    
reviewer_2.rate_hw(student_2, 'Git', 6)  
reviewer_2.rate_hw(student_3, 'Git', 3)   

print(student_1)
print(student_2)
print(student_3)
print(reviewer_1)
print(reviewer_2)
print(lecturer_1)
print(lecturer_2)

print(f' оценки студента 1: {student_1.grades}')
print(f' оценки студента 2: {student_2.grades}')
print(f' оценки студента 3: {student_3.grades}')

print(f' оценки лектора 1: {lecturer_1.rates}')
print(f' оценки лектора 2: {lecturer_2.rates}')

print(f'Средняя оценка студентов по курсу "Git": {grades_stud(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_stud(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')