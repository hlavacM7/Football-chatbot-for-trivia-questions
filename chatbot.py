from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import numpy as np
import pandas as pd

#nltk.download("punkt")
#nltk.download("wordnet")
#nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    tokens = [token for token in tokens if token not in stopwords.words("english")]
    return " ".join(tokens)

df = pd.read_csv("trivia_questions.csv")
df["Proccesed Question"] = df["Question"].apply(preprocess_text)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Proccesed Question"])

def get_response(user_input):
    user_input = preprocess_text(user_input)
    user_input_vector = vectorizer.transform([user_input])
    cosine_similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    most_similar_question_idx = np.argmax(cosine_similarities)

    return df["Answer"][most_similar_question_idx]

#user_input = input("Enter a Question: ")
#response = get_response(user_input)
#print(response)