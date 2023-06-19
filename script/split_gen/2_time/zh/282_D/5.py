def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if a not in d:
            d[a] = []
        d[a].append(b)
    ans = 0
    for i in range(1, n+1):
        if i not in d:
            continue
        for j in range(i+1, n+1):
            if j not in d:
                ans += 1
            elif j not in d[i]:
                ans += 1
    print(ans)
