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
    ans = 0
    for i in range(N):
        ans += (L[i] - R[i]) * (N - i)
    ans = ans // D
    if ans * D < ans:
        ans += 1
    print(ans)
