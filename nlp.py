import nltk
from nltk.tokenize import word_tokenize

def process_text(text):
    tokens = word_tokenize(text.lower())
    return tokens

def interpret_command(tokens):
    if 'weather' in tokens or 'temperature' in tokens:
        return 'weather'
    elif 'time' in tokens or 'clock' in tokens:
        return 'time'
    elif 'reminder' in tokens or 'remind' in tokens:
        return 'reminder'
    elif 'date' in tokens:
        return 'date'
    elif 'day' in tokens:
        return 'day'
    elif 'month' in tokens:
        return 'month'
    elif 'year' in tokens:
        return 'year'
    elif 'name' in tokens or 'your name' in tokens:
        return 'name'
    elif 'purpose' in tokens or 'do' in tokens:
        return 'purpose'
    elif 'joke' in tokens:
        return 'joke'
    elif 'quote' in tokens:
        return 'quote'
    elif 'creator' in tokens or 'created' in tokens:
        return 'creator'
    elif 'age' in tokens:
        return 'age'
    elif 'help' in tokens:
        return 'help'
    else:
        return 'unknown'
