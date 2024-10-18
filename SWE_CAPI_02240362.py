###############################
"https://github.com/Sonamdorji1904/SWE_CAP1_Dzo_Spell_Checker.git"


# Sonam Dorji
# 1st SWE A
# 02240362
###############################

# REFERENCES
"https://sqlpad.io/tutorial/python-download-file-from-url/#:~:text=Here's%20how%20you'd%20tell,request%20was%20successful%20if%20response."

## Problem Statement:
" You are tasked with creating a spell checker for the Dzongkha language. Your program should read a Dzongkha text file (dzo.txt) that contains multiple spelling errors which will be provided by the tutor (refer Accessing Input File section). The program should identify and report these errors. "

###############################
# SOLUTION
###############################


import requests

def download_file(url, output_filename):
    data = requests.get(url)
    with open(output_filename, 'wb') as file:
        file.write(data.content)
    print(f"Downloaded: {output_filename}")

# Example usage
download_file("https://csf101-server-cap1.onrender.com/get/input/362", "362.txt")


print("Converting.........................")



from docx import Document
import re 

# Defining a function where it will erase all characters apart from dzongkha characters
def clean(text):
    # filters everything that are not Dzongkha characters (U+0F00 to U+0FFF) and whitespaces
    cleaned_text = re.sub(r'[^\u0F00-\u0FFF\s]', '', text)
    
    # Returns the cleaned text with each word on new line
    return '\n'.join(cleaned_text.split())

# Reading the .docx file
doc = Document('dictionary.docx') 

# Get the text contained in the document
doc_text = '\n'.join([para.text for para in doc.paragraphs])

# Processes the text in order to remove all but Dzongkha letters
cleaned_txt = clean(doc_text)

# It writes the modified content into a new file
with open('dictionary.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_txt)

print("You have successfully converted and cleaned your .docx file in 'dictionary.txt' ")


# Load dictionary words into a set for fast lookup
def dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(each_word.strip() for each_word in file)

# Load the input text file line by line
def input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Check for misspelled words and print line no, word no, and the word
def spell_checker(dictionary_file, input_file):
    dictionary_words = dictionary(dictionary_file)
    input_lines = input(input_file)

    for line_no, line in enumerate(input_lines, start=1):
        words = line.split('་')  # Split line into words
        for word_no, word in enumerate(words, start=1):
            if word not in dictionary_words:  # Checks if word is in the dictionary
                print(f"Line {line_no}, {word_no} word {word} is incorrect.")

spell_checker('dictionary.txt', '362.txt')



