# Cowsays-moo
#### Video Demo: (https://youtu.be/AKIYT9C4ayE)
#### Description:
"Cowsays-moo" is an engaging and interactive Python program designed to bring a smile to your face with riddles, jokes, and quirky character responses. Inspired by the classic "cowsay" program, this project introduces four primary functions that users can explore for fun and entertainment:

Riddle: This feature challenges the user with riddles presented by a random character. It’s an excellent way to test your problem-solving skills and have some fun cracking the answers.

Joke: If you're in need of a good laugh, this function is for you. A character of the program will deliver a joke, chosen randomly from a collection of humorous snippets. It’s perfect for lightening the mood.

Ask Questions: Curious about something? Ask away! In this mode, you can pose any question, and a random character will provide an answer. The responses range from witty and humorous to surprisingly insightful, adding a playful twist to the typical Q&A format.

Write Responses: This is a specialized sub-function of the "Ask Questions" feature. It allows users to contribute by writing their own humorous or clever responses, which will be stored and potentially used to answer future questions. This makes the program dynamic and continuously evolving based on user input.


#### Libraries Used:
- cowsay
- json
- sys
- random
- csv

### Files Included: 


#### project.py:
The first file "project.py" is the main file containing all the code. It has 4 functions as described above. 


#### before.csv:
The second file "before.csv" stores all the riddles, its answers, and jokes. These are displayed by reading this csv file.


#### responses.json:
The third file "responses.json" stores all of responses to the questions that user asks. User can also add new responses using "write_responses" function.


#### requirements.txt:
The fourth file "requirements.txt" mentiones all the libraries used in one line.


#### test_project.py:
The fifth file "test_project.py" is a pytest file, containing 16 tests to ensure the main file "project.py" is working properly.