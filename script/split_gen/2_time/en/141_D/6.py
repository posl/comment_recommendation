def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    B = [0] * (M+1)
    for a in A:
        for i in range(M+1):
            if B[i] >= a:
                break
            if a > B[i] * 2:
                B[i+1] = max(B[i+1], B[i] * 2)
            else:
                B[i+1] = max(B[i+1], a)
    print(sum(B))
