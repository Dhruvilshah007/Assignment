from cgi import test
from email.policy import default
from django.contrib import admin
from .models import *


admin.site.register(login_user)
admin.site.register(courses)
admin.site.register(group)
admin.site.register(classes)
admin.site.register(questions)
admin.site.register(Test_All)
admin.site.register(institute)
