def main():
    n,m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    s.sort()
    t.sort()
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
                break
    print(ans)
main()

if __name__ == '__main__':
    main()