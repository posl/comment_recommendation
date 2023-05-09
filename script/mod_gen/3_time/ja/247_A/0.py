def main():
    s = input()
    s = list(s)
    for i in range(len(s)):
        if s[i] == "1":
            s[i] = "0"
        else:
            s[i] = "1"
    print("".join(s))

if __name__ == '__main__':
    main()