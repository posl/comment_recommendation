def main():
    s = input()
    if len(s) == 1:
        print(s)
        print(s)
        return
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

if __name__ == '__main__':
    main()