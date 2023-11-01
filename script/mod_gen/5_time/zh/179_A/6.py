def plural_form(word):
    if word[-1] == "s":
        return word + "es"
    else:
        return word + "s"

if __name__ == '__main__':
    plural_form()