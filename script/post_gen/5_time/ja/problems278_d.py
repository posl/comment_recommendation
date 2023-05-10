Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    query.reverse()
    for i in range(q):
        #print(query[i])
        if query[i][0] == 1:
            a = [query[i][1]] * n
        elif query[i][0] == 2:
            a[query[i][1] - 1] += query[i][2]
        else:
            print(a[query[i][1] - 1])

=======
Suggestion 2

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
            A[query[i][1]-1] = A[query[i][1]-1] + query[i][2]
        else:
            print(A[query[i][1]-1])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for q in range(Q):
        query.append(input().split())
    
    for q in query:
        if q[0] == '1':
            for i in range(N):
                A[i] = int(q[1])
        elif q[0] == '2':
            A[int(q[1]) - 1] += int(q[2])
        else:
            print(A[int(q[1]) - 1])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    a_sum = sum(a)
    for i in range(q):
        if query[i][0] == 1:
            print(a_sum + n * query[i][1])
        elif query[i][0] == 2:
            a_sum += query[i][2]
        elif query[i][0] == 3:
            print(a[query[i][1] - 1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for i in range(Q)]
    for q in query:
        if q[0] == 1:
            for i in range(N):
                A[i] = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        else:
            print(A[q[1]-1])

=======
Suggestion 6

def get_input_data():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for q in range(Q):
        query.append(list(map(int, input().split())))
    return (N, A, Q, query)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for i in range(Q)]
    #print(N, A, Q, query)
    #print(query[0][0])
    #print(query[0][1])
    #print(query[0][2])
    #print(query[1][0])
    #print(query[1][1])
    #print(query[1][2])
    #print(query[2][0])
    #print(query[2][1])
    #print(query[2][2])
    #print(query[3][0])
    #print(query[3][1])
    #print(query[3][2])
    #print(query[4][0])
    #print(query[4][1])
    #print(query[4][2])
    #print(query[5][0])
    #print(query[5][1])
    #print(query[5][2])
    #print(query[6][0])
    #print(query[6][1])
    #print(query[6][2])
    #print(query[7][0])
    #print(query[7][1])
    #print(query[7][2])
    #print(query[8][0])
    #print(query[8][1])
    #print(query[8][2])
    #print(query[9][0])
    #print(query[9][1])
    #print(query[9][2])
    #print(query[10][0])
    #print(query[10][1])
    #print(query[10][2])
    #print(query[11][0])
    #print(query[11][1])
    #print(query[11][2])
    #print(query[12][0])
    #print(query[12][1])
    #print(query[12][2])
    #print(query[13][0])
    #print(query[13][1])
    #print(query[13][2])
    #print(query[14][0])
    #print(query[14][1])
    #print(query[14][2])
    #print(query[15][0])
    #print(query[15][1])
    #print(query[15][2])
    #print(query[16][0])
    #print(query[16][1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    sum = 0
    for i in range(Q):
        if query[i][0] == 1:
            sum += query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            ans.append(A[query[i][1]-1] + sum)
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    #print(n, a, q, query)
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            for j in range(n):
                a[j] = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        else:
            ans.append(a[query[i][1]-1])
    for i in ans:
        print(i)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    #print(query)
    for q in query:
        if q[0] == 1:
            for i in range(N):
                A[i] = q[1]
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        elif q[0] == 3:
            print(A[q[1]-1])
        #print(A)
main()
