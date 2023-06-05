def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        sum += (BC[i][1] - BC[i][0]) * A.count(BC[i][0])
        print(sum)
        sum = sum - (BC[i][1] - BC[i][0]) * A.count(BC[i][0])
        A = [BC[i][1] if x == BC[i][0] else x for x in A]

if __name__ == '__main__':
    main()