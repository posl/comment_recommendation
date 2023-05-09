def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int,input().split())))
    X = []
    for q in query:
        if q[0] == 3:
            X.append(A[q[1]-1])
        elif q[0] == 1:
            A = [q[1]]*N
        else:
            A[q[1]-1] += q[2]
    for x in X:
        print(x)

if __name__ == '__main__':
    main()