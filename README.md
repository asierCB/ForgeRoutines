# ForgeRoutines

A Django-based web application that generates personalized workout routines using Google's Generative AI API. ForgeRoutines creates customized fitness plans based on user preferences and displays them in an intuitive, tabbed interface.

## 🏋️‍♂️ Features

- **AI-Powered Routine Generation**: Leverages Google's Generative AI to create personalized workout routines
- **Interactive Interface**: Clean, responsive design with Bootstrap tabs for easy navigation
- **Comprehensive Workout Structure**: Includes warm-up, main exercises, and cooldown sections
- **Detailed Exercise Information**: Provides sets, reps, duration, and focus areas for each exercise
- **General Fitness Tips**: AI-generated advice and tips for better workout performance

## 🚀 Technologies Used

- **Backend**: Django 5.2.3 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.6
- **AI Integration**: Google Generative AI API (google-generativeai 0.8.5)
- **Data Format**: JSON processing and manipulation
- **Template Engine**: Django Templates
- **Environment Management**: python-dotenv for configuration
- **Database**: SQLite (default Django database)

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8+
- pip (Python package manager)
- Google Generative AI API key
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/asierCB/ForgeRoutines.git
   cd ForgeRoutines
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Main dependencies include:**
   - Django 5.2.3
   - google-generativeai 0.8.5
   - python-dotenv 1.1.0
   - And other supporting libraries for Google API integration

4. **Set up environment variables**
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 🎯 How It Works

### 1. User Input
Users fill out a form with their fitness preferences, goals, and constraints through a clean Bootstrap interface.

### 2. Structured API Request (`WorkoutGenerator` Class)
The application uses a custom `WorkoutGenerator` class in `utils.py` that:
- **Builds complex prompts**: Creates detailed JSON schema templates that guide the AI response
- **Configures Google Gemini API**: Uses the `gemini-2.0-flash` model for content generation
- **Handles user data**: Processes form inputs (age, gender, fitness level, goals, equipment, etc.)
- **Manages API authentication**: Securely loads API keys from environment variables

### 3. JSON Response Processing
The AI response undergoes sophisticated processing:
- **Response cleaning**: Removes markdown code blocks (````json`) from API responses
- **Error handling**: Implements retry logic and comprehensive error catching
- **JSON validation**: Parses and validates the structured workout data
- **Data transformation**: Converts raw JSON into template-ready data structures

### 4. Data Structuring (`structure_workout_data` method)
The application processes the JSON response into two main components:
- **General Information**: Extracts fitness tips, categories, and important considerations
- **Daily Routines**: Organizes workouts by day with separate sections for:
  - Warm-up exercises (with duration, series, reps, rest)
  - Main exercises (with series, reps, rest, focus areas)
  - Cooldown activities (with duration and descriptions)

### 5. Template Rendering
Django templates dynamically render the workout data using:
- **Template variables** to display exercise information
- **Template loops** to iterate through days and exercises  
- **Conditional rendering** for different exercise types
- **Bootstrap tabs** for organized content presentation

## 📁 Project Structure

```
ForgeRoutines/
├── ForgeRoutines/          # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── FRoutines/              # Django app
│   ├── migrations/
│   ├── static/
│   │   └── img/
│   │       └── logo.jpg
│   ├── templates/
│   │   ├── routine_display.html
│   │   └── routine_input_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── venv/                   # Virtual environment
├── .env                    # Environment variables
├── .gitignore
├── db.sqlite3             # SQLite database
├── manage.py
├── README.md
└── requirements.txt
```

## 🔧 Key Learning Points

This project demonstrates several important concepts:

### Google API Integration
- **API Authentication**: Secure handling of API keys using environment variables and python-dotenv
- **Gemini 2.0 Flash Model**: Integration with Google's latest generative AI model
- **Complex Prompt Engineering**: Designing detailed JSON schema templates to ensure consistent API responses
- **Response Handling**: Advanced processing including markdown cleanup and error recovery

### JSON Data Management
- **Structured Prompting**: Creating comprehensive JSON templates that guide AI output format
- **Response Validation**: Robust JSON parsing with error handling for malformed responses
- **Data Transformation**: Converting nested JSON structures into Django-friendly data formats
- **Schema Design**: Implementing complex nested structures for workout routines with multiple exercise types

### Advanced Python Techniques
- **Class-based Architecture**: Using the `WorkoutGenerator` class for organized API management
- **Environment Configuration**: Secure API key management with dotenv
- **Error Handling**: Comprehensive exception handling for API failures and JSON parsing errors
- **Data Processing**: Complex data restructuring from API responses to template variables

### Django Template System
- **Dynamic Content Rendering**: Using template variables to display complex workout data structures
- **Template Logic**: Implementing loops and conditionals for nested exercise data
- **Component Organization**: Separating general information from daily workout routines
- **Frontend Integration**: Seamlessly combining Django backend processing with Bootstrap frontend components

## ⚙️ Technical Implementation Details

### WorkoutGenerator Class
The core functionality is built around a sophisticated `WorkoutGenerator` class that handles:

```python
# Key features of the implementation:
- Complex JSON schema generation for AI prompts
- Google Gemini 2.0 Flash model integration
- Automatic response cleaning and validation
- Structured data transformation for Django templates
```

### API Response Processing
- **Smart Response Cleaning**: Automatically removes markdown formatting from API responses
- **Retry Logic**: Implements fallback mechanisms for failed API calls  
- **Data Validation**: Comprehensive JSON parsing with detailed error reporting
- **Flexible Schema**: Handles varying response formats while maintaining structure

### Data Flow Architecture
1. **Form Input** → User preferences collected via Django forms
2. **Prompt Building** → Complex JSON template construction
3. **API Call** → Google Gemini API request with structured prompts
4. **Response Processing** → JSON cleaning, validation, and parsing
5. **Data Structuring** → Transformation into template-ready format
6. **Template Rendering** → Dynamic HTML generation with Bootstrap styling

The application features:
- **Responsive Design**: Works on desktop and mobile devices
- **Tabbed Navigation**: Easy switching between workout days and general information
- **Clean Layout**: Professional appearance with proper spacing and typography
- **Interactive Elements**: Bootstrap components for enhanced user experience

## 🔮 Future Enhancements

- User authentication and profile management
- Workout progress tracking
- Exercise video integration
- Social features for sharing routines
- Mobile app development
- Advanced AI customization options

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Generative AI for providing the AI capabilities
- Bootstrap team for the excellent CSS framework
- Django community for the robust web framework

---

**Note**: This project was developed as a learning exercise to explore AI integration, JSON data handling, and Django template rendering. It showcases practical application of modern web development techniques combined with artificial intelligence.