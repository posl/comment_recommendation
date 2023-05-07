def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    B = [a%200 for a in A]
    #print(B)
    C = {}
    for i in range(N):
        if B[i] in C:
            C[B[i]] += 1
        else:
            C[B[i]] = 1
    #print(C)
    ans = 0
    for c in C.values():
        ans += c*(c-1)//2
    print(ans)
