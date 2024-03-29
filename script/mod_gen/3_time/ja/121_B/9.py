def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[int(i) for i in input().split()] for j in range(N)]
    cnt = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()