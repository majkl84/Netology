class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def grades(self):
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        average_grade = sum(Student.grades(self)) / len(Student.grades(self))
        return round(average_grade, 1)
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {Student.average(self)}" \
               f"\n Курсы в процессе изучения: {self.courses_in_progress}\n Курсы завершены: {self.finished_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def grades(self):
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        average_grade = sum(Lecturer.grades(self)) / len(Lecturer.grades(self))
        return round(average_grade, 1)
    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {Lecturer.average(self)}"


class Reviewer(Mentor):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f" Имя: {self.name}\n Фамилия: {self.surname}"

Ruoy = Student('Ruoy', 'Eman', 'your_gender')
Ivan = Student('Иван', 'Жаров', 'your_gender')
Ruoy.courses_in_progress += ['Python']
Ruoy.finished_courses += ['C++']
Ivan.courses_in_progress += ['Python']
Ivan.courses_in_progress += ['Java']

Some_mentor = Reviewer('Some', 'Buddy')
Petr_mentor = Reviewer('Петр', 'Сидоров')
Some_mentor.courses_attached += ['Python']
Some_mentor.courses_attached += ['C++']
Petr_mentor.courses_attached += ['Java']

Some_mentor.rate_st(Ruoy, 'Python', 9)
Some_mentor.rate_st(Ruoy, 'Python', 10)
Some_mentor.rate_st(Ruoy, 'Python', 10)
Petr_mentor.rate_st(Ivan, 'Java', 9)
Petr_mentor.rate_st(Ivan, 'Java', 10)
Petr_mentor.rate_st(Ivan, 'Java', 9)

Vasya_lecturer = Lecturer('Васиан', 'Сидоров')
Gena_lecturer = Lecturer('Гена', 'Сидоров')
Vasya_lecturer.courses_attached += ['Python']
Gena_lecturer.courses_attached += ['Java']

Ruoy.rate_lec(Vasya_lecturer, 'Python', 10)
Ruoy.rate_lec(Vasya_lecturer, 'Python', 9.6)
Ruoy.rate_lec(Vasya_lecturer, 'Python', 10)
Ivan.rate_lec(Gena_lecturer, 'Java', 10)
Ivan.rate_lec(Gena_lecturer, 'Java', 7)
Ivan.rate_lec(Gena_lecturer, 'Java', 8)


print(Ruoy.grades)
print(Some_mentor.courses_attached)
print(Gena_lecturer.grades)
print(Some_mentor)
print(Vasya_lecturer)
print(Ruoy)