"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from Final_Project import is_question, remove_punctuation, respond_echo, ask_question

##
##

def is_question():

    assert callable(is_question)
    assert isinstance(is_question('abc'),bool)
    assert is_question('what?')==True

def remove_punctuation():

    assert callable(remove_punctuation)
    assert isinstance (remove_punctuation('a'),str)
    assert remove_punctuation ("Hey! It is Dalilah!")== "Hey It is Dalilah"
    
def respond_echo():
    
    assert callable(respond_echo)
    assert isinstance(respond_echo('ha',2,' '),str)
    assert respond_echo('meow', 3,'~')== 'meow~meow~meow~'
    assert respond_echo(None, 2,'') == None
    
def ask_question(self):
        # Override the Python built-in input method 
        Final_Project.input = lambda: 'test'
        # Call the function you would like to test (which uses input)
        output = Final_Project.ask_question()  
        assert output == 'OUTPUT: All praise ' + 'test!'
'