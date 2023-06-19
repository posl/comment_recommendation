def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(N):
                A[j] = query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            print(A[query[i][1]-1])
