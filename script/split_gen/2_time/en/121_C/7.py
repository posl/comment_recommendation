def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)
    a, b = (list(t) for t in zip(*sorted(zip(a, b))))
    tmp = 0
    ans = 0
    for i in range(N):
        if tmp + b[i] <= M:
            ans += a[i] * b[i]
            tmp += b[i]
        else:
            ans += a[i] * (M - tmp)
            tmp = M
        if tmp == M:
            break
    print(ans)
