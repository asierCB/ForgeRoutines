from email.policy import default

from django import forms

class RoutineGenerationForm(forms.Form):
    # Age
    age = forms.IntegerField()

    # Gender
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = forms.ChoiceField(choices=gender_choices)

    # Height and Weight
    height = forms.IntegerField(
        label='Height (in cm)',
    )
    weight = forms.IntegerField(
        label='Weight (in kg)',
    )

    # Level section
    level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advance', 'Advance'),
    ]
    level = forms.ChoiceField(
        label='Level',
        choices=level_choices,
        required=True,
    )

    # Goal
    goal_choices = [
        ('fat loss', 'Fat Loss'),
        ('muscle gain', 'Muscle Gain'),
        ('improved endurance', 'Improved Endurance'),
        ('general health', 'General Health'),
    ]
    goal = forms.ChoiceField(
        choices=goal_choices,
    )

    # Frequency
    frequency = forms.IntegerField(
        label='Workout Frequency (days per week)',
    )

    # Preferred workout style
    style_choices = [
        ('full body', 'Full Body'),
        ('split routine', 'Split Routine'),
        ('HIIT', 'HIIT'),
        ('bodyweight', 'Body Weight'),
        ('functional training', 'Functional Training'),
    ]
    style = forms.ChoiceField(
        label='Prefered Workout Style',
        choices=style_choices,
    )

    '''#Training Type
    type_choices = [
        ('strenght', 'Strength'),
        ('cardiovascular', 'Cardiovascular'),
        ('flexibility_mobility', 'Flexibility / Mobility'),
    ]
    type = forms.ChoiceField(
        label='Training Type',
        choices=type_choices,
        required=True,
    )'''

    '''# Muscular Group
    muscular_group_choices = [
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('shoulder', 'Shoulder'),
        ('arms', 'Arms'),
        ('legs', 'Legs'),
        ('quads', 'Quads'),
        ('harmstrings', 'Harmstrings'),
        ('glutes', 'Glutes'),
        ('calves', 'Calves'),
        ('adductors', 'Adductors'),
        ('abductors', 'Abductors'),
        ('core_abs', 'Core / Abs'),
    ]
    muscular_group = forms.MultipleChoiceField(
        label='Muscular Group',
        choices=muscular_group_choices,
        widget=forms.CheckboxSelectMultiple,
    )'''

    # Equipment
    equipment_choices = [
        ('nothing', 'Nothing'),
        ('complete_gym', 'Complete Gym'),
        ('dumbbells', 'Dumbbells'),
        ('kettlebell', 'Kettlebell'),
        ('pullupbar', 'Pull Up Bar'),
        ('parallelbars', 'Parallel Bars'),
        ('resistance bands', 'Resistance Bands'),
    ]
    equipment = forms.MultipleChoiceField(
        label='Equipment',
        choices=equipment_choices,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    # Duration
    duration = forms.IntegerField(
        label='Duration (in minutes)',
        required=True,
        min_value=10,

    )

    # Extra Information
    extra = forms.CharField(
        label='Extra Information',
        max_length=500,
        required=False,
        widget=forms.Textarea,
    )