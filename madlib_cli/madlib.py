import re


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
            stop = True
        if stop == False:
            str = str + char 
        if char == "}":
            stop = False
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
    return [new_str,game_word_list]

def replace_part_with_num(word):
    new_str = ""
    stop = False
    counter = 0
    for char in word:
        if char == "{":
            new_str = new_str + char + str(counter)
            counter += 1
            stop = True
        if char == "}":
            stop = False
        if stop == False:
            new_str = new_str + char 
    return new_str

def main():
    welcom_msg = """welcom to new Madlib game
    the game is easy
    Madlib will ask you to enter some some input words depending on the question
    after that it will use these input words to create an article and show it to you"""
    print(welcom_msg)
    content = read_template('assets/game_readin_file.txt')
    if content != "no such file":
        parse_content = parse_template(content)
        new_str = parse_content[0]
        game_word_list = parse_content[1]
        index = 0
        # for word in game_word_list:
        #     print("please insert {} ".format(word))
        #     replaced_word = input()
        #     game_word_list[index] = replaced_word
        #     index += 1
        content = replace_part_with_num(content)
        # print(content)
        print(game_word_list)
        content = content.format(*game_word_list)
        # print(content)

main()


