def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(A)
    #print(query)
    
    # 1番目のクエリの処理
    for q in range(Q):
        if query[q][0] == 1:
            x = query[q][1]
            for i in range(N):
                A[i] = x
        elif query[q][0] == 2:
            i = query[q][1]
            x = query[q][2]
            A[i-1] += x
        elif query[q][0] == 3:
            i = query[q][1]
            print(A[i-1])
        #print(q, A)
