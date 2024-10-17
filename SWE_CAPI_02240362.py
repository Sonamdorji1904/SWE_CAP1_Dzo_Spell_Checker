###############################
# 

# Sonam Dorji
# 1st SWE A
# 02240362
###############################

# REFERENCES
## https://sqlpad.io/tutorial/python-download-file-from-url/#:~:text=Here's%20how%20you'd%20tell,request%20was%20successful%20if%20response.

## The problem valid problem I faced during this assignment is that I couldn't read dzongkha words with different syllabus as a word rather it is being read by the whitespaces, so I tried referring to same situation like katakana words and tibetan spell checkers

###############################
# SOLUTION
###############################


import requests

url = "https://csf101-server-cap1.onrender.com/get/input/362"
r = requests.get(url)

with open('362.txt', 'wb') as file:
    data = file.write(r.content)

print("Downloaded: 362.txt")


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
cleaned_content = clean(doc_text)

# It will write the modified content into a new file
with open('dictionary.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

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

    for line_num, line in enumerate(input_lines, start=1):
        words = line.split()  # Split line into words
        for word_num, word in enumerate(words, start=1):
            if word not in dictionary_words:  # Checks if word is in the dictionary
                print(f"Line {line_num}, {word_num} word {word} is incorrect.")

spell_checker('dictionary.txt', '362.txt')



