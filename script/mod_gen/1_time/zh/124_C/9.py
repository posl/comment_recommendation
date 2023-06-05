def main():
    s = input()
    white = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "1":
                white += 1
        else:
            if s[i] == "0":
                white += 1
    print(min(white, len(s) - white))

if __name__ == '__main__':
    main()