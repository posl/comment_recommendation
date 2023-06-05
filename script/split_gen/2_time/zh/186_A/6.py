def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = sorted(map(int, input().split()))
    if a[0] != 1:
        a.insert(0, 0)
    if a[-1] != n:
        a.append(n+1)
    b = [a[i+1] - a[i] - 1 for i in range(len(a)-1)]
    k = min(b)
    ans = 0
    for i in b:
        if i % k == 0:
            ans += i // k
        else:
            ans += i // k + 1
    print(ans)
