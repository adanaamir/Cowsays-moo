# Cowsays-moo
#### Video Demo:  <URL HERE>
#### Description:
This is a fun and interactive program where users can enjoy riddles, jokes, ask questions and get responses from random characters. This program has 4 main functions: 
1.  Riddles:  A random character will ask you riddles and you'll have to crack them.
2.  Jokes:  If you're in a mood for some humor, a character will tell you jokes.
3.  ask_questions:  You can ask any question and a random character will answer them.
4.  write_responses:  This function is a sub part of "ask_questions" where you can write hilarious responses.

#### Libraries Used:
- cowsay
- json
- sys
- random
- cvs

### Files Included: 


#### project.py:
The first file "project.py" is the main file in which all of the code is written. It has 4 functions as described above. 


#### before.csv:
The second file "before.csv" is the file in which all of the riddles, its answers, and jokes are saved. These jokes and riddles are displayed by reading this csv file.


#### responses.json:
The third file "responses.json" is a json file in which all of the responses to the questions that user asks, are saved. User can also write responses to this json file (with the help of the "write_responses" function).


#### requirements.txt:
The fourth file "requirements.txt" is a text file in which all of the libraries used, have been mentioned in one line.


#### test_project.py:
The fifth file "test_project.py" is a pytest file, in which all of the tests have been written to ensure the main file "project.py" is working properly. It has 16 tests, testing all of the functions in the main file.