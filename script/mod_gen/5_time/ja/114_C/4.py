def check(n):
    s = str(n)
    return s.count("7") >= 1 and s.count("5") >= 1 and s.count("3") >= 1 and s.count("7") + s.count("5") + s.count("3") == len(s)

if __name__ == '__main__':
    check()