
# return the no of words in a string
def word_in_string(text):
    words = text.split()
    return len(words)

# count the no of each char in a string
def char_count(text):
    dic = {}
    global alphabet_count

    for word in text:
        word = word.lower()
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    
    return dic

def sort_on(dict):
    return dict["value"]


def sorted_dic(dic):
    alphabet_count = []
    for key in dic:
        if key.isalpha():
            alphabet_count.append({"char": key, "value": dic[key]})

    alphabet_count.sort(key=sort_on, reverse=True)

    return alphabet_count



filepath = "books/frankenstein.txt"

def main():
    filecontent = ""
    # opening the file and reading it
    with open(filepath) as f:
        file_content = f.read()
        # print(file_content)


    print(f"--- Begin report of {filepath} ---")
    print(f"{word_in_string(file_content)} words found in the document")
    l = sorted_dic(char_count(file_content))
    for i in l:
        print(f"The {i['char']} character was found {i['value']} times")
    print("--- End report ---")
main()