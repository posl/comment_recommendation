def main():
    s = input()
    v = 0
    w = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            v += 1
        else:
            w += 1
        if v > w:
            count += 1
    print(count)

if __name__ == '__main__':
    main()