def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    K = bin(K)[2:]
    K = K.zfill(41)
    A = [bin(a)[2:].zfill(41) for a in A]
    S = [0]*41
    for a in A:
        for i in range(41):
            S[i] += int(a[i])
    ans = 0
    for i in range(41):
        if S[i] < N//2:
            ans += 2**i
    print(ans)
