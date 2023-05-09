def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    S = sum(A)
    for q in queries:
        if q[0] == 1:
            S += q[1] * N
        elif q[0] == 2:
            S += q[2]
        else:
            print(A[q[1]-1] + q[1] * N)

if __name__ == '__main__':
    main()