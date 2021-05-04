import re

# to activate uncomment main_code() at the end of the code file

def read_template(path):
    try:
        file = open(path)
        content = file.read()
        file.close()
    except FileNotFoundError:
        content = "no such file"
    if content == "no such file":
        raise FileNotFoundError('incorrect file path or name')
    return content

def remove_parts(word):
    str = ""
    stop = False
    for char in word:
        if char == "{":
            str = str + char
            stop = True
        if char == "}":
            stop = False
        if stop == False:
            str = str + char 
    return str

def split_and_remove_curly(word):
    char_list = []
    counter = 0
    for char in word:
        if counter != 0 and counter != len(word)-1:
            char_list.append(char)
        counter += 1
    return char_list

def parse_template(str):
    game_word_list = []
    new_str = remove_parts(str)
    pattern = r"(({)\w+( ?)(\w+)?( ?)(\w+)?(})|({)\w+( ?)(\d)-( ?)(\w+)?(})|({)\w+( ?)(\w+)?(')?(\w+)( ?)(\w+)?(}))"
    matched_word = (re.finditer(pattern, str))
    for match in matched_word:
        word = match.group()
        char_list = split_and_remove_curly(word)
        speartor = ""
        word = speartor.join(char_list)
        game_word_list.append(word)
    return new_str,game_word_list

def merge(str,tuple):
    str = str.format(*tuple)
    return str

def main_code():
    welcom_msg = """welcom to new Madlib game
    the game is easy
    Madlib will ask you to enter some some input words depending on the question
    after that it will use these input words to create an article and show it to you"""
    print(welcom_msg)
    content = read_template('assets/game_readin_file.txt')
    if content != "no such file":
        new_str,game_word_list = parse_template(content)
        index = 0
        for word in game_word_list:
            print("please insert {} ".format(word))
            replaced_word = input()
            game_word_list[index] = replaced_word
            index += 1
        article = merge(new_str,tuple(game_word_list))
        writter = open('assets/game_output.txt',"w")
        writter.write(article)
        writter.close()
        print(read_template('assets/game_output.txt'))

# main_code()


