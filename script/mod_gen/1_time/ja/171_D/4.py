def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, BC)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    for i in range(Q):
        sum = sum - A[BC[i][0]-1] * BC[i][1] + BC[i][1] * BC[i][0]
        A[BC[i][0]-1] = BC[i][1]
        print(sum)

if __name__ == '__main__':
    main()