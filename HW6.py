class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        gpa_self_sub = 0
        gpa_other_sub = 0
        number_self = 0
        number_other = 0
        for course_name, grade in self.grades.items():
            gpa_self_sub += sum(grade)
            number_self += len(grade)
        for course_name, grade in other.grades.items():
            gpa_other_sub += sum(grade)
            number_other += len(grade)
        gpa_self = gpa_self_sub / number_self
        gpa_other = gpa_other_sub / number_other
        return gpa_self < gpa_other
    def __str__(self):
        gpa_self_sub = 0
        number_self = 0
        for course_name, grade in self.grades.items():
            gpa_self_sub += sum(grade)
            number_self += len(grade)
        gpa_self = gpa_self_sub / number_self
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {gpa_self}'
        return res

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        gpa_self_sub = 0
        gpa_other_sub = 0
        number_self = 0
        number_other = 0
        for course_name, grade in self.grades.items():
            gpa_self_sub += sum(grade)
            number_self += len(grade)
        for course_name, grade in other.grades.items():
            gpa_other_sub += sum(grade)
            number_other += len(grade)
        gpa_self = gpa_self_sub / number_self
        gpa_other = gpa_other_sub / number_other
        return gpa_self < gpa_other
    def __str__(self):
        gpa_self_sub = 0
        number_self = 0
        for course_name, grade in self.grades.items():
            gpa_self_sub += sum(grade)
            number_self += len(grade)
        gpa_self = gpa_self_sub / number_self
        str_courses_in_progress = ' ,'.join(self.courses_in_progress)
        str_finished_courses = ' ,'.join(self.finished_courses)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {gpa_self}\nКурсы в процессе изучения: {str_courses_in_progress}\nЗавершенные курсы: {str_finished_courses}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

 
first_student = Student('Ruoy', 'Eman', 'gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']

second_student = Student('Leeroy', 'Jenkins', 'male')
second_student.courses_in_progress += ['Python']
 
first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Samanta', 'Blobby')
second_reviewer.courses_attached += ['Python']

first_lecturer = Lecturer('Sam', 'Bob')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Tam', 'Mops')
second_lecturer.courses_attached += ['Python']
 
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Git', 9)
first_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 10)


first_student.rate_lecturers(first_lecturer, 'Python', 9)
second_student.rate_lecturers(second_lecturer, 'Python', 10)
second_student.rate_lecturers(second_lecturer, 'Python', 10)



def students_gpa(students):
    studens_all_dict = {}
    for student in students:
        for w, e in student.items():
            if w in studens_all_dict.keys():
                studens_all_dict[w] += e
            else:
                studens_all_dict[w] = e
    for course_name, grade in studens_all_dict.items():
        gpa = sum(grade) / len(grade)
        print(f'Курс: {course_name} Средний бал: {gpa}')

def lecturers_gpa(lecturers):
    lecturers_all_dict = {}
    for lecturers in lecturers:
        for w, e in lecturers.items():
            if w in lecturers_all_dict.keys():
                lecturers_all_dict[w] += e
            else:
                lecturers_all_dict[w] = e
    for course_name, grade in lecturers_all_dict.items():
        gpa = sum(grade) / len(grade)
        print(f'Курс: {course_name} Средний бал: {gpa}')



print(first_lecturer < second_lecturer)
print(first_student < second_student)

print(first_reviewer)
print(first_student)
print(first_lecturer)
print(students_gpa([first_student.grades, second_student.grades]))
print(lecturers_gpa([first_lecturer.grades, second_lecturer.grades]))