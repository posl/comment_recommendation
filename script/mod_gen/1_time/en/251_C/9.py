def main():
    n = int(input())
    t = 0
    s = []
    for i in range(n):
        s.append(input().split())
        s[i][1] = int(s[i][1])
    for i in range(n - 1):
        if s[i][0] == s[i + 1][0] and s[i][1] > s[i + 1][1]:
            t = s[i][1]
            s[i][1] = s[i + 1][1]
            s[i + 1][1] = t
    for i in range(n):
        if s[i][1] == s[n - 1][1]:
            print(i + 1)
            break

if __name__ == '__main__':
    main()