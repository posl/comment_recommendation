def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if B[i] >= A[i]:
            ans += A[i]
            B[i] -= A[i]
            if B[i] >= A[i+1]:
                ans += A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
        else:
            ans += B[i]
    print(ans)
