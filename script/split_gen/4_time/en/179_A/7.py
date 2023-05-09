def plural_form(word):
    if word.endswith("s"):
        word += "es"
    else:
        word += "s"
    return word
