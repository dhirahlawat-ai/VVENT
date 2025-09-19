import random
from database import *

def find_sentiment(text: str):
    text = text.lower()
    happy_count = sum(text.count(word) for word in happy_keywords)
    sad_count = sum(text.count(word) for word in sad_keywords)
    stress_count = sum(text.count(word) for word in stress_keywords)
    angry_count = sum(text.count(word) for word in angry_keywords)
    
    values = {"happy": happy_count, "sad": sad_count, "stress": stress_count, "angry": angry_count}

    sentiment = max(values, key=values.get)
    return sentiment

first = input("Start venting:\n")
users_senti = find_sentiment(first)
response = random.choice(responses[users_senti])

while True:
    user_input = input(response+"\n")
    if user_input.lower() == "exit":
        break
    senti = find_sentiment(user_input)
    response = random.choice(responses[senti])
