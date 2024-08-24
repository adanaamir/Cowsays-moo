import pytest
from project import user_choice
from unittest.mock import patch

# Since user_choice() relies on user input, we'll need to mock this input.
#mocking means instead of typing any values, youre telling python that user has typed this eg "yes" and "1" in this case
# this was achieved by using patch that replaced the normal input() wiht a fake one that gave python yes and 1 repsonse

def test_user_choice_riddles():
    with patch("builtins.input", side_effect=["yes", "1"]):
        try:
            user_choice()   
        except Exception as e:  #the actual error message is stored in variable "e"
            pytest.fail(f"An error occurred: {e}")
            
def test_user_choice_jokes():
    with patch("builtins.input", side_effect=["yes", "2"]):
        try:
            user_choice()   
        except Exception as e:  #the actual error message is stored in variable "e"
            pytest.fail(f"An error occurred: {e}")

def test_user_choice_questions():
    with patch("builtins.input", side_effect=["yes", "3"]):
        try:
            user_choice()   
        except Exception as e:  #the actual error message is stored in variable "e"
            pytest.fail(f"An error occurred: {e}")

def test_user_choice_exit():
    with patch("builtins.input", side_effect=["no", "1"]):
        try:
            user_choice()   
        except Exception as e:  #the actual error message is stored in variable "e"
            pytest.fail(f"An error occurred: {e}")



