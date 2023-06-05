def main():
    s = input()
    length = len(s)
    min_s = s
    max_s = s
    for i in range(1,length):
        s = s[1:] + s[0]
        if s < min_s:
            min_s = s
        elif s > max_s:
            max_s = s
    print(min_s)
    print(max_s)

if __name__ == '__main__':
    main()