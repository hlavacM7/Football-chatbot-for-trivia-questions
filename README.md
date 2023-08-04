<h1 align="center">Chatbot Trivia</h1>

<p align="justify">
This is a simple Natural Language Processing (NLP) project that implements a chatbot capable of answering trivia questions. The chatbot uses cosine similarity to find the best match between user input and the available questions in the database. The project also includes a simple Flask application that serves as an interface for the chatbot.
</p>

<h2>Files</h2>

<ul>
<li><code>chatbot.py</code>: This file contains the main functionality of the chatbot. It uses cosine similarity to match the user's question with the questions in the known database and provides the best answer it can find.</li>
<li><code>app.py</code>: This is the Flask application file. It sets up a web interface where users can interact with the chatbot.</li>
<li><code>scraper.py</code>: This file scrapes football-related trivia questions and answers from a specified source and adds them to the chatbot's knowledge base.</li>
<li><code>home.html</code>: The main HTML file for the Flask application's interface.</li>
<li><code>styles.css</code>: The CSS file that provides styling for the Flask application's interface.</li>
<li><code>requirements.txt</code>: List of all the Python libraries needed. </li>
</ul>
<p>The database was constructed by scraping HTML files from https://www.funtrivia.com/ and then by asking ChatGPT some basic questions to fill in the knowledge gaps. Overall, it contains 2000 questions.</p>

<h2>Testing Results</h2>

<p>After some testing, the bot has shown the following weaknesses:</p>

<ul>
<li><b>Too many stopwords:</b> If a question consists only of stopwords or only one meaningful word, the bot is often incorrect due to the cosine similarity and stopwords filtering.</li>
<li><b>Distinguishing between teams and players:</b> Questions like "Who is the top scorer in the Champions League?" can be problematic as the bot has trouble recognizing whether the user is asking about a team or a player.</li>
<li><b>Answering general questions:</b> A question like "Who is the best American football player?" can be problematic because it's too general, and the model might not find similarities.</li>
</ul>

<h2>Summary</h2>
<p align="justify">
This project serves as a basic, end-to-end application in the domain of Natural Language Processing (NLP). By implementing a chatbot capable of answering trivia questions, it provides an illustrative example of how NLP can be applied in a practical scenario. Using techniques like cosine similarity for matching user queries with existing questions in the database, the application showcases some fundamental aspects of information retrieval in NLP. Even tho it's accuracy is not the best it can be easily scalable by creating larger database. My goal wasn't to build sophisticated large language model, instead i wanted to build my first end-to-end application that showcases basic NLP concepts and also has something on top provided by the Flask application. Moving forward, this project will serve as a valuable starting point in the broader study of NLP, laying a solid foundation upon which more complex and sophisticated NLP applications can be built.
</p>

<p>Link: https://footballtriviachat.onrender.com</p>
<p>In case this link isn't working here is a video demo: https://youtu.be/Ju-FzBnRioc </p>
