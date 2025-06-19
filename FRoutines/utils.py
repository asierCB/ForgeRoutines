import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from .forms import RoutineGenerationForm
from datetime import date

# Load environment variables from .env
load_dotenv()

# Configure API KEY
#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class WorkoutGenerator:
    def __init__(self, user_data, api_key = os.getenv("GOOGLE_API_KEY"), **kwargs):
        self.user_data = user_data

        genai.configure(api_key=api_key)

    def build_prompt(self):

        prompt_dict = {
                "routine_id": "generate_unique_id",
                "creation_date": {date.today()},
                "user_data": {
                        "age": self.user_data.get('age'),
                        "gender": self.user_data.get('gender'),
                        "height": self.user_data.get('height'),
                        "weight": self.user_data.get('weight'),
                        "level": self.user_data.get('level'),
                        "goal": self.user_data.get('goal'),
                        "frequency": self.user_data.get('frequency'),
                        "equipment": self.user_data.get('equipment'),
                        "style": self.user_data.get('style'),
                        "duration": self.user_data.get('duration'),
                        "extra_info": self.user_data.get('extra', '')
                },
                "important_considerations": [
                    {
                        "category": "category_name",
                        "description": "description",
                        "tips": ["tip1", "tip2", "tip3"]
                    }
                ],
                "program": {
                    "total_duration": self.user_data.get('duration'),
                    "training_days": [
                        {
                            "day": "Day 1",
                            "focus": "e.g., Full Body, Upper Body, Legs",
                            "warm_up": {
                                "duration": "X minutes",
                                "exercises": [
                                    {
                                        "name": "exercise_name",
                                        "duration": "time_or_null",
                                        "series": "number_or_null",
                                        "repetitions": "reps_or_null",
                                        "rest": "rest_time_or_null"
                                    }
                                ]
                            },
                            "main_workout": {
                                "duration": "X minutes",
                                "description": "workout_description",
                                "exercises": [
                                    {
                                        "name": "exercise_name",
                                        "series": "number",
                                        "repetitions": "reps_range",
                                        "rest": "rest_time",
                                        "focus": "focus_description"
                                    }
                                ]
                            },
                            "cooldown": {
                                "duration": "X minutes",
                                "exercises": [
                                    {
                                        "name": "stretch_name",
                                        "duration": "time",
                                        "description": "how_to_perform"
                                    }
                                ]
                            }
                        },
                        {
                            "day": "Day 2",
                            "focus": "e.g., Cardio, Core, Rest",
                            "warm_up": {
                                "duration": "X minutes",
                                "exercises": [
                                    {
                                        "name": "exercise_name",
                                        "duration": "time_or_null",
                                        "series": "number_or_null",
                                        "repetitions": "reps_or_null",
                                        "rest": "rest_time_or_null"
                                    }
                                ]
                            },
                            "main_workout": {
                                "duration": "X minutes",
                                "description": "workout_description",
                                "exercises": [
                                    {
                                        "name": "exercise_name",
                                        "series": "number",
                                        "repetitions": "reps_range",
                                        "rest": "rest_time",
                                        "focus": "focus_description"
                                    }
                                ]
                            },
                            "cooldown": {
                                "duration": "X minutes",
                                "exercises": [
                                    {
                                        "name": "stretch_name",
                                        "duration": "time",
                                        "description": "how_to_perform"
                                    }
                                ]
                            }
                        }
                        # ... Add more 'training_day' objects based on user_data.frequency
                    ]
                },
                "additional_tips": {
                    "tips": [
                        {
                            "category": "category",
                            "description": "description",
                            "example": ["example1", "example2"]
                        }
                    ]
                },
                "week_progression": {
                    "week_1": {
                        "focus": "focus_description",
                        "intensity": "intensity_level",
                        "daily_details": {
                            "day_1": "summary of changes or specifics for day 1 of week 1",
                            "day_2": "summary of changes or specifics for day 2 of week 1"
                        }
                    },
                    "week_2": {
                        "focus": "focus_description",
                        "changes": "changes_description",
                        "daily_details": {
                            "day_1": "summary of changes or specifics for day 1 of week 2",
                            "day_2": "summary of changes or specifics for day 2 of week 2"
                        }
                    }
                    # ... Add more weeks as needed"
                }
            }
        prompt = "Act as a professional fitness trainer and create a personalized workout routine. Return the response ONLY as a valid JSON object with the following structure:"
        prompt += str(prompt_dict)#json.dumps(prompt_dict, indent= 4)
        prompt += f"""
                Create a complete X-week workout routine with Y training days per week based on the user data provided.
                Generate different exercises and progressions for each week.
                Each week should show clear progression from the previous week.
                Ensure the JSON is valid and complete. Do not include any text outside the JSON structure.
            
                If I asking you for a X day routines do not include a rest day includes on that days
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

        '''
        In this part I am preparing the introduction of the workout routine.
        '''
        info = []
        info_structure = json_data.get('important_considerations', [])

        for part in info_structure:
            info_output = {
                'category': part.get('category', 'N/A'),
                'description': part.get('description', 'N/A'),
                'tips': part.get('tips', 'N/A'),
            }
            info.append(info_output)

        '''
        In this part of the code I am preparing the list for the exercises (warmup, cooldown and main exercises)
        '''
        structured_days_data = []
        structure = json_data.get('program', {}).get('training_days', [])

        for index, day_data in enumerate(structure):
            day_output = {
                'day_name': day_data.get('day', f'Day {index + 1}'),
                'focus': day_data.get('focus', 'N/A'),
                'warmup_exercises': [],
                'main_exercises': [],
                'cooldown_exercises': []
            }

            # Process Warm-Up Exercise
            for exercise in day_data.get('warm_up', {}).get('exercises', []):
                day_output['warmup_exercises'].append({
                    'Exercise': exercise.get('name', 'No name'),
                    'Duration': exercise.get('duration', '-'),
                    'Series': exercise.get('series', '-'),
                    'Repetitions': exercise.get('repetitions', '-'),
                    'Rest': exercise.get('rest', '-')
                })

            # Process Main Workout
            for exercise in day_data.get('main_workout', {}).get('exercises', []):
                day_output['main_exercises'].append({
                    'Exercise' : exercise.get('name', 'No name'),
                    'Series' : exercise.get('series', '-'),
                    'Repetitions' : exercise.get('repetitions', '-'),
                    'Rest' : exercise.get('rest', '-'),
                    'Focus' : exercise.get('focus', '-'),
                    #'Progression' : exercise.get('progression', {}).get('description', '-') if exercise.get('progression') else '-'
                })

            # Process Cooldown
            for exercise in day_data.get('cooldown', {}).get('exercises', []):
                day_output['cooldown_exercises'].append({
                    'Exercise': exercise.get('name', 'No name'),
                    'Duration': exercise.get('duration', '-'),
                    'Description': exercise.get('description', '-')
                })


            structured_days_data.append(day_output)
        return structured_days_data, info

