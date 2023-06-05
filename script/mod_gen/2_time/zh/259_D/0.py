def main():
    s = input()
    t = input()
    while len(s) < len(t):
        if s[-1] == t[len(s)-1]:
            s = s + s[-1]
        else:
            break
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()