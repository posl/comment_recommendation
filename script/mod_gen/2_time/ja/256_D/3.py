def solve():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = []
    while i < N and j < N:
        if L[i] < R[j]:
            ans.append([L[i], R[j]])
            i += 1
            j += 1
        else:
            j += 1
    for a in ans:
        print(a[0], a[1])
solve()

if __name__ == '__main__':
    solve()