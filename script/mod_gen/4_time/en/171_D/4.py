def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    A_sum = sum(A)
    B_sum = [0] * (10**5 + 1)
    for i in range(N):
        B_sum[A[i]] += 1
    for i in range(Q):
        A_sum += (BC[i][1] - BC[i][0]) * B_sum[BC[i][0]]
        B_sum[BC[i][1]] += B_sum[BC[i][0]]
        B_sum[BC[i][0]] = 0
        print(A_sum)

if __name__ == '__main__':
    main()