def count(s):
    if len(s) == 1:
        if s[0] == "?":
            return 10
        else:
            return 1
    elif len(s) == 0:
        return 1
    else:
        if s[0] == "?":
            return count(s[1:]) * 10
        else:
            return count(s[1:])

if __name__ == '__main__':
    count()