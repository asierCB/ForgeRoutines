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

        f"Genera una rutina de entrenamiento de 1 día para una persona con los siguientes datos:\n"
        f"Nivel: {user_data.get('level')}\n"#, 'intermedio')}\n"
        #f"Objetivo: {user_data.get('objetivo', 'ganar masa muscular')}\n"
        #f"Días a la semana: {user_data.get('dias', '4')}\n"
        f'Tipo de entrenamiento: {user_data.get("type")}\n'
        f'Para trabajar los grupos musculares: {user_data.get("muscular_group")}\n'
        f"Equipo disponible: {user_data.get('equipment')}\n"#, 'mancuernas, barra, banco')}\n"
        #f"Limitaciones: {user_data.get('limitaciones', 'ninguna')}\n\n"
        f'Duración: {user_data.get("duration")} minutos\n'
        f"Estructura la rutina por días, con ejercicios, series y repeticiones. Sé conciso y ve al grano."

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

