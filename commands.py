import datetime
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the voice
voices = engine.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_weather():
    now = datetime.datetime.now()
    hour = now.hour

    if 6 <= hour < 18:
        return "The weather is sunny."
    elif 18 <= hour < 20:
        return "The weather is cloudy."
    else:
        return "It is night time."

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def get_day():
    now = datetime.datetime.now()
    return now.strftime("%A")

def get_month():
    now = datetime.datetime.now()
    return now.strftime("%B")

def get_year():
    now = datetime.datetime.now()
    return now.strftime("%Y")

def get_name():
    return "I am your voice assistant."

def get_purpose():
    return "I can help you with various tasks like telling the time, weather, setting reminders, and more."

def tell_joke():
    return "Why don't scientists trust atoms? Because they make up everything!"

def give_quote():
    return "The only way to do great work is to love what you do. - Steve Jobs"

def get_creator():
    return "I was created by a team of developers."

def get_age():
    return "I don't have an age, but I'm always here to help!"

def set_reminder(reminder):
    return f"Reminder set: {reminder}"

def help_user():
    return "Sure, what do you need help with?"

def execute_command(command, text):
    if command == 'weather':
        response = get_weather()
    elif command == 'time':
        response = get_time()
    elif command == 'date':
        response = get_date()
    elif command == 'day':
        response = get_day()
    elif command == 'month':
        response = get_month()
    elif command == 'year':
        response = get_year()
    elif command == 'name':
        response = get_name()
    elif command == 'purpose':
        response = get_purpose()
    elif command == 'joke':
        response = tell_joke()
    elif command == 'quote':
        response = give_quote()
    elif command == 'creator':
        response = get_creator()
    elif command == 'age':
        response = get_age()
    elif command == 'reminder':
        response = set_reminder(text)
    elif command == 'help':
        response = help_user()
    else:
        response = "Sorry, I don't understand that command."

    speak(response)
    return response