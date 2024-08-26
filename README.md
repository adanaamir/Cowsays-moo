# Cowsays-moo
#### Video Demo:  <URL HERE>
#### Description:
This is a fun and interactive program where users can enjoy riddles, jokes, ask questions and get responses from random characters. This program has 4 main functions: 
1.  riddle:  A random character will ask you riddles and you'll have to crack them.
2.  joke:  If you're in a mood for some humor, a character will tell you jokes.
3.  ask_questions:  You can ask any question and a random character will answer them.
4.  write_responses:  This function is a sub part of "ask_questions" where you can write hilarious responses.

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