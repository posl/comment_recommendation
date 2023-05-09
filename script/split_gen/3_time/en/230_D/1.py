def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    cnt = 0
    r = 0
    for l in L:
        while r < N and R[r] < l:
            r += 1
        cnt += N - r
    print((cnt + D - 1) // D)
