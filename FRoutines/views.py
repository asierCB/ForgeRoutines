from django.shortcuts import render
import os
import google.generativeai as genai
from dotenv import load_dotenv
from .forms import RoutineGenerationForm

# Load environment variables from .env
load_dotenv()

# Configure API KEY
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

def generate_workout_routine(user_data):
    '''
    This is the function that generates the workout routine. This receives the information from the
    template and introduces it intro de prompt
    '''

    prompt = (
        #String with the information
        #f' Generate a 1 day training routine for a person using the following data:\n'
        #f"Level: {user_data.get('level')}\n"#, 'intermedio')}\n"
        #f"Objetivo: {user_data.get('objetivo', 'ganar masa muscular')}\n"
        #f"Días a la semana: {user_data.get('dias', '4')}\n"
        #f'Training Type: {user_data.get("type")}\n'
        #f'Muscular Groups: {user_data.get("muscular_group")}\n'
        #f"Equipmetn Available: {user_data.get('equipment')}\n"#, 'mancuernas, barra, banco')}\n"
        #f"Limitaciones: {user_data.get('limitaciones', 'ninguna')}\n\n"
        #f'Duration: {user_data.get("duration")} minutos\n'
        #f'Extra Information: {user_data.get("extra")}\n'
        #f"Estructura la rutina por días, con ejercicios, series y repeticiones. Sé conciso y ve al grano."


        f"Act as a professional fitness trainer and create a personalized workout routine for me. I want a plan that "
        f"includes both strength training and cardio, tailored to my fitness level, goals, available equipment, and schedule. "
        f"Here are my details:\n"

        f"Age:{user_data.get('age')}\n"
        f"Gender:{user_data.get('gender')}\n"
        f"Height / Weight:{user_data.get('height')} and {user_data.get('weight')}\n"
        f"Fitness level: {user_data.get('level')}\n"
        f"Goal:{user_data.get('goal')}\n"
        f"Workout frequency:{user_data.get('frequency')}\n"
        f"Available equipment (you do not have to use all of them):{user_data.get('equipment')}\n"
        f"Preferred workout style:{user_data.get('style')}\n"
        f"Workout duration:{user_data.get('duration')}\n"
        f"Extra information:{user_data.get('extra')}\n"
        
        f"Please include warm-up, main exercises, and cooldown / stretching.Provide sets, reps, and rest time.Also, "
        f"include tips or progressions for each week if possible."
    )

    #model = genai.GenerativeModel('gemini-pro')
    model = genai.GenerativeModel('gemini-1.5-flash')

    try:
        response = model.generate_content(prompt)
        return response.text, prompt
    except Exception as e:
        print(f'Error generating workout routine: {e}')
        return 'Sorry, I could not generate workout routine at this time.'


def create_routine_view(request):
    '''
    This is the function that creates the routine view.
    '''

    if request.method == "POST":
        form = RoutineGenerationForm(request.POST)
        if form.is_valid():
            # Over here is where I have to configure the form from the template
            user_data = form.cleaned_data
            print(user_data)
            routine_text, prompt = generate_workout_routine(user_data)
        else:
            routine_text = 'Error generating workout routine'
            prompt = 'Error generating workout routine'
            print('Error generating workout routine')

        context = {
            'form':form,
            'routine': routine_text,
            'prompt': prompt
        }

        return render(request, 'routine_display.html', context)
    else:
        form = RoutineGenerationForm()
        context = {
            'form': form
        }
        return render(request, 'routine_input_form.html', context)

