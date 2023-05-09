def main():
    # read input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = []
    for i in range(Q):
        BC.append(list(map(int, input().split())))
    # calculate
    A_sum = sum(A)
    A_count = [0] * (10**5 + 1)
    for i in range(N):
        A_count[A[i]] += 1
    for i in range(Q):
        A_sum += (BC[i][1] - BC[i][0]) * A_count[BC[i][0]]
        A_count[BC[i][1]] += A_count[BC[i][0]]
        A_count[BC[i][0]] = 0
        print(A_sum)

if __name__ == '__main__':
    main()