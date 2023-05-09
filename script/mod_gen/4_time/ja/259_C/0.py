def main():
    s = input()
    t = input()
    while len(s) < len(t):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1]
            t = t[::-1]
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()