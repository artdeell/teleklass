# Generated by Django 4.1.4 on 2022-12-22 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActualCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(verbose_name='Количество баллов')),
            ],
            options={
                'verbose_name': 'Акутаальный курс',
                'verbose_name_plural': 'Акутальные курсы',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('max_mark', models.IntegerField(verbose_name='Максимальное количество баллов')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('patronymic', models.TextField(verbose_name='Отчество')),
                ('login', models.TextField(verbose_name='Логин')),
                ('password', models.TextField(verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
        ),
        migrations.CreateModel(
            name='Pizdos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('patronymic', models.TextField(verbose_name='Отчество')),
                ('login', models.TextField(verbose_name='Логин')),
                ('password', models.TextField(verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер задания')),
                ('name', models.TextField(verbose_name='Название задания')),
                ('mark', models.IntegerField(verbose_name='Максимальный балл')),
                ('description', models.TextField(verbose_name='Описание задания')),
                ('type', models.IntegerField(verbose_name='Тип задания')),
                ('img', models.ImageField(upload_to='', verbose_name='Картинка задания')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.course')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст варианта')),
                ('status', models.BooleanField(verbose_name='Правильность варианта')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.task')),
            ],
            options={
                'verbose_name': 'Выарианет ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('patronymic', models.TextField(verbose_name='Отчество')),
                ('login', models.TextField(verbose_name='Логин')),
                ('password', models.TextField(verbose_name='Пароль')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.parent')),
            ],
            options={
                'verbose_name': 'Ребёнок',
                'verbose_name_plural': 'Дети',
            },
        ),
        migrations.CreateModel(
            name='ActualTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(verbose_name='Количество баллов')),
                ('time', models.TimeField(verbose_name='Время выполнеия задания')),
                ('count', models.IntegerField(verbose_name='Количество ответов')),
                ('status', models.BooleanField(verbose_name='Статус выполнения')),
                ('actual_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.actualcourse')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.task')),
            ],
            options={
                'verbose_name': 'Акутальное задание',
                'verbose_name_plural': 'Акутальные задания',
            },
        ),
        migrations.AddField(
            model_name='actualcourse',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.child'),
        ),
        migrations.AddField(
            model_name='actualcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.course'),
        ),
    ]
