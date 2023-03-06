class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and (course in self.courses_in_progress or course in self.finished_courses)
                and grade <= 10 and type(grade) == int):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка!"

    def __str__(self):
        student_initials = f"""
Имя: {self.name}
Фамилия: {self.surname}
"""
        rates = [x for value in self.grades.values() for x in value]
        if len(rates) != 0:
            average_rate = sum(rates) / len(rates)
            average = f"Средняя оценка за домашние задания: {average_rate} \n"
        else:
            average = f"Средняя оценка за домашние задания: оценок пока нет \n"
        if len(self.courses_in_progress) > 0:
            courses = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
        else:
            courses = f"Курсы в процессе изучения: пока нет изучаемых курсов \n"
        if len(self.finished_courses) > 0:
            fin_courses = f"Завершенные курсы: {', '.join(self.finished_courses)} \n"
        else:
            fin_courses = f"Завершенные курсы: пока нет завершенных курсов \n"
        res = student_initials + average + courses + fin_courses
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            try:
                rates_self = [x for value in self.grades.values() for x in value]
                average_self = sum(rates_self) / len(rates_self)
                rates_other = [x for value in other.grades.values() for x in value]
                average_other = sum(rates_other) / len(rates_other)
            except ZeroDivisionError:
                if len(rates_self) == 0:
                    average_self = 0
                elif len(rates_other) == 0:
                    average_other = 0
            return average_self < average_other
        return "Ошибка!"

    def __le__(self, other):
        if isinstance(other, Student):
            try:
                rates_self = [x for value in self.grades.values() for x in value]
                average_self = sum(rates_self) / len(rates_self)
                rates_other = [x for value in other.grades.values() for x in value]
                average_other = sum(rates_other) / len(rates_other)
            except ZeroDivisionError:
                if len(rates_self) == 0:
                    average_self = 0
                elif len(rates_other) == 0:
                    average_other = 0
            return average_self <= average_other
        return "Ошибка!"

    def __eq__(self, other):
        if isinstance(other, Student):
            try:
                rates_self = [x for value in self.grades.values() for x in value]
                average_self = sum(rates_self) / len(rates_self)
                rates_other = [x for value in other.grades.values() for x in value]
                average_other = sum(rates_other) / len(rates_other)
            except ZeroDivisionError:
                if len(rates_self) == 0:
                    average_self = 0
                elif len(rates_other) == 0:
                    average_other = 0
            return average_self == average_other
        return "Ошибка!"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        lecturer_initials = f"""
Имя: {self.name}
Фамилия: {self.surname}
"""
        rates = [x for value in self.grades.values() for x in value]
        if len(rates) != 0:
            average_rate = sum(rates) / len(rates)
            average = f"Средняя оценка за лекции: {average_rate} \n"
        else:
            average = f"Средняя оценка за лекции: оценок пока нет \n"
        res = lecturer_initials + average
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            try:
                self_rates = [x for value in self.grades.values() for x in value]
                average_self = sum(self_rates) / len(self_rates)
                other_rates = [x for value in other.grades.values() for x in value]
                average_other = sum(other_rates) / len(other_rates)
            except ZeroDivisionError:
                if len(self_rates) == 0:
                    average_self = 0
                elif len(other_rates) == 0:
                    average_other = 0
            return average_self < average_other
        return "Ошибка!"

    def __le__(self, other):
        if isinstance(other, Lecturer):
            try:
                self_rates = [x for value in self.grades.values() for x in value]
                average_self = sum(self_rates) / len(self_rates)
                other_rates = [x for value in other.grades.values() for x in value]
                average_other = sum(other_rates) / len(other_rates)
            except ZeroDivisionError:
                if len(self_rates) == 0:
                    average_self = 0
                elif len(other_rates) == 0:
                    average_other = 0
            return average_self <= average_other
        return "Ошибка!"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            try:
                self_rates = [x for value in self.grades.values() for x in value]
                average_self = sum(self_rates) / len(self_rates)
                other_rates = [x for value in other.grades.values() for x in value]
                average_other = sum(other_rates) / len(other_rates)
            except ZeroDivisionError:
                if len(self_rates) == 0:
                    average_self = 0
                elif len(other_rates) == 0:
                    average_other = 0
            return average_self == average_other
        return "Ошибка!"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка!'

    def __str__(self):
        res = f"""
Имя: {self.name}
Фамилия: {self.surname}
"""
        return res


student_eman = Student('Ruoy', 'Eman', 'male')
student_wang = Student('Li', 'Wang', 'male')

reviewer_karr = Reviewer('Anna', 'Karr')
reviewer_sotkin = Reviewer('Alexander', 'Sotkin')

lecturer_lori = Lecturer('Lucky', 'Lori')
lecturer_dann = Lecturer('Emil', 'Dann')

student_eman.courses_in_progress += ['Python', 'JavaScript', 'Web-design']
student_wang.courses_in_progress += ['Web-design']
# student_eman.finished_courses += ['Java']
student_wang.finished_courses += ['C#', 'Python']

reviewer_karr.courses_attached += ['Python']
reviewer_sotkin.courses_attached += ['JavaScript', 'Web-design']

lecturer_lori.courses_attached += ['Python']
lecturer_dann.courses_attached += ['JavaScript', 'Web-design']

student_eman.rate_lecture(lecturer_lori, 'Python', 10)
student_wang.rate_lecture(lecturer_dann, 'Web-design', 9)

student_wang.rate_lecture(lecturer_lori, 'Python', 8)
reviewer_karr.rate_hw(student_eman, 'Python', 10)
reviewer_karr.rate_hw(student_wang, 'Python', 9)
reviewer_sotkin.rate_hw(student_eman, 'JavaScript', 7)
reviewer_sotkin.rate_hw(student_wang, 'Web-design', 10)
# reviewer_sotkin.rate_hw(lecturer_lori, 'C++', 9)

print(student_wang.grades)
print(student_eman.grades)
print(student_eman)
print(student_wang)
print(lecturer_lori)
print(lecturer_dann)
print(reviewer_karr)
print(reviewer_sotkin)
print(student_eman == student_wang)
print(student_eman == lecturer_lori)
