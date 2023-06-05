def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    sum = 0
    for i in range(N):
        sum += A[i]
    ans = 0
    for i in range(N):
        ans = max(ans, sum)
        sum -= A[i]
        sum += A[i+N]
    print(ans)

if __name__ == '__main__':
    main()