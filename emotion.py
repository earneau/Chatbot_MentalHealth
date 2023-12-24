import pandas as pd
import numpy as np
import neattext.functions as nfx

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

class Emotion:

    def process_data(df):
        if 'text' in df:
            df['clean text'] = df['text'].apply(nfx.remove_userhandles)
            df['clean text'] = df['clean text'].apply(nfx.remove_stopwords)

        return df
    
    def model(train, test):
        if 'text' in train and 'emotion' in train:
            x_train = train['clean text']
            y_train = train['emotion']

        if 'text' in test and 'emotion' in test:
            x_test = test['clean text']
            y_test = test['emotion']

        pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])
        pipe_lr.fit(x_train,y_train)

        print(pipe_lr.score(x_test,y_test))

        return pipe_lr
    
    
    def emotion_detection(predictor, sample):
       
       emotion = predictor.predict([sample])
       detected_emotion = emotion[0]

       return detected_emotion


