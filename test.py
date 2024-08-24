import pytest
from project import user_choice
from unittest.mock import patch


# Since user_choice() relies on user input, we'll need to mock this input.
def test_user_choice(monkeypatch):
    #iter() is used to test multiple inputs, it iterates over the list of inputs
    inputs = iter(["yes", "1"])

    #builtins.input() refers to the builtin input function
    #the next() function return the next value from an iterator i-e "1" each time the lambda function is called
    #lambda takes one argument which is not used so _ is used as a placeholder , the function simulates input() by returning the next value from the inputs iterator
    #when input() is called during the test, it will now use the lambda function, which provides the next value from inputs, instead of waiting for actual user input.

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    user_choice()


