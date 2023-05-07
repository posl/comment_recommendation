def solve():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if s[i] + s[j] > s[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()