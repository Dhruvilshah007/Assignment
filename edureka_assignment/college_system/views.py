from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random

from . models import *


def index(request):
    all_question = questions.objects.all()

    total_question = all_question.count()

    random_number = random.randint(1, total_question)

    number = questions.objects.get(pk=random_number)

    if number.courses_names is not None and number.group_name is None:
        print("This question has  course name")
        all_questions__of_coursename = questions.objects.filter(
            courses_names=number.courses_names)
        print(all_questions__of_coursename)

    elif number.group_name is not None and number.courses_names is None:
        print("This question has  group name")
        all_questions__of_groupname = questions.objects.filter(
            group_name=number.group_name)
        print(all_questions__of_groupname)

    else:
        print("This questionis individual")

    return HttpResponse(f"Done- {random_number}")
