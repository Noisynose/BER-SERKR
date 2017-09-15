import datetime

from django import forms
from django.forms import ModelForm, BaseModelFormSet
from django.utils.translation import ugettext_lazy as _

from .models import *

class LoginForm (forms.Form):
    email = forms.EmailField (label='Email', max_length=254)
    password = forms.CharField (widget=forms.PasswordInput)
    
class ProgramForm (ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'auto_update_stats', 'rounding', 'repeatable']
        """labels = {
            'rep_scheme': _('Prefered rep scheme'),
        }"""
        help_texts = {
            'start_date': _('Start date will be used to plan your workouts.'),
            'rep_scheme': _('Will help you build your program, can be changed for each exercise later.'),
            'auto_update_stats': _('Uncheck this if you don''t want the system to automatically log your new PRs.'),
        }

class WorkoutForm (ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'day_of_week']
        
class WorkoutExerciseForm (ModelForm):
    loading = forms.IntegerField(required=True, min_value=0)
    notes_formt = forms.CharField(required=False)
    
    class Meta:
        model = Workout_Exercise
        fields = ['id', 'exercise', 'sets', 'reps', 'rep_scheme', 'weight', 'percentage', 'rpe', 'is_amrap', 'notes']
        
    def __init__(self, *args, **kwargs):
        # Calling Django's init
        lifter_id = kwargs.pop('lifter')
        super(WorkoutExerciseForm, self).__init__(*args, **kwargs)
       
        # Custom fields
        self.fields['exercise'].choices = Exercise.get_exercise_select(lifter_id)
        self.fields['notes_formt'].initial = self.instance.notes_formt()
        
        # Manage loading
        if self.instance.rep_scheme == 'MAX_PERCENTAGE':
            self.fields['loading'].initial = self.instance.percentage
        elif self.instance.rep_scheme == 'RPE':
            self.fields['loading'].initial = self.instance.rpe
        elif self.instance.rep_scheme == 'WEIGHT':
            self.fields['loading'].initial = self.instance.weight

    def save(self, commit=True):
        # Manage loading
        print(self.instance)
        if self.cleaned_data['rep_scheme'] == 'MAX_PERCENTAGE':
            self.instance.percentage = self.cleaned_data['loading']
            self.instance.rpe = None
            self.instance.weight = None
        elif self.cleaned_data['rep_scheme'] == 'RPE':
            self.instance.rpe = self.cleaned_data['loading']
            self.instance.percentage = None
            self.instance.weight = None
        elif self.cleaned_data['rep_scheme'] == 'WEIGHT':
            self.instance.weight = self.cleaned_data['loading']
            self.instance.percentage = None
            self.instance.rpe = None
        
        return super(WorkoutExerciseForm, self).save(commit=commit)
    
class WorkoutLogForm (ModelForm):
    class Meta:
        model = Workout_Log
        fields = ['workout_date']
        
class WorkoutExerciseLogForm (ModelForm):    
    notes_formt = forms.CharField(required=False)
    
    class Meta:
        model = Workout_Exercise_Log
        fields = ['id', 'exercise', 'sets', 'reps', 'weight', 'rpe', 'is_amrap', 'notes']
        
    def __init__(self, *args, **kwargs):
       # Calling Django's init
       lifter_id = kwargs.pop('lifter')
       super(WorkoutExerciseLogForm, self).__init__(*args, **kwargs)
       
       # Custom fields
       self.fields['exercise'].choices = Exercise.get_exercise_select(lifter_id) 
       self.fields['notes_formt'].initial = self.instance.notes_formt()      

class LogByExerciseForm (forms.Form):
    exercise = forms.ChoiceField (label='Exercise', choices=Exercise.get_exercise_select())
       
class ProfileForm (ModelForm):
    # Redefine constructor to customize
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].disabled = True
    
    class Meta:
        model = Lifter
        fields = ['email', 'first_name', 'last_name', 'age', 'sex', 'measurement_system']
        
class ChangePasswordForm (forms.Form):
    password = forms.CharField (label='New password', required=False, widget=forms.PasswordInput)
    confirm_password = forms.CharField (label='Confirm password', required=False, widget=forms.PasswordInput)
    
class BodyweightForm (ModelForm):
    class Meta:
        model = Lifter_Weight
        fields = ['entry_date', 'weight']
        
class CustomExerciseForm (ModelForm):    
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'category', 'has_stats']
        
    def __init__(self, *args, **kwargs):
       # Calling Django's init
       super(CustomExerciseForm, self).__init__(*args, **kwargs)
       
       # Custom fields
       self.fields['has_stats'].label = 'Manage stats'

class StatForm (ModelForm):
    # Redefine constructor to enforce required fields
    def __init__(self, *args, **kwargs):
        lifter_id = kwargs.pop('lifter')
        super(StatForm, self).__init__(*args, **kwargs)
        
        self.fields['weight'].required = True
        self.fields['reps'].required = True
        self.fields['exercise'].choices = Exercise.get_exercise_select(lifter_id)         
    
    class Meta:
        model = Lifter_Stats
        fields = ['exercise', 'entry_date', 'weight', 'reps']