def main():
    n = int(input())
    s = input()
    for i in range(1, n+1):
        if i % 2 != 0:
            if s[i-1] != '"':
                s = s[:i-1] + '.' + s[i:]
        else:
            if s[i-1] != '"':
                s = s[:i-1] + '.' + s[i:]
    print(s)

if __name__ == '__main__':
    main()