def countWords(text):
    word_count = text.split()
    return len(word_count)

def sort_on(items):
    return items["num"]

def countChars(text):
    char_dict = {}
    for char in text:
        char_lower = char.lower()
        if not char_lower.isalpha():
            continue
        if char_lower not in char_dict:
            char_dict[char_lower] = 0
        char_dict[char_lower] += 1

    char_count_list = []
    for key in char_dict:
        char_count_list.append({"char": key, "num": char_dict[key]})

    char_count_list.sort(reverse=True, key=sort_on)
    
    return char_count_list

def analyzeBookText(filePath):
    file_contents = ''
    with open(filePath) as f:
        file_contents = f.read()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")

    num_words = countWords(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    count_chars = countChars(file_contents)
    print("--------- Character Count -------")
    for elem in count_chars:
        print(f"{elem["char"]}: {elem["num"]}")

    print("============= END ===============")