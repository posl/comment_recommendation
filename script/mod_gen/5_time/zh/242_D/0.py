def replace(s):
    s = s.replace("a","bc")
    s = s.replace("b","ca")
    s = s.replace("c","ab")
    return s

if __name__ == '__main__':
    replace()