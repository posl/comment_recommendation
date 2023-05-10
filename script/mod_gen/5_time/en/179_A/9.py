def plural_form():
    s = input()
    if s.endswith("s"):
        print(s + "es")
    else:
        print(s + "s")
plural_form()

if __name__ == '__main__':
    plural_form()