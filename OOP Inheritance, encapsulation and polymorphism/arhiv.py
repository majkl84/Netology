class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_student = float

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_l:
                lecturer.grades_l[course] += [grade]
            else:
                lecturer.grades_l[course] = [grade]
        else:
            return 'Ошибка'
    def average_grades(self) -> float:
        self.average_grade_student = sum(self.grades[self.courses_in_progress[0]]) \
                                    / len(self.grades[self.courses_in_progress[0]])
        return ("{0:.1f}" .format(self.average_grade_student))
    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self.average_grades()}\n Курсы в процессе изучения: {self.courses_in_progress}\n Курсы завершены: {self.finished_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_l = {}
        self.average_grade_lector = float

    def average_grade(self) -> float:
        self.average_grade_lector = sum(self.grades_l[self.courses_attached[0]]) \
                                    / len(self.grades_l[self.courses_attached[0]])
        return self.average_grade_lector

    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_grade()}"


class Reviewer(Mentor):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student_1 = Student('Иван', 'Жаров', 'your_gender')
best_student_1.courses_in_progress += ['Java']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor_1 = Reviewer('Петр', 'Сидоров')
cool_mentor_1.courses_attached += ['Java']

very_mentor = Lecturer('Any', 'Versary')
very_mentor.courses_attached += ['Python']
very_mentor_1 = Lecturer('Яна', 'Петрова')
very_mentor_1.courses_attached += ['Java']

best_student.rate_lec(very_mentor, 'Python', 10)
best_student.rate_lec(very_mentor, 'Python', 9.6)
best_student.rate_lec(very_mentor, 'Python', 10)
best_student.rate_lec(very_mentor, 'Python', 10)

best_student_1.rate_lec(very_mentor_1, 'Java', 8.8)
best_student_1.rate_lec(very_mentor_1, 'Java', 9.5)
best_student_1.rate_lec(very_mentor_1, 'Java', 9.7)

cool_mentor.rate_st(best_student, 'Python', 9)
cool_mentor.rate_st(best_student, 'Python', 10)
cool_mentor.rate_st(best_student, 'Python', 10)

cool_mentor_1.rate_st(best_student_1, 'Java', 9)
cool_mentor_1.rate_st(best_student_1, 'Java', 10)
cool_mentor_1.rate_st(best_student_1, 'Java', 9)

print(best_student.grades)
print(cool_mentor.courses_attached)
print(very_mentor.grades_l)
print(cool_mentor)
print(very_mentor)
print(best_student)