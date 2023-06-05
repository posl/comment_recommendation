def main():
    n, d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    i = 0
    j = 0
    ans = 0
    while i < n:
        if l[i] <= r[j]:
            i += 1
            ans += 1
        else:
            j += 1
            ans -= 1
    print(ans)
