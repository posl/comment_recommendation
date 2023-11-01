def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = sorted(s)
    for i in range(n-1):
        if s[i][0] != '!' and s[i+1][0] == '!' and s[i] == s[i+1][1:]:
            print(s[i])

if __name__ == '__main__':
    main()