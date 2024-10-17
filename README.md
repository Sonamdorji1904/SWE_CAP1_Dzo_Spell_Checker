# Dzongkha Spell Checker

## Project Overview
This project was to create a spell checker for Dzongkha, which is not officially done in Bhutan. The spell checker reads an input text file containing Dzongkha words and checks each word against a dictionary of valid Dzongkha words sourced from a Word document. The main purpose of the this project is so that we can spell check dzongkha words. The main features I used in this project are like input downloading, prepare for the txt file and cleaning the dictionary file.

# Table of Contents

## Usage
This project can be used to spell check any dzongkha paragraphs that we want to spell check like it is programmed such that there is a input file file where you can have your own input data to be spell checked and it is checked from comparing with the valid words provided in the dictionary.

```bash 
python SWE_CAPI_02240362.py 362.txt
```

## Implementation
The Dzongkha spell checker project is structured into several core components, each responsible for a specific aspect of the spell-checking process. This system takes two primary inputs: a text file containing the words to be checked, and a dictionary file which includes the correctly spelled Dzongkha words.
1. Downloading of input file from a given link
2. Dictionary and input file reading
3. Spell checking logics

## Data Structures
I used file operations to open the files to read and write on the files and 'with open' file operations are chosed to use so that I can open the files to read line by line and write binaries. Some other data structures used are like;
1. 'set' to store dictionary  words and for fast lookup, 
2. 'list' to store lines from the input text file for ordered collection and
3. 'string' for text processing, including the contents of the dictionary and input files.

## Algorithms
1. Text Cleaning: Algorithm
uses regular expressions to filter out non-Dzongkha characters from the dictionary text.
2. Dictionary Loading Algorithm: reads the cleaned dictionary file and stores the words in a set.
3. Input Loading Algorithm: reads the input file line by line.
4. Spell Checking Algorithm: iterates through each word in the input file and checks its existence in the dictionary.

## Performance Analysis
1. Time Complexity:
    * Dictionary Loading: O(D), where D is the number of words in the dictionary.
    * Spell Checking (for N words): O(N), where N is the number of words in the input text.

    * Total Time Complexity:
O(D + N + M * D * L)

2. Space Complexity:
    * Dictionary Storage: O(D * L), where L is the average word length.
    * Input Text Storage: O(N * W), where W is the average length of words in the input text.

    * Total Space Complexity:
O(D * L + N * W)

## Challenges and Solutions
1. Character Encoding Issues:

    * Challenge: Misinterpretation of Dzongkha characters due to inconsistent encodings.
    * Solution: Use UTF-8 encoding consistently.

2. Dictionary Completeness:

    * Challenge: Missing words can lead to false positives.
    * Solution: Continuously update and expand the dictionary.

3. Handling Compound Words and Affixes:

    * Challenge: Missed valid words due to compounds and affixes not in the dictionary.
    * Solution: Recognize common compounds and affixes.
4. User Interface and Usability:

    * Challenge: Difficulty for non-technical users to utilize the tool.
    * Solution: Develop a user-friendly GUI.
5. Performance with Large Files:

    * Challenge: Slow processing times with large input and dictionary files.
    * Solution: Optimize algorithms for better performance.
6. Regular Expression Limitations:

    * Challenge: Edge cases may not be handled correctly.
    * Solution: Thoroughly test and adjust regex patterns.
7. Maintenance and Updates:

    * Challenge: Keeping the dictionary current can be resource-intensive.
    * Solution: Establish a regular update process.
8. Error Handling:

    * Challenge: Robust error handling for file operations is needed.
    * Solution: Implement thorough exception handling.

## References
1. Dzongkha Language Resources
    * Dzongkha Unicode. (n.d.). Unicode Consortium. Retrieved from https://www.unicode.org/charts/PDF/U0F00.pdf 
2. Programming Libraries and Tools
    * python-docx. (n.d.). python-docx Documentation. Retrieved from https://python-docx.readthedocs.io/en/latest/
    * Requests: HTTP for Humans. (n.d.). Requests Documentation. Retrieved from https://docs.python-requests.org/en/latest/
    * Regular Expressions. (n.d.). Python re module documentation. Retrieved from https://docs.python.org/3/library/re.html
    * AI like chatGPT, BlackBox



