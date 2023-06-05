def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > ans:
            ans = A[i]
        elif A[i] < ans:
            print(-1)
            return
    print(ans)
main()
