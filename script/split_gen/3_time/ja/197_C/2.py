def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**31-1
    for i in range(N):
        x = 0
        for j in range(i,N):
            x |= A[j]
            if j == N-1:
                ans = min(ans, x)
            else:
                ans = min(ans, x^A[j+1])
    print(ans)
main()
