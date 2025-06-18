import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from .forms import RoutineGenerationForm

# Load environment variables from .env
load_dotenv()

# Configure API KEY
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

'''class WorkoutGenerator:

    def generate_workout_routine(self, user_data):
        

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

        # model = genai.GenerativeModel('gemini-pro')
        model = genai.GenerativeModel('gemini-2.0-flash')

        try:
            response = model.generate_content(prompt)
            return json.loads(response.text)
            #return response.text
        except Exception as e:
            print(f'Error generating workout routine: {e}')
            return 'Sorry, I could not generate workout routine at this time.'
            '''


class WorkoutGenerator:
    def __init__(self, user_data, api_key = os.getenv("GOOGLE_API_KEY"), **kwargs):
        self.user_data = user_data

        genai.configure(api_key=api_key)

    def build_prompt(self):
        prompt = f"""
                    Act as a professional fitness trainer and create a personalized workout routine. 
                    Return the response ONLY as a valid JSON object with the following structure:

                    {{
                        "routine_id": "generate_unique_id",
                        "creation_date": "today's_date",
                        "user_data": {{
                                "age": {self.user_data.get('age')},
                                "gender": "{self.user_data.get('gender')}",
                                "height": "{self.user_data.get('height')}",
                                "weight": "{self.user_data.get('weight')}",
                                "level": "{self.user_data.get('level')}",
                                "goal": "{self.user_data.get('goal')}",
                                "frequency": "{self.user_data.get('frequency')}",
                                "equipment": "{self.user_data.get('equipment')}",
                                "style": "{self.user_data.get('style')}",
                                "duration": "{self.user_data.get('duration')}",
                                "extra_info": "{self.user_data.get('extra', '')}"                                        
                    }},
                        "important_conisderations": [
                            {{
                                "category": "category_name",
                                "description": "description",
                                "tips": ["tip1", "tip2", "tip3"]
                            }}
                        ],
                        "program": {{
                            "total_duration": "{self.user_data.get('duration')}",
                            "structure": [
                                {{
                                    "fase": "warm_up",
                                    "name": "Warm-up",
                                    "duration": "X minutes",
                                    "exercises": [
                                        {{
                                            "name": "exercise_name",
                                            "duration": "time_or_null",
                                            "series": "number_or_null",
                                            "repetitions": "reps_or_null",
                                            "rest": "rest_time_or_null"
                                        }}
                                    ]
                                }},
                                {{
                                    "fase": "main_workout",
                                    "name": "Main Workout",
                                    "duration": "X minutes",
                                    "description": "workout_description",
                                    "exercises": [
                                        {{
                                            "name": "exercise_name",
                                            "series": "number",
                                            "repetitions": "reps_range",
                                            "rest": "rest_time",
                                            "focus": "focus_description",
                                            "progression": {{
                                                "week": "week_number",
                                                "description": "progression_description"
                                            }}
                                        }}
                                    ]
                                }},
                                {{
                                    "fase": "cooldown",
                                    "name": "Cooldown & Stretching",
                                    "duration": "X minutes",
                                    "exercises": [
                                        {{
                                            "name": "stretch_name",
                                            "duration": "time",
                                            "description": "how_to_perform"
                                        }}
                                    ]
                                }}
                            ]
                        }},
                        "additional_tips": {{
                            "tips": [
                                {{
                                    "category": "category",
                                    "description": "description",
                                    "example": ["example1", "example2"]
                                }}
                            ]
                        }},
                        "week_progression": {{
                            "week_1": {{
                                "focus": "focus_description",
                                "intensity": "intensity_level"
                            }},
                            "week_2": {{
                                "focus": "focus_description",
                                "changes": "changes_description"
                            }}
                        }}
                    }}
                    
                    Create a complete X-week workout routine with Y training days per week based on the user data provided.
                    Generate different exercises and progressions for each week.
                    Each week should show clear progression from the previous week.
                    Ensure the JSON is valid and complete. Do not include any text outside the JSON structure.
                    """
        return prompt

    def call_gemini_api(self, prompt=None):
        if prompt is None:
            prompt = self.build_prompt()

        model = genai.GenerativeModel('gemini-2.0-flash')

        try:
            response = model.generate_content(prompt)

            content = response.text

            if content.startswith('```json'):
                content = content[7:-3]
            elif content.startswith('```'):
                content = content[3:-3]

            if content == "":
                return {"error": "Empty response from API"}

            json_data = json.loads(content)

            return json_data

        except json.JSONDecodeError as e:
            response = model.generate_content(prompt)

            print(f"JSON parsing error: {e}")
            print(f"Raw response that failed: '{response.text}'")  # 🔍 DEBUG
            return {"error": "Invalid JSON response"}

        except Exception as e:
            print(f'Error generating workout routine: {e}')
            return {"error": f"API error: {str(e)}"}


    def structure_workout_data(self, json_data = None):
        if json_data is None:
            json_data = self.call_gemini_api()

        main_exercise = []
        warmup_exercises = []

        structure = json_data.get('program', {}).get('structure', [])

        for fase in structure:
            if fase.get('fase') == 'main_workout':
                for exercise in fase.get('exercises', []):
                    exercise_row = {
                        'Exercise' : exercise.get('name', 'No name'),
                        'Series' : exercise.get('series', '-'),
                        'Repetitions' : exercise.get('repetitions', '-'),
                        'Rest' : exercise.get('rest', '-'),
                        'Focus' : exercise.get('focus', '-'),
                        'Progression' : exercise.get('progression', {}).get('description', '-') if exercise.get('progression') else '-'
                    }
                    main_exercise.append(exercise_row)

            if fase.get('fase') == 'warm_up':
                for exercise in fase.get('exercises', []):
                    exercise_row = {
                        'Exercise': exercise.get('name', 'No name'),
                        'Series': exercise.get('series', '-'),
                        'Repetitions': exercise.get('repetitions', '-'),
                        'Rest': exercise.get('rest', '-')
                    }
                    warmup_exercises.append(exercise_row)

        return main_exercise, warmup_exercises
