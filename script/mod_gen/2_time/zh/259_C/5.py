def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()