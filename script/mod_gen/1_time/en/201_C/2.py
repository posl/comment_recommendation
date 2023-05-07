def main():
    s = input()
    if s[0] == 'o':
        n = 1
    elif s[0] == 'x':
        n = 0
    else:
        n = 10
    for i in range(1, 10):
        if s[i] == 'o':
            n *= 1
        elif s[i] == 'x':
            n *= 0
        else:
            n *= 9
    print(n)

if __name__ == '__main__':
    main()