def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == '"' and i % 2 == 0:
            s = s[:i] + '.' + s[i + 1:]
    print(s)

if __name__ == '__main__':
    main()