from django.db import models


class login_user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class courses(models.Model):
    courses_name = models.CharField(max_length=100)

    def __str__(self):
        return self.courses_name


class group(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name


class classes(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class questions(models.Model):
    questions_name = models.CharField(max_length=100)
    courses_names = models.ForeignKey(
        courses, on_delete=models.CASCADE, blank=True, null=True)
    group_name = models.ForeignKey(
        group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.questions_name


class Test_All(models.Model):
    test_name = models.CharField(max_length=200)
    question = models.ForeignKey(
        questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class institute(models.Model):
    institute_name = models.CharField(max_length=100)
    course_name = models.ForeignKey(
        courses, on_delete=models.CASCADE)
    group_name = models.ForeignKey(
        group, on_delete=models.CASCADE)
    class_name = models.ManyToManyField(
        'classes', related_name='classes')

    def __str__(self):
        return self.institute_name
