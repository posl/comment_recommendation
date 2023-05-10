def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    cnt = {}
    for a in A:
        cnt[a] = cnt.get(a, 0) + 1
    for i in range(1, 200001):
        if i not in cnt:
            continue
        if cnt[i] == 1:
            ans[A.index(i)] = 1
        else:
            ans[A.index(i)] = 0
        for j in range(2 * i, 200001, i):
            if j not in cnt:
                continue
            if cnt[j] == 1:
                ans[A.index(i)] += 1
            cnt[j] = 0
    for i in ans:
        print(i)
