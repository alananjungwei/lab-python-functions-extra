
import string

def get_unique_list_f(lst):

    unique_list = []
    for item in lst:

        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def count_case_f(string_input):

    upper_count = 0
    lower_count = 0

    for char in string_input:
        if char.isupper():
            upper_count += 1

        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

def remove_punctuation_f(sentence):

    clean_sentence = ""

    for char in sentence:
        
        if char not in string.punctuation:
            clean_sentence += char
        
    return clean_sentence

def word_count_f(sentence):

    clean_sentence = remove_punctuation_f(sentence)

    words = clean_sentence.split()

    return len(words)