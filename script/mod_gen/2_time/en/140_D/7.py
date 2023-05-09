def main():
    n, k = map(int, input().split())
    s = input()
    if k == 1:
        print(max(s.count('R'), s.count('L')))
    else:
        s += 'R'
        c = 0
        for i in range(n):
            if s[i] == s[i + 1]:
                c += 1
        print(n - c)

if __name__ == '__main__':
    main()