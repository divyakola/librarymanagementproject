# Generated by Django 2.0.4 on 2018-05-23 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=50)),
                ('isbnno', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('bookid', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('issuedate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('user_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('m_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='r',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booklib.Student'),
        ),
    ]
