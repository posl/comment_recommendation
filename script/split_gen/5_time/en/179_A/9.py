def plural_form():
    s = input()
    if s.endswith("s"):
        print(s + "es")
    else:
        print(s + "s")
plural_form()
