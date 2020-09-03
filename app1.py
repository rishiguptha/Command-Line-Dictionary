import json
from os import system
from difflib import get_close_matches

data = json.load(open("data.json"))


def defination(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.tittle()]
    elif len(get_close_matches(w, data.keys())) > 0:
        print("Did you mean % s instead?" % get_close_matches(w, data.keys())[0])
        a = input("If Yes(y) or No(n) : ")
        if a in ["y", "Y"]:
            return data[get_close_matches(w, data.keys())[0]]
        elif a in ["n", "N"]:
            print("Please check Your entered word properly")
        else:
            return "We don't understand your query"
    else:
        print("The Entered Word doesn't exists, Please double check the word")


while True:
    system("cls")
    print("                DICITIONARY                 ")
    word = input("Enter the Word : ")
    output = defination(word)
    if type(output) == list:
        for items in output:
            print(items)
    else:
        print(output)
    q = input("Do you Want to Search another press y for Yes  or Any Key to exit: ")
    if q in ["Y", "y"]:
        continue
    else:
        quit()
