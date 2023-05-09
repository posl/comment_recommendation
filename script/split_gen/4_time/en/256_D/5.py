def solve():
    N = int(input())
    L = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append((l, r))
    L.sort()
    ans = []
    l, r = L[0]
    for i in range(1, N):
        if r >= L[i][0]:
            r = max(r, L[i][1])
        else:
            ans.append((l, r))
            l, r = L[i]
    ans.append((l, r))
    for l, r in ans:
        print(l, r)
