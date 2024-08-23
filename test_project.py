from project import user_choice, riddle, joke, ask_questions, write_questions 
import sys,pytest

def test_user_choice():
    assert user_choice("1") == riddle()
    assert user_choice("2") == joke()
    assert user_choice("3") == ask_questions

    with pytest.raises(ValueError):
        user_choice("okay")

    assert user_choice("e") == sys.exit()

def test_riddle():
    ...


def test_joke():
    ...


def test_ask_questions():
    ...


def test_write_questions():
    ...