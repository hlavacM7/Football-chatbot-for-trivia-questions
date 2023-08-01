from bs4 import BeautifulSoup
import pandas as pd
import re
import os

def process_file(file):
 
    with open(file, 'r', encoding='ISO-8859-1') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    question_divs = soup.find_all('div', style=lambda value: value is not None and 'margin-bottom:15px;background:#Ffeeee;border-radius: 12px;padding:5px;' in value)
    questions = [re.sub('^\d+\.', '', div.span.get_text(strip=True).replace('\n', ' ')) for div in question_divs if div.span is not None]

    answer_divs = soup.find_all('div', style=lambda value: value is not None and 'margin-top:5px;' in value)
    answers = [div.p.get_text(strip=True).split("was")[1] if "was" in div.p.get_text(strip=True) else div.p.get_text(strip=True) for div in answer_divs if div.p is not None]

    assert len(questions) == len(answers), "Number of questions and answers do not match."

    df = pd.DataFrame({'Question': questions, 'Answer': answers})

    return df

files = [f for f in os.listdir('pages_trivia/') if f.endswith('.html')]

dataframes = [process_file('pages_trivia/' + file) for file in files]

df = pd.concat(dataframes, ignore_index=True)

df.to_csv('trivia_questions.csv', index=False)
