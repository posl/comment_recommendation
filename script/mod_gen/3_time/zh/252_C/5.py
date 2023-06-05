def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(10):
        #print(i)
        #print(s)
        #print(s[0][i])
        #print(s[1][i])
        #print(s[2][i])
        #print(s[3][i])
        #print(s[4][i])
        #print()
        if s[0][i] != s[1][i] or s[0][i] != s[2][i] or s[0][i] != s[3][i] or s[0][i] != s[4][i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()