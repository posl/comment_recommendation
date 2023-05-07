def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            if i+j < N:
                sum += (j+1) * A[i+j]
        ans = max(ans, sum)
    print(ans)

if __name__ == '__main__':
    main()