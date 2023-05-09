def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum > N:
        print(-1)
    else:
        print(N - sum)

if __name__ == '__main__':
    main()