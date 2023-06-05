def main():
    n = int(input())
    s = input()
    for i in range(n):
        if i % 2 == 0 and s[i] == '"':
            print('"', end='')
        else:
            print(s[i], end='')

if __name__ == '__main__':
    main()