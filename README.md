<h1 align="center">Chatbot Trivia</h1>

<p align="justify">
This is a simple Natural Language Processing (NLP) project that implements a chatbot capable of answering trivia questions. The chatbot uses cosine similarity to find the best match between user input and the available questions in the database. The project also includes a simple Flask application that serves as an interface for the chatbot.
</p>
<h2>Link: https://footballtriviachat.onrender.com </h2>

<h2>Files</h2>

<ul>
<li><code>chatbot.py</code>: This file contains the main functionality of the chatbot. It uses cosine similarity to match the user's question with the questions in the known database and provides the best answer it can find.</li>
<li><code>app.py</code>: This is the Flask application file. It sets up a web interface where users can interact with the chatbot.</li>
<li><code>scraper.py</code>: This file scrapes football-related trivia questions and answers from a specified source and adds them to the chatbot's knowledge base.</li>
<li><code>home.html</code>: The main HTML file for the Flask application's interface.</li>
<li><code>styles.css</code>: The CSS file that provides styling for the Flask application's interface.</li>
</ul>
<p>The database was populated by scraping HTML files from https://www.funtrivia.com/ and then by asking ChatGPT some basic questions to fill the knowledge gaps.</p>

<h2>Testing Results</h2>

<p>After some testing, the bot has shown the following weaknesses:</p>

<ul>
<li><b>Too many stopwords:</b> If a question consists only of stopwords or only one meaningful word, the bot is often wrong due to the cosine similarity and stopwords filtering.</li>
<li><b>Distinguishing between teams and players:</b> Questions like "Who is the top scorer in the Champions League?" can be problematic as the bot has trouble recognizing whether you are asking about a team or a player.</li>
<li><b>Answering general questions:</b> A question like "Who is the best American football player?" can be problematic because it's too general and the model might not find similarities.</li>
</ul>
