def plural(s):
    if s[-1] == "s":
        s += "es"
    else:
        s += "s"
    return s

if __name__ == '__main__':
    plural()