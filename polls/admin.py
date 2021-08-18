from django.contrib import admin
from .models import Choice, Question

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'publ_date'], 'classes': ['collapse']}),
    ]

    list_display = ('question_text', 'publ_date', 'was_published_recently')
    list_filter = ['publ_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
