def main():
    n = int(input())
    s = input()
    for i in range(0, n):
        if s[i] == ',':
            if (i + 1) % 2 == 0:
                print('.', end='')
            else:
                print(s[i], end='')
        else:
            print(s[i], end='')
    print()

if __name__ == '__main__':
    main()