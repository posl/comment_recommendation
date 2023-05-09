def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        A = list(map(int, input().split()))
        sum = 0
        for j in range(M):
            sum += A[j] * B[j]
        sum += C
        if sum > 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()