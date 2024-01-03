from emotion import Emotion
import pandas as pd
import os
import openai
import random
from transformers import GPT2LMHeadModel, GPT2Tokenizer

openai.api_key = "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"

 # openai api token
emotion = Emotion() # loading emotion detector

# loading and cleaning datasets
train_df = pd.read_csv('archive/train.txt', names=['text', 'emotion'], sep=';')
test_df = pd.read_csv('archive/test.txt', names=['text', 'emotion'], sep=';')

train_df = emotion.process_data(train_df)
test_df = emotion.process_data(test_df)

predictor = emotion.model(train_df,test_df) # training model

random_responses = ['Hello, I am Emobot ! How can I help you today ?', 'Hi, my name is Emobot, what can I do for you ?', 'Good day, allow me to present myself : I am Emobot, your emotional chat companion !']
random_hello = ['hello', 'hi', 'hey', 'heyy', 'good day']

# function to generate a response based on user input and the detected emotion
def generate_gpt3_response(user_input):
    # Prepend the detected emotion to the user input
    if (user_input.lower() in random_hello):
        return random.choice(random_responses)

    detected_emotion = emotion.emotion_detection(predictor, user_input)  # Replace with your emotion detection logic
    input_text = f"User is feeling {detected_emotion}. {user_input}"

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": input_text}
        ]
    )
    
    try:
        input_text = completion['choices'][0]['message']['content']
        if input_text is not None:
            return input_text
        else:
            return "Failed to generate response"
    except KeyError:
        return "Failed to extract input text from OpenAI response"

# Example usage
#user_input = input("You: ")

#while user_input not in ['exit', 'quit']:
#    response = generate_gpt3_response(user_input)
#    print("Bot:", response)
#    user_input = input("You: ")
    
    