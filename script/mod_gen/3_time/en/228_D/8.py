def main():
    # read input
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    # solve
    N = 2 ** 20
    A = [-1] * N
    h = 0
    for t, x in queries:
        if t == 1:
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
            h += 1
        else:
            print(A[x % N])

if __name__ == '__main__':
    main()