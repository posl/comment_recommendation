def solve():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    for i in range(10 ** N):
        s = str(i)
        if len(s) != N:
            continue
        for j, c in sc:
            if int(s[j - 1]) != c:
                break
        else:
            return s
    return -1
print(solve())
