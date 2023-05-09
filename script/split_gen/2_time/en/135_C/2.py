def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if B[i] >= A[i]:
            ans += A[i]
            B[i] -= A[i]
            A[i] = 0
            if B[i] >= A[i+1]:
                ans += A[i+1]
                B[i] -= A[i+1]
                A[i+1] = 0
            else:
                ans += B[i]
                A[i+1] -= B[i]
                B[i] = 0
        else:
            ans += B[i]
            A[i] -= B[i]
            B[i] = 0
    print(ans)
main()
I have a problem with my code. I want to know why my code is not working correctly. I have tried to debug it but I have not been able to find the problem.
My code is this:
