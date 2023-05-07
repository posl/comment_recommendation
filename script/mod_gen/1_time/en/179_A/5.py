def plural_form(s):
    if s.endswith("s"):
        return s + "es"
    else:
        return s + "s"

if __name__ == '__main__':
    plural_form()