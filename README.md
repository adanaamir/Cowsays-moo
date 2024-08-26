# Cowsays-moo
#### Video Demo:  <URL HERE>
#### Description:
This program features three main functions:
1. Riddles: A random character will ask you riddles and you'll have to crack them.
2. Jokes: If you're in a mood for some humor, a character will tell you jokes.
3. Questions: You can ask any question and a random character will answer them. You can even add some hilarious responses.

The first file "project.py" is the main file in which all of the code is written. It has 4 functions as described above. The forth function "write_questions" is a sub part of the function "ask_questions". 

The second file "before.csv" is the file in which all of the riddles, its answers, and jokes are saved. These jokes and riddles are displayed by reading this csv file.

The third file "responses.json" is a json file in which all of the responses to the questions that user asks, are saved. User can also write responses to this json file (withi the help of the "write_questions" function).

The fourth file "requirements.txt" is a text file in which all of the libraries used, have been mentioned in one line.

The fifth file "test_project.py" is a pytest file, in which all of the tests have been written to ensure the main file "project.py" is working correctly. It has 16 test, testing all of the fucntions in the main file.