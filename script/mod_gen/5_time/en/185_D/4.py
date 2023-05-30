def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] > 1:
            B.append(A[i+1] - A[i] - 1)
    if len(B) == 0:
        print(0)
    else:
        min_B = min(B)
        ans = 0
        for b in B:
            ans += (b + min_B - 1) // min_B
        print(ans)
main()
