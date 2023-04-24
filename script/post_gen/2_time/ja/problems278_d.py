Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    query = []
    for i in range(Q):
        query.append([int(i) for i in input().split()])
    for i in range(Q):
        if query[i][0] == 1:
            A = [query[i][1]] * N
        elif query[i][0] == 2:
            A[query[i][1] - 1] += query[i][2]
        else:
            print(A[query[i][1] - 1])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    X = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            for j in range(N):
                A[j] = query[1]
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        elif query[0] == 3:
            X.append(A[query[1]-1])
    for i in range(len(X)):
        print(X[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    add = 0
    for i in range(Q):
        if query[i][0] == 1:
            add = query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            print(A[query[i][1]-1] + add)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for i in range(q)]
    x = 0
    for i in range(q):
        if query[i][0] == 1:
            x += query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        else:
            print(a[query[i][1]-1]+x)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for q in query:
        if q[0] == 1:
            A = [q[1]]*N
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            ans.append(A[q[1]-1])
    for i in ans:
        print(i)

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    #print(N,A,Q,query)
    
    add = 0
    for q in query:
        if q[0] == 1:
            add = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2] - add
        else:
            print(A[q[1]-1] + add)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    query = [list(map(int,input().split())) for _ in range(Q)]
    x = 0
    for i in range(Q):
        if query[i][0] == 1:
            x += query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            print(A[query[i][1]-1] + x)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    query = [list(map(int,input().split())) for i in range(q)]
    x = 0
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            x = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
            a[query[i][1]-1] -= x
        else:
            ans.append(a[query[i][1]-1] + x)
    for i in ans:
        print(i)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    
    # 1番目のクエリが1の場合のみ、aの値をxに更新していく
    # 1番目のクエリが2の場合のみ、aの値をxに更新していく
    # 1番目のクエリが3の場合のみ、aの値をxに更新していく
    
    # 1番目のクエリが1の場合のみ、aの値をxに更新していく
    # 1番目のクエリが2の場合のみ、aの値をxに更新していく
    # 1番目のクエリが3の場合のみ、aの値をxに更新していく
    
    # 1番目のクエリが1の場合のみ、aの値をxに更新していく
    # 1番目のクエリが2の場合のみ、aの値をxに更新していく
    # 1番目のクエリが3の場合のみ、aの値をxに更新していく
    
    # 1番目のクエリが1の場合のみ、aの値をxに更新していく
    # 1番目のクエリが2の場合のみ、aの値をxに更新していく
    # 1番目のクエリが3の場合のみ、aの値をxに更新していく
    
    # 1番目のクエリが1の場合のみ、aの値をxに更新していく
    # 1番目のクエリが2の場合のみ、aの値をxに更新していく
    # 1番目のクエリが3の場合のみ、aの値をxに更新していく
    
    # 1番目
