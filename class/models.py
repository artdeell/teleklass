from django.db import models

class Parent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField('Имя')
    surname = models.TextField('Фамилия')
    patronymic = models.TextField('Отчество')
    login = models.TextField('Логин')
    password = models.TextField('Пароль')

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    def __str__(self):
        return str(f"{self.name}<->{self.surname}")

class Child(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField('Имя')
    surname = models.TextField('Фамилия')
    patronymic = models.TextField('Отчество')
    login = models.TextField('Логин')
    password = models.TextField('Пароль')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Ребёнок"
        verbose_name_plural = "Дети"

    def __str__(self):
        return str(f"{self.name}<->{self.surname}")

class Course(models.Model):
    name = models.TextField('Название')
    max_mark = models.IntegerField('Максимальное количество баллов')
    description = models.TextField('Описание')

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return str(f"{self.name}")

class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField("Номер задания")
    name = models.TextField('Название задания')
    mark = models.IntegerField("Максимальный балл")
    description = models.TextField("Описание задания")
    type = models.IntegerField('Тип задания')
    img = models.ImageField("Картинка задания")

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return str(f"{self.name}")



class ActualCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mark = models.IntegerField('Количество баллов')
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Акутаальный курс"
        verbose_name_plural = "Акутальные курсы"

    def __str__(self):
        return str(f"{self.name}")
        
class ActualTask(models.Model):
    actual_course = models.ForeignKey(ActualCourse, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    mark = models.IntegerField("Количество баллов")
    time = models.TimeField('Время выполнеия задания')
    count = models.IntegerField('Количество ответов')
    status = models.BooleanField('Статус выполнения')

    class Meta:
        verbose_name = "Акутальное задание"
        verbose_name_plural = "Акутальные задания"

    def __str__(self):
        return str(f"{self.name}<->{self.task}")

class Variant(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField('Текст варианта')
    status = models.BooleanField('Правильность варианта')

    class Meta:
        verbose_name = "Выарианет ответа"
        verbose_name_plural = "Варианты ответов"

    def __str__(self):
        return str(f"{self.task}<->{self.status}")