def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #solve
    X = []
    for q in query:
        if q[0] == 1:
            a = q[1]
            A = [a] * N
        elif q[0] == 2:
            i, a = q[1], q[2]
            A[i-1] += a
        else:
            i = q[1]
            X.append(A[i-1])
    #output
    for x in X:
        print(x)

if __name__ == '__main__':
    main()