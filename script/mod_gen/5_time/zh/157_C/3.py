def solve():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    ans = -1
    for i in range(10 ** n):
        i = str(i)
        if len(i) != n:
            continue
        for j in range(m):
            if i[s[j] - 1] != str(c[j]):
                break
        else:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    solve()