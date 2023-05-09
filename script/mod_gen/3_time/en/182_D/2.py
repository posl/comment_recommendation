def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    ans = 0
    for i in range(N+1):
        ans = max(ans, A[i])
    print(ans)

if __name__ == '__main__':
    main()