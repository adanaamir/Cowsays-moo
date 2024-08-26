from project import user_choice, riddle, joke, ask_questions, write_responses
from unittest.mock import patch

# Since user_choice() relies on user input, we'll need to mock this input.
#mocking means instead of typing any values, youre telling python that user has typed this eg "yes" and "1" in this case
# this was achieved by using patch that replaced the normal input() wiht a fake one that gave python yes and 1 repsonse
#in mocking, the numbe rof inputs in your function should match the inputs you provide

def test_user_choice_riddles():
    with patch("builtins.input", side_effect=["yes", "1", "a candle", "n", "e"]):
        try:
            user_choice()   
        except SystemExit as e:  #the actual error message is stored in variable "e"
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"   #converting the error to string

            
def test_user_choice_jokes():
    with patch("builtins.input", side_effect=["yes", "2", "y", "n", "no", "no", "no"]):
        try:
            user_choice() 
        except SystemExit: 
            pass 

def test_user_choice_questions():
    with patch("builtins.input", side_effect=["yes", "3", "W", "Whats the meaning of life", "E", "e"]):
        try:
            user_choice()   
        except SystemExit as e:    #catching SystemExit error
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"

def test_user_choice_exit_1():
    with patch("builtins.input", side_effect=["e"]):
        try:
            user_choice()   
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"
            
def test_user_choice_exit_2():
    with patch("builtins.input", side_effect=["no", "nope", "NO"]):
        try:
            user_choice()
        except SystemExit:
            pass

def test_user_choice_exit_3():
    with patch("builtins.input", side_effect=["no", "."]):
        try:
            user_choice()
        except SystemExit:
            pass

#testing riddle() function
def test_riddle():
    with patch("builtins.input", side_effect=["idk", "yes", "a candle", "n", "e"]):
        try:
            riddle()   
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"

def test_riddle_1():
    with patch("builtins.input", side_effect=[";", "y", "a knife", "no", "e"]):
        try:
            riddle()  
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"
            
def test_riddle_2():
    with patch("builtins.input", side_effect=["light", "y", "i dont know", "n", "e"]):
        try:
            riddle()  
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"
            
def test_riddle_ValueError():
    with patch("builtins.input", side_effect=["y", "4"]):
        try:
            riddle()   
        except ValueError as e:   
            assert str(e) == "Please provide a valid response 🙂"

#testing jokes() function           
def test_jokes():
    with patch("builtins.input", side_effect=["y", "n", "e"]):
        try:
            joke()   
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"

def test_jokes_ValueError_1():
    with patch("builtins.input", side_effect=["/"]):
        try:
            joke()  
        except ValueError as e:   
            assert str(e) == "Please provide a valid response 🙂"
            
def test_jokes_ValueError_2():
    with patch("builtins.input", side_effect=["y", "yes", "no" ,"y", "q"]):
        try:
            joke()  
        except ValueError as e:   
            assert str(e) == "\nPlease choose from the list 😟"

#testing question function
def test_ask_questions():
    with patch("builtins.input", side_effect=["Whats the meaning of life", "E", "e"]):
        try:
            ask_questions()
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"
            
#testing write question function
def test_write_responses_1():
    with patch("builtins.input", side_effect=["are you real?", "W", "mom said no, sorry", "E", "e"]):
        try:
            ask_questions()   
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"
            
def test_write_responses_2():
    with patch("builtins.input", side_effect=["not a very nice question", "M", "8, it has to be 8", "E", "e"]):
        try:
            write_responses()   
        except SystemExit as e:   
            assert str(e) == "\nThank you for playing, had a fun time with you! 😙"

def test_write_responses_2():
    with patch("builtins.input", side_effect=["im paid enough not to answer your question", "/"]):
        try:
            write_responses()   
        except SystemExit:
            pass
