def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        print(a[0])
        return
    b = [0] * N
    for i in range(N):
        b[i] = (a[i], i)
    b.sort()
    c = [0] * N
    for i in range(N):
        c[b[i][1]] = i
    seg = SegmentTree(N, min)
    seg.update(0, N, 0)
    for i in range(N):
        seg.update(c[i], c[i] + 1, i)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += seg.query(i, j + 1)
    print(ans)
