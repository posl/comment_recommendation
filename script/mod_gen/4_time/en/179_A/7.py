def plural_form(word):
    if word.endswith("s"):
        word += "es"
    else:
        word += "s"
    return word

if __name__ == '__main__':
    plural_form()