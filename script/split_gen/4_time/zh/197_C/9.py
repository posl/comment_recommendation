def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**30
    for i in range(N):
        a = A[i]
        for j in range(i, N):
            a = a | A[j]
            ans = min(ans, a)
    print(ans)
main()
