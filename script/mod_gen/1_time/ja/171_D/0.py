def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    sumA = sum(A)
    for i in range(Q):
        sumA += BC[i][1] * (A.count(BC[i][0]) - A.count(BC[i][1]))
        print(sumA)
        A = list(map(lambda x: BC[i][1] if x == BC[i][0] else x, A))

if __name__ == '__main__':
    main()