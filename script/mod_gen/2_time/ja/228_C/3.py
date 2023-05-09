def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        x = 0
        for j in range(N):
            if sum(A[i]) < sum(A[j]):
                x += 1
        if x < K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()