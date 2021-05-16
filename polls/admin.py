from django.contrib import admin

from .models import Question, Choice


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


# class ChoiceInline(admin.StackedInline):    -> show design take a lot of screen
class ChoiceInline(admin.TabularInline):  # save screen square
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # inline ChoiceInline in to QuestionAdmin in admin website when create new question
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # show 3 column in admin web
    list_filter = ['pub_date']   # show filter table in admin web
    search_fields = ['question_text'] # show search field in admin web


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Choice)