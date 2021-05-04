import re

def split_to_char(word):
    char_list = []
    counter = 0
    for char in word:
        if counter != 0 and counter != len(word)-1:
            char_list.append(char)
        counter += 1
    return char_list

file = open('assets/game_readin_file.txt')
content = file.read()
file.close()
game_word_list = []
pattern = r"(({)\w+( ?)(\w+)?( ?)(\w+)?(}))"
matched_word = (re.finditer(pattern, content))
for match in matched_word:
    word = match.group()
    char_list = split_to_char(word)
    speartor = ""
    word = speartor.join(char_list)
    game_word_list.append(word)
