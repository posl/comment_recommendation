def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    ans = []
    for i in range(2**N):
        B = []
        C = []
        for j in range(N):
            if (i >> j) & 1:
                B.append(j+1)
            else:
                C.append(j+1)
        if len(B) != 0 and len(C) != 0 and len(B) != len(C):
            if sum([A[b-1] for b in B]) % mod == sum([A[c-1] for c in C]) % mod:
                ans.append([B, C])
    if len(ans) == 0:
        print("No")
    else:
        print("Yes")
        print(*ans[0])
