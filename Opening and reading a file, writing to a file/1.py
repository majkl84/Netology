
class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def all_grades(self):
        # функция возвращения всех оценок
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        # функция подсчета среднего арифметического числа
        average_grade = sum(Student.all_grades(self)) / len(Student.all_grades(self))
        return round(average_grade, 1)

    def __lt__(self, other):
        # функция сравнения студентов по средней оценки за домашнее задание
        if self.average() >= other.average():
            return f"{self.name} {self.surname} средняя оценка больше, равно {self.average()}"
        else:
            return f"{self.name} {self.surname} средняя оценка меньше, равно {self.average()}"

    def __str__(self):
        try:
            print(
                f"Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {Student.average(self)}"
                f"\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")
        except ZeroDivisionError:
            print("нет курсов")

    def lecturer_grades(self, lecturer, course, grade):
        # функция добавления лекторам оценок
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        self.grades = {}
        super().__init__(name, surname)

    def all_grades(self):
        # функция возвращения всех оценок
        sum_grades = []
        for value_item in self.grades.values():
            for new_list in value_item:
                sum_grades += [new_list]

        return sum_grades

    def average(self):
        # функция подсчета среднего арифметического числа
        average_grade = sum(Lecturer.all_grades(self)) / len(Lecturer.all_grades(self))
        return round(average_grade, 1)

    def __lt__(self, other):
        if self.average() >= other.average():
            return f"{self.name} {self.surname} средняя оценка больше, равно {self.average()}"
        else:
            return f"{self.name} {self.surname} средняя оценка меньше, равно {self.average()}"

    def __str__(self):
        try:
            print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.average(self)}")
        except ZeroDivisionError:
            print("нет лекций")

    def show_grades(self):
        # просмотр всех оценок у лекторов
        for key_course, value_grades in self.grades.items():
            print(f"Курс: {key_course} Оценка: {value_grades}")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        print(f"Имя: {self.name}\nФамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        # функция добавления студентам оценок
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def courses_average_students(student_list, course):
    # подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    # в качестве аргументов принимаем список студентов и название курса

    for student in student_list:
        for k, v in student.grades.items():
            if course == k:
                sum_average = sum(v) / len(v)
                print(f"Студент: {student.name} {student.surname}\nКурс: {k}\n"
                      f"Cредняя оценка за домашние задания: {round(sum_average, 1)}\n")


def courses_average_lecturer(lecturer_list, course):
    # подсчет средней оценки за лекции всех лекторов в рамках конкретного курса
    # в качестве аргументов принимаем список лекторов и название курса
    for lecturer in lecturer_list:
        for k, v in lecturer.grades.items():
            if course == k:
                sum_average = sum(v) / len(v)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\nКурс: {k}\n"
                      f"Cредняя оценка за курс: {round(sum_average, 1)}\n")


# студенты
ivan_student = Student('Ivan', 'Kovalev', 'man')
igor_student = Student('Igor', 'Yanov', 'man')
irina_student = Student('Irina', 'Grekova', 'girl')
# курсы студентов в прогрессе
ivan_student.courses_in_progress += ['Python']
ivan_student.finished_courses += ['Git']
igor_student.courses_in_progress += ['Python']
igor_student.courses_in_progress += ['Git']
irina_student.courses_in_progress += ['C++']
irina_student.courses_in_progress += ['Git']
# ******
pety_reviewer = Reviewer('Petr', 'Rydov')
tolik_reviewer = Reviewer('Toly', 'Cherbov')
pety_reviewer.courses_attached += ['Python']
tolik_reviewer.courses_attached += ['Git']
tolik_reviewer.courses_attached += ['C++']
# ******
pety_reviewer.rate_hw(ivan_student, 'Python', 0)
pety_reviewer.rate_hw(ivan_student, 'Python', 9)
pety_reviewer.rate_hw(ivan_student, 'Python', 6)
pety_reviewer.rate_hw(igor_student, 'Python', 10)
pety_reviewer.rate_hw(igor_student, 'Python', 10)
pety_reviewer.rate_hw(igor_student, 'Python', 10)
tolik_reviewer.rate_hw(igor_student, 'Git', 9)
tolik_reviewer.rate_hw(igor_student, 'Git', 9)
tolik_reviewer.rate_hw(igor_student, 'Git', 9)
tolik_reviewer.rate_hw(irina_student, 'Git', 7)
tolik_reviewer.rate_hw(irina_student, 'Git', 7)
tolik_reviewer.rate_hw(irina_student, 'Git', 7)
tolik_reviewer.rate_hw(irina_student, 'C++', 9)
tolik_reviewer.rate_hw(irina_student, 'C++', 9)
tolik_reviewer.rate_hw(irina_student, 'C++', 9)
ivan_student.__str__()
# irina_student.comparison_student(ivan_student)
# лектора
alex_lecturer = Lecturer('Alex', 'Eratov')
igor_lecturer = Lecturer('Igor', 'Kyzin')
anton_lecturer = Lecturer('Anton', 'Orlov')
# выставление оценок лекторам
ivan_student.lecturer_grades(alex_lecturer, 'Python', 10)
ivan_student.lecturer_grades(alex_lecturer, 'Python', 10)
ivan_student.lecturer_grades(alex_lecturer, 'Python', 10)
igor_student.lecturer_grades(alex_lecturer, 'Python', 10)
igor_student.lecturer_grades(alex_lecturer, 'Python', 10)
igor_student.lecturer_grades(alex_lecturer, 'Python', 10)
igor_student.lecturer_grades(igor_lecturer, 'Git', 8)
igor_student.lecturer_grades(igor_lecturer, 'Git', 5)
igor_student.lecturer_grades(igor_lecturer, 'Git', 6)
irina_student.lecturer_grades(igor_lecturer, 'Git', 7)
irina_student.lecturer_grades(igor_lecturer, 'Git', 7)
irina_student.lecturer_grades(igor_lecturer, 'Git', 7)
irina_student.lecturer_grades(alex_lecturer, 'Git', 9)
irina_student.lecturer_grades(alex_lecturer, 'Git', 9)
irina_student.lecturer_grades(alex_lecturer, 'Git', 9)
irina_student.lecturer_grades(anton_lecturer, 'C++', 10)
irina_student.lecturer_grades(anton_lecturer, 'C++', 10)
irina_student.lecturer_grades(anton_lecturer, 'C++', 10)
# __str()__
pety_reviewer.__str__()
alex_lecturer.__str__()
ivan_student.__str__()
# подсчет средней оценки за домашние задания
print("")
courses_average_students(Student.student_list, 'Git')
courses_average_lecturer(Lecturer.lecturer_list, 'Git')
# сравнение студентов и лекторов
print(igor_lecturer > alex_lecturer)
print(ivan_student < irina_student)
