def check():
    s = input()
    t = input()
    if len(s) == len(t) -1 and s == t[:-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    check()