def check(s):
    if s[0] == "!":
        if s[1:] in d:
            return True
        else:
            d.add(s)
            return False
    else:
        if "!" + s in d:
            return True

if __name__ == '__main__':
    check()