def pluralize(s):
    if s[-1] == "s":
        print(s + "es")
    else:
        print(s + "s")

if __name__ == '__main__':
    pluralize()