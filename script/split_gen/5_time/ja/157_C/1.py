def solve():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
        s[i] -= 1
    for i in range(10 ** n):
        str_i = str(i)
        if len(str_i) != n:
            continue
        for j in range(m):
            if str_i[s[j]] != str(c[j]):
                break
        else:
            print(i)
            return
    print(-1)
