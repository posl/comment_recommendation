def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = [list(map(int,input().split())) for i in range(Q)]
    for i in range(Q):
        if query[i][0] == 1:
            A[query[i][1]-1] = query[i][2]
        elif query[i][0] == 2:
            print(A[query[i][1]-1])
