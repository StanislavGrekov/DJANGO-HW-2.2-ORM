from django.core.management.base import BaseCommand
from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        pass

        # students = Student.objects.all()
        # for student in students:
        #     print(student.name)

        # --------------------------------Связь один ко многим____________________________________
        # appel = Company.objects.create(name = 'Appel')
        # tel_appleX = Product.objects.create(name='Apple10', company=appel, price = 100)

        # xiaomi = Company.objects.create(name = 'Xiaomi')
        # tel_redmi10 = Product.objects.create(name='Redmi10', company=xiaomi, price = 85)

        # company = Product.objects.get(id=1).company.id
        # print(company)

        # company = Product.objects.get(id=2).company.name
        # print(company)

        # prod = Product.objects.filter(company__name = 'Appel')
        # for element in prod:
        #     print(f'{element.name} - {element.price}')

        # xiaomi = Company.objects.get(name = 'Xiaomi')
        # print(xiaomi.id)
        #
        # for element in xiaomi.product_set.all():
        #     print(f'{element.name} - {element.price}')
        #
        #
        # print(xiaomi.product_set.count())

        # xiaomi = Company.objects.get(name='Xiaomi')
        # xiaomi_prod = xiaomi.product_set.filter(name__istartswith = 'Redmi10')
        # for element in xiaomi_prod:
        #     print(f'{element.name} - {element.price}')

        # samsung_company = Company.objects.create(name = "Samsung")
        # samsung_prod_1 = samsung_company.product_set.create(name = 'Galaxy10', price = 95)

        # my_company = Company.objects.get(name = 'Xiaomi')
        # new_prod = my_company.product_set.create(name = 'Redmi 4 Pro', price = 56)
        # my_prod = my_company.product_set.all()
        # for element in my_prod:
        #     print(f'{element.name} - {element.price}')

        # --------------------------------Связь многие ко многим____________________________________

        # student_1 = Student.objects.create(name = 'Tom')
        # student_2 = Student.objects.create(name='Bob')
        #
        # student_3 = Student.objects.create(name = 'Max')
        # student_4 = Student.objects.create(name='Ivan')
        #
        # student_1.courses.create(name = 'Algebra')
        # student_2.courses.create(name='Algebra')
        # student_3.courses.create(name = 'History')
        # student_4.courses.create(name = 'History')

        # student_5 = Student.objects.create(name='Semen')
        # student_5.courses.create(name = 'Algebra')
        # student_5.courses.create(name = 'History')

        # Все курсы студента
        # courses = Student.objects.get(name = 'Semen').courses.all()
        # for course in courses:
        #     print(course.name)
        # Все студенты, которые посещают курс алгебры
        # students = Student.objects.filter(courses__name = 'Algebra')
        # for student in students:
        #     print(student.name)

        # Фильтрация по имени
        #         student = Student.objects.filter(name='Semen')
        #         for element in student:
        #             print(element.id)

        # course_python = Course.objects.create(name='C++')
        # course_python.student_set.create(name='Gena')

        # students = Student.objects.all()
        # for student in students:
        #     print(student.name)
        #
        # courses = Course.objects.all()
        # for course in courses:
        #     print(course.name)

        # student_7 = Student.objects.create(name='Lexa')
        # perl = Course.objects.create(name = 'Perl')
        # perl.courses.add(student_7)

        # Получение Всех курсов одного студента
        # student_3 = Student.objects.create(name = 'Max')
        # student_3.courses.create(name='Algebra')
        # student_3.courses.create(name='History')
        # for course in Student.objects.get(name = 'Max').courses.all():
        #     print(course.name)

        # Взаимосвязь через related_name

        # python = Course.objects.create(name = "Python")
        # python.cour.create(name='Lexa')
        # python.cour.create(name="Semen")
        #
        # students = python.cour.all()
        #
        # for student in students:
        #     print(student.name)

        # --------------------------------Связь многие ко многим через промежуточную таблицу____________________________________

        # python = Course.objects.create(name='Python')
        #
        # sam = Student.objects.create(name='Sam')
        # tom = Student.objects.create(name='Tom')
        #
        # sam_python = Enrollment(student = sam, course = python, date = '2022-10-22', mark=4)
        # tom_python = Enrollment(student=tom, course=python, date='2022-10-23', mark=5)
        # tom_python.save()
        # sam_python.save()
        #
        # # request = Enrollment.objects.all()
        # # for element in request:
        # #     print(element)
        #
        # tom_courses = tom.courses.all()
        # print(tom_courses[0].name)
        #
        # student_all = python.student_set.all()
        # for element in student_all:
        #     print(element.name)

        # создадим курсы
        django = Course.objects.create(name="Django")
        python = Course.objects.create(name="Python")
        java = Course.objects.create(name="Java")

        # создадим студента
        bob = Student.objects.create(name="Bob")

        # добавляем курс для студента bob
        bob.courses.add(django, through_defaults={"date": date.today(), "mark": 5})
        # создаем курс для студента bob
        bob.courses.create(name="C++", through_defaults={"date": date.today(), "mark": 4})

        # получаем все курсы Boba
        print(bob.courses.all().values_list())

        # переустанавливаем курсы для студента bob
        # bob.courses.set([python, java], through_defaults={"date": date.today(), "mark": 4})