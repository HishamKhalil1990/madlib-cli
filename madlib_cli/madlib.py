import re

def remove_parts(word):
    str = ""
    stop = False
    for char in word:
        if char == "{":
            stop = True
        if stop == False:
            str = str + char 
        if char == "}":
            stop = False
    return str

def read_template(path):
    try:
        file = open(path)
        content = file.read()
        file.close()
    except FileNotFoundError:
        content = "no such file"
    if content == "no such file":
        raise FileNotFoundError('incorect file path or name')
    return content

def parse_template(str):
    game_word_list = []
    new_str = remove_parts(str)
    pattern = r"(({)\w+( ?)(\w+)?( ?)(\w+)?(}))"
    matched_word = (re.finditer(pattern, str))
    for match in matched_word:
        word = match.group()
        char_list = split_and_remove_curly(word)
        speartor = ""
        word = speartor.join(char_list)
        game_word_list.append(word)
    return [new_str,game_word_list]

def split_and_remove_curly(word):
    char_list = []
    counter = 0
    for char in word:
        if counter != 0 and counter != len(word)-1:
            char_list.append(char)
        counter += 1
    return char_list

content = read_template('assets/game_readin_file.txt')
if content != "no such file":
    parse_content = parse_template(content)
    new_str = parse_content[0]
    game_word_list = parse_content[1]
    print(new_str)
    print(game_word_list)


