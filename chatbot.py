import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import random
import re
import string
import pandas as pd

df_test = pd.read_csv("archive/test.txt")
df_train = pd.read_csv("archive/train.txt")
df_val = pd.read_csv("archive/val.txt")

def process_dataset(df):
    if (df):
        df.apply()
    else:
        print("slay")

def process_document(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup with 'lxml' as the parser
        soup = BeautifulSoup(response.content, 'lxml')

        # Get all paragraphs using find_all('p')
        paragraphs = soup.find_all('p')

        # Extract lowercase text from each paragraph and remove tags, symbols, and digits
        paragraphs_text = [re.sub(r'<[^>]+>', ' ', re.sub(r'[^a-zA-Z\s]', ' ', paragraph.get_text().lower())) for paragraph in paragraphs]

        # Tokenize words
        tokenized_words = [word_tokenize(sentence) for sentence in paragraphs_text]

        # Lemmatize words and remove punctuation
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [
            [lemmatizer.lemmatize(word) for word in words if word.isalnum()]  # Remove punctuation
            for words in tokenized_words
        ]

        return lemmatized_words

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Example usage:
hiv_who = "https://www.who.int/news-room/fact-sheets/detail/hiv-aids?gclid=Cj0KCQiAyeWrBhDDARIsAGP1mWSx7WbkfT1KFTbF2Av9exhL647vUeh4Wa-DwHtqcwi9M20jveQ4SGwaAlOqEALw_wcB"
hiv_wiki = "https://en.wikipedia.org/wiki/HIV"
hiv_cdc = "https://www.cdc.gov/hiv/basics/whatishiv.html"
processed_hiv_who = process_document(hiv_who)
processed_hiv_wiki = process_document(hiv_wiki)
processed_hiv_cdc = process_document(hiv_cdc)
