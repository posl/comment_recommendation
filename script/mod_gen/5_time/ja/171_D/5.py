def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        print(sum - A[B-1] * (A[B-1] - C) + C * (A[B-1] - C))
        A[B-1] = C
        sum = sum - A[B-1] * (A[B-1] - C) + C * (A[B-1] - C)

if __name__ == '__main__':
    main()