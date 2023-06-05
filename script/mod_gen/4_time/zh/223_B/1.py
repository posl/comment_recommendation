def main():
    s = input()
    l = len(s)
    min = s
    max = s
    for i in range(1, l):
        s = s[1:] + s[0]
        if s < min:
            min = s
        if s > max:
            max = s
    print(min)
    print(max)

if __name__ == '__main__':
    main()