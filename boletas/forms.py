from django.forms import ModelForm, inlineformset_factory
from .models import Task, Calificacion, Plan, Performance, StudentEntry, Attendance, AttendanceEntry, CalificacionAdult, CalificacionBabies, ResponsibilityNote, Comment, FeedbackNote
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']

class GradeForm(ModelForm):
    class Meta:
        model = Calificacion
        fields = ['student_name', 'level', 'unit', 'unit_exam_grade', 'speaking_grade', 'spelling_grade', 'verbs_grade', ]

        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_exam_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'speaking_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'spelling_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'verbs_grade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class GradeBabiesForm(ModelForm):
    class Meta:
        model = CalificacionBabies
        fields = ['student_name', 'level', 'unit', 'unit_exam_grade', 'speaking_grade', 'spelling_grade', 'pronunciation_grade', ]

        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_exam_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'speaking_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'spelling_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'pronunciation_grade': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class GradeAdultForm(ModelForm):
    class Meta:
        model = CalificacionAdult
        fields = ['student_name', 'level', 'unit', 'unit_exam_grade', 'speaking_grade', 'spelling_grade', 'verbs_grade', 'writing_grade']

        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_exam_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'speaking_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'spelling_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'verbs_grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'writing_grade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['day', 'topic', 'unit', 'clase', 'activities', 'book_pages', 'resources', 'expected_learning']

        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'clase': forms.TextInput(attrs={'class': 'form-control'}),
            'activities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'book_pages': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'resources': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'expected_learning': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = []

class StudentEntryForm(ModelForm):
    class Meta:
        model = StudentEntry
        fields = ['student_name', 'comments']

        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = []

class AttendanceEntryForm(ModelForm):
    class Meta:
        model = AttendanceEntry
        fields = ['student_name', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'monday': forms.TextInput(attrs={'class': 'form-control'}),
            'tuesday': forms.TextInput(attrs={'class': 'form-control'}),
            'wednesday': forms.TextInput(attrs={'class': 'form-control'}),
            'thursday': forms.TextInput(attrs={'class': 'form-control'}),
            'friday': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResponsibilityNoteForm(forms.ModelForm):
    class Meta:
        model = ResponsibilityNote
        fields = ['note']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class FeedbackNoteForm(forms.ModelForm):
    class Meta:
        model = FeedbackNote
        fields = ['feedback']