def plural(s):
    if s[-1] == "s":
        return s + "es"
    else:
        return s + "s"

if __name__ == '__main__':
    plural()