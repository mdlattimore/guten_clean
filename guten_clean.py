"""A function to remove all extraneous text from Project Gutenberg txt files. Most such files start with informational text at the beginning written by the creator of the file and licensing text at the end. The text of the work itself is sandwiched between the strings '*** START ... *** and '*** END ... ***' This function preserves evertything in between those strings, strips leading and trailing whitespace, collapses any 3 or more consecutive new lines into 2, and saves to a new file with suffix '_processed' """

import re

def clean(text):
    """Strips Project Gutenberg .txt files of all but the text of the work and removes extraneous new lines (collapses any 3 or more consective new lines into 2) """
    pattern_start = r"\*\*\* START .+ \*\*\*"
    pattern_end = r"\*\*\* END .+ \*\*\*"
    pattern_space = r"\n\n\n+"
    start = re.search(pattern_start, text).span()[1]
    end = re.search(pattern_end, text).span()[0]
    intermediate_text = text[start:end].strip()
    final_text = re.sub(pattern_space, "\n\n", intermediate_text)
    return final_text

def main():
    target_text = input("Please input path to file (omit file extension): ")

    with open(f"{target_text}.txt", mode="r") as file:
        raw_text = file.read()

    cleaned = clean(raw_text)
    with open(f"{target_text}_processed.txt", mode='w') as file:
        file.write(cleaned)

if __name__ == '__main__':
    main()