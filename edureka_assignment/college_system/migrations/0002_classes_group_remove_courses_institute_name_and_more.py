# Generated by Django 4.0.4 on 2022-04-26 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='courses',
            name='institute_name',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='user',
        ),
        migrations.AddField(
            model_name='institute',
            name='course_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='college_system.courses'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='courses_names',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='college_system.courses'),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_system.questions')),
            ],
        ),
        migrations.AddField(
            model_name='institute',
            name='class_name',
            field=models.ManyToManyField(related_name='classes', to='college_system.classes'),
        ),
        migrations.AddField(
            model_name='institute',
            name='group_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='college_system.group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='group_name',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='college_system.group'),
            preserve_default=False,
        ),
    ]