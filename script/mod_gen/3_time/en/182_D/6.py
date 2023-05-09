def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(N):
        ans = max(ans, sum+A[i])
        sum += A[i]
    print(ans)

if __name__ == '__main__':
    main()