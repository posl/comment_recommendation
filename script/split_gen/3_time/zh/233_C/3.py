def main():
    n, x = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, 1 << n):
        p = 1
        for j in range(n):
            if i >> j & 1:
                p *= l[j][0]
        if p == x:
            ans += 1
    print(ans)
