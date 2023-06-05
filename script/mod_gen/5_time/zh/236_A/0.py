def main():
    str = input()
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    str = list(str)
    str[a], str[b] = str[b], str[a]
    for i in str:
        print(i, end='')

if __name__ == '__main__':
    main()