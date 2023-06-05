def problems273_c():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if A[i] != A[i+1]:
            for j in range(cnt, i+1):
                ans[j] = i - cnt + 1
            cnt = i + 1
    print('\n'.join(map(str, ans)))
    return 0
