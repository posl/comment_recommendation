def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
        else:
            ans += A[i]
            B[i] -= A[i]
            if A[i+1] >= B[i]:
                ans += B[i]
                A[i+1] -= B[i]
            else:
                ans += A[i+1]
                A[i+1] = 0
    print(ans)
