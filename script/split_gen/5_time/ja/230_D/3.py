def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        Li, Ri = map(int, input().split())
        L.append(Li)
        R.append(Ri)
    L.sort()
    R.sort()
    ans = 0
    i = 0
    j = 0
    while i < N:
        if L[i] <= R[j]:
            i += 1
        else:
            j += 1
        if j - i > ans:
            ans = j - i
    print(ans)
