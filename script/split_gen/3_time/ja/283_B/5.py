def main():
    # input
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = []
    for _ in range(Q):
        query.append(list(map(int,input().split())))
    # output
    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1]-1] = query[i][2]
        else:
            print(A[query[i][1]-1])
    return
