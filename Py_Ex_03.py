def isOdd(num):
    """Checks if the given number is odd"""
    return num % 2 != 0

def isEven(num):
    """Checks if the given number is even"""
    return num % 2 == 0

# Test 
print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))

#----------------

def getParity(num, parity):
    """Checks if the given number has the specified parity type"""
    if parity == 'odd':
        return num % 2 != 0
    elif parity == 'even':
        return num % 2 == 0
    else:
        return 'Parity indicated is unknown'

# Test 
print(getParity(1, 'odd'), getParity(1, 'even'))
print(getParity(657842, 'odd'), getParity(657842, 'even'))
print(getParity(0, 'odd'), getParity(0, 'even'))
print(getParity(-2, 'number'))

#----------------

import datetime

def greet(*, name, date):
    """Greets a person based on the time of the day"""
    if date.time() < datetime.time(12, 0):
        return f"Good Morning, {name}!"
    else:
        return f"Good Afternoon, {name}!"

# Test cases
print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
))

#-----------------

def sumAll(*lists):
    """Returns the sum of all numbers in the given lists"""
    total_sum = 0
    for lst in lists:
        total_sum += sum(lst)
    return total_sum

# Test 
test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sumAll(*test1))
print(sumAll(*test2))

#----------------------
def pig_latin(*words, suffix='ay', single=False):
    """Transforms words into Pig Latin based on the specified rules"""
    translated_words = []
    for word in words:
        if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            translated_word = word + suffix
        else:
            translated_word = word[1:] + word[0] + suffix
        translated_words.append(translated_word)
    
    if single:
        return ' '.join(translated_words)
    else:
        return translated_words

# Test cases
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1_data, **test1_config))
print(pig_latin(*test2_data, **test2_config))
print(pig_latin(*test3_data, **test3_config))
