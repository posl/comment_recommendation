def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(N):
        sum -= A[i]
        ans += A[i] * sum
    print(ans % (10**9 + 7))

if __name__ == '__main__':
    main()