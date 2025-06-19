from django.shortcuts import render
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from .forms import RoutineGenerationForm

# Load environment variables from .env
load_dotenv()

# Configure API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_workout_routine(user_data):
    '''
    This is the function that generates the workout routine. This receives the information from the
    template and introduces it intro de prompt
    '''

    '''prompt = (
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
    )'''

    prompt = f"""
            Act as a professional fitness trainer and create a personalized workout routine. 
            Return the response ONLY as a valid JSON object with the following structure:

            {{
                "rutina_id": "generate_unique_id",
                "fecha_creacion": "today's_date",
                "datos_usuario": {{
                    "edad": {user_data.get('age')},
                    "genero": "{user_data.get('gender')}",
                    "altura": "{user_data.get('height')}",
                    "peso": "{user_data.get('weight')}",
                    "nivel": "{user_data.get('level')}",
                    "objetivo": "{user_data.get('goal')}",
                    "frecuencia": "{user_data.get('frequency')}",
                    "equipamiento": "{user_data.get('equipment')}",
                    "estilo": "{user_data.get('style')}",
                    "duracion": "{user_data.get('duration')}",
                    "info_extra": "{user_data.get('extra', '')}"
                }},
                "consideraciones_importantes": [
                    {{
                        "categoria": "category_name",
                        "descripcion": "description",
                        "consejos": ["tip1", "tip2", "tip3"]
                    }}
                ],
                "programa": {{
                    "duracion_total": "{user_data.get('duration')}",
                    "estructura": [
                        {{
                            "fase": "warm_up",
                            "nombre": "Warm-up",
                            "duracion": "X minutes",
                            "ejercicios": [
                                {{
                                    "nombre": "exercise_name",
                                    "duracion": "time_or_null",
                                    "series": "number_or_null",
                                    "repeticiones": "reps_or_null",
                                    "descanso": "rest_time_or_null"
                                }}
                            ]
                        }},
                        {{
                            "fase": "main_workout",
                            "nombre": "Main Workout",
                            "duracion": "X minutes",
                            "descripcion": "workout_description",
                            "ejercicios": [
                                {{
                                    "nombre": "exercise_name",
                                    "series": "number",
                                    "repeticiones": "reps_range",
                                    "descanso": "rest_time",
                                    "enfoque": "focus_description",
                                    "progresion": {{
                                        "semana": "week_number",
                                        "descripcion": "progression_description"
                                    }}
                                }}
                            ]
                        }},
                        {{
                            "fase": "cooldown",
                            "nombre": "Cooldown & Stretching",
                            "duracion": "X minutes",
                            "ejercicios": [
                                {{
                                    "nombre": "stretch_name",
                                    "duracion": "time",
                                    "descripcion": "how_to_perform"
                                }}
                            ]
                        }}
                    ]
                }},
                "consejos_adicionales": {{
                    "tips": [
                        {{
                            "categoria": "category",
                            "descripcion": "description",
                            "ejemplos": ["example1", "example2"]
                        }}
                    ]
                }},
                "progresion_semanal": {{
                    "semana_1": {{
                        "enfoque": "focus_description",
                        "intensidad": "intensity_level"
                    }},
                    "semana_2": {{
                        "enfoque": "focus_description",
                        "cambios": "changes_description"
                    }}
                }}
            }}

            Create a complete workout routine based on the user data provided. 
            Ensure the JSON is valid and complete. Do not include any text outside the JSON structure.
            """

    #model = genai.GenerativeModel('gemini-pro')
    model = genai.GenerativeModel('gemini-2.0-flash')

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f'Error generating workout routine: {e}')
        return 'Sorry, I could not generate workout routine at this time.'


def create_routine_view(request):
    '''
    This is the function that creates the routine view.
    '''

    from .utils import WorkoutGenerator

    if request.method == "POST":
        form = RoutineGenerationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            #print(user_data)
            #routine_text = generate_workout_routine(user_data)

            routine_text = WorkoutGenerator(user_data)

            routine, info = routine_text.structure_workout_data()

        else:
            routine = 'Error generating workout routine'
            info = 'Error generating workout routine'
            print('Error generating workout routine')

        context = {
            'form':form,
            'routine': routine,
            'info': info,
        }

        return render(request, 'routine_input_form.html', context)
    else:
        form = RoutineGenerationForm()
        context = {
            'form': form
        }
        return render(request, 'routine_input_form.html', context)

