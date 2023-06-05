def main():
    s = input()
    t = input()
    if len(s) == len(t) - 1 and t[:-1] == s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()