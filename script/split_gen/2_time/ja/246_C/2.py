def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] < X:
                ans += A[i]
            else:
                if K > 1:
                    ans += X
                    K -= 2
                else:
                    ans += A[i]
                    K -= 1
        else:
            ans += A[i]
    print(ans)
main()
