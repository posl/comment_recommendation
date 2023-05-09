def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = []
    i = 0
    while i < N:
        l = L[i]
        while i < N and L[i] <= R[i-1]:
            i += 1
        r = R[i-1]
        ans.append([l, r])
    for a in ans:
        print(a[0], a[1])
