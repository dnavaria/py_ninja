from faker import Faker
import random

fobj = Faker()

# returns list of random words
#fobj.words(number_of_words) 

# return random digit
#fobj.random_digit()

def generate_num_list(length: int) -> list:
    return [fobj.random_int() for y in range(length)]

def generate_ranged_num_list(a: int, b: int,length: int) -> list:
    return [fobj.random_int(a,b) for y in range(length)]

def choose_input(data: list):
    randomize = random.choice([0,1])
    if randomize:
        print("randomizing input.....")
        displacement = fobj.random_int(1,9)
        return random.choice(data)+displacement
    return random.choice(data)

def remove_dups(data: list) -> list:
    return list(set(data))

