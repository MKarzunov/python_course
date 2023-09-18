from random import randint, sample, randrange


class Person:
    possible_sex = {'мужской', 'женский'}

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        if sex in self.possible_sex:
            self.sex = sex
        else:
            raise NameError('Неверный пол')


class Teacher(Person):
    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)
        self.students_taught: int = 0

    def teach(self, topic: str, *args):
        for pupil in args:
            pupil.take(topic)
            self.students_taught += 1


class Student(Person):
    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)
        self.knowledge = []

    def __len__(self):
        return len(self.knowledge)

    def take(self, topic: str):
        self.knowledge.append(topic)

    def forget(self):
        if self.knowledge:
            self.knowledge.pop(randrange(len(self.knowledge)))


class Materials:
    def __init__(self, *args):
        self.topics = list(args)

    def __len__(self):
        return len(self.topics)


themes = Materials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')

teacher = Teacher('Иванов Иван Петрович', 53, 'мужской')

students_data = (('Сахарова Ирина Петровна', 23, 'женский'),
                 ('Федоров Егор Васильевич', 26, 'мужской'),
                 ('Степанова Мария Сергеевна', 19, 'женский'),
                 ('Уткин Федор Евгеньевич', 22, 'мужской'))

students = [Student(*data) for data in students_data]

for theme in themes.topics:
    students_set = sample(students, k=randint(1, len(students)))
    teacher.teach(theme, *students_set)

for student in students:
    print(student.knowledge)

for student in students:
    student.forget()

print('-' * 30)

for student in students:
    print(student.knowledge)
    print(len(student))
