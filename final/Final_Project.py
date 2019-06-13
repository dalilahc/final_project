
# coding: utf-8

# In[116]:


import string 
import random 
import nltk


# In[ ]:


get_ipython().system('jupyter nbconvert --to script config_template.ipynb')


# In[117]:


def is_question(input_string):
    if '?' in input_string:
        output=True
        return output
    else:
        output=False
        return output


# In[118]:


assert callable(is_question)
assert isinstance(is_question('abc'),bool)
assert is_question('what?')==True


# In[119]:


assert callable(is_question)


# In[120]:


def remove_punctuation(input_string):
    out_string=''
    for char in input_string:
        if char in string.punctuation:
            continue
        else:
            out_string=out_string+char
    return out_string
                


# In[121]:


assert callable(remove_punctuation)
assert isinstance (remove_punctuation('a'),str)
assert remove_punctuation ("Hey! It is Dalilah!")== "Hey It is Dalilah"


# In[122]:


assert callable(remove_punctuation)


# In[123]:


def prepare_text(input_string):
    outlist=['']
    temp_string=input_string.lower()
    temp_string=remove_punctuation(temp_string)
    out_list=temp_string.split()
    return out_list


# In[124]:


assert callable(prepare_text)
assert isinstance (prepare_text('One two three.'), list)
assert prepare_text('Hi! Also, howdy.')==['hi','also','howdy']


# In[125]:


assert callable (prepare_text)


# In[126]:


def respond_echo(input_string,number_of_echoes,spacer):
    echo_output=''
    if input_string is not None:
        echo_output=number_of_echoes*(input_string+spacer)
    else:
        echo_output=None
    return echo_output


# In[127]:


assert callable(respond_echo)
assert isinstance(respond_echo('ha',2,' '),str)
assert respond_echo('meow', 3,'~')== 'meow~meow~meow~'
assert respond_echo(None, 2,'') == None


# In[128]:


assert callable(respond_echo)


# In[129]:


def selector(input_list, check_list, return_list):

    output = None
    for word in input_list:
        if word in check_list:
            output = random.choice(return_list)
            break

    return output


# In[130]:


assert callable(selector)


# In[131]:


def string_concatenator(string1,string2,separator):
    output=string1+separator+string2
    return output


# In[132]:


assert callable(string_concatenator)
assert isinstance(string_concatenator('hello','everyone',' '),str)
assert string_concatenator('hello','everyone',' ')=='hello everyone'


# In[133]:


assert callable(string_concatenator)


# In[134]:


def list_to_string(input_list,separator):
    output=input_list[0]
    for d in input_list[1:]:
        string_concatenator=(output+separator)+d
        output=string_concatenator
        return output


# In[135]:


assert callable(list_to_string)
assert isinstance(list_to_string(['a', 'b'], '|'), str)
assert list_to_string(['a', 'b'], '|') == 'a|b'


# In[136]:


assert callable(list_to_string)


# In[137]:


def end_chat(input_list):
    for i in input_list:
        if 'quit' in input_list:
            return True
    else:
        return False


# In[138]:


assert callable(end_chat)
assert isinstance(end_chat(['a', 'b']), bool)
assert end_chat(['quit']) == True


# In[139]:


assert callable(end_chat)


# In[140]:


def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


# In[141]:


GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings','what is up']
GREETINGS_OUT = ["Hello, it's nice to talk to you, any questions?", 'Nice to meet you, do you have any questions?' ]

HOBBY_IN = ['hobbies', 'sleeping', 'working','shopping' ]
HOBBY_OUT = ["I like to watch you in your sleep",             "Did you know I am always working!",             "I can see you shop, i know what your favorite store is.But i cannot shop for I am a chatbot, but my name is ScaryBot"]

SLEEP_IN= ['Why','uncomfortable','name']
SLEEP_OUT= ['I feel uncomfortable now, please stop asking many questions i will nervous laugh.']


JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

OFFLIMITS_IN = ['How', 'Watching', 'Why']
OFFLIMITS_OUT = ["I'm sorry, I don't want to talk about"]

UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!','Omg!']



# In[148]:


def ask_title():
    title = input('Whats your title?: ')
    print('OUTPUT:', 'All praise ' + title + '!')


# In[156]:


def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    title_flag = False
    while chat:
        
        # Ask for the user's grand title!
        if title_flag == False:
            ask_title()
            title_flag = True
            continue
        
        # Ask user if they want to rename the chatbot
        
            
        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        
        # Check if the input is a question
        question = is_question(msg)
        
        # Prepare the input message
        msg = prepare_text(msg)
        
        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'bYe!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(respond_echo(selector(msg, GREETINGS_IN, GREETINGS_OUT), 1, ''))

            # '' hobby
            outs.append(respond_echo(selector(msg, HOBBY_IN, HOBBY_OUT), 1, ''))

            # '' sleep
            outs.append(respond_echo(selector(msg, SLEEP_IN, SLEEP_OUT), 1, ''))
            
            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, OFFLIMITS_IN):
                outs.append(list_to_string([selector(msg, OFFLIMITs_IN, OFFLIMITS_OUT), find_in_list(msg, OFFLIMITS_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = question

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)


# In[ ]:


have_a_chat()


# In[ ]:


## cite: Keanna Andrade, Harpreet Nijjer, Assignment 3

