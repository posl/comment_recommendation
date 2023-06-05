def replace(s):
    s = s.replace("1","a")
    s = s.replace("9","1")
    s = s.replace("a","9")
    return s

if __name__ == '__main__':
    replace()