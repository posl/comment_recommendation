Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 1 x
    # 2 i x
    # 3 i
    add = 0
    ans = []
    for q in query:
        if q[0] == 1:
            add = q[1]
        elif q[0] == 2:
            A[q[1] - 1] += q[2]
        else:
            ans.append(A[q[1] - 1] + add)
    print(*ans, sep='

')
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    query = []
    for q in range(Q):
        query.append([int(x) for x in input().split()])
    add = [0] * N
    add_all = 0
    for q in range(Q):
        if query[q][0] == 1:
            add_all += query[q][1]
        elif query[q][0] == 2:
            add[query[q][1]-1] += query[q][2]
        else:
            print(A[query[q][1]-1] + add[query[q][1]-1] + add_all)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    ans = []
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a = [query[1]]*n
        elif query[0] == 2:
            a[query[1]-1] += query[2]
        else:
            ans.append(a[query[1]-1])
    print('

'.join(map(str, ans)))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    B = [0] * N
    C = 0
    for q in queries:
        if q[0] == 1:
            C = q[1]
        elif q[0] == 2:
            B[q[1]-1] += q[2]
        else:
            print(A[q[1]-1] + C + B[q[1]-1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    add = [0] * N
    for q in queries:
        if q[0] == 1:
            add = [q[1]] * N
        elif q[0] == 2:
            add[q[1] - 1] += q[2]
        else:
            print(A[q[1] - 1] + add[q[1] - 1])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    add = 0
    for i in range(q):
        if query[i][0] == 1:
            add = query[i][1]
        elif query[i][0] == 2:
            a[query[i][1]-1] = query[i][2] - add
        else:
            ans.append(a[query[i][1]-1]+add)
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [input().split() for _ in range(q)]
    ans = []
    for query in queries:
        if query[0] == '1':
            a = [int(query[1])] * n
        elif query[0] == '2':
            a[int(query[1]) - 1] += int(query[2])
        else:
            ans.append(a[int(query[1]) - 1])
    print('

'.join(map(str, ans)))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [input().split() for _ in range(q)]
    ans = []
    add = 0
    for query in queries:
        if query[0] == '1':
            add = int(query[1])
        elif query[0] == '2':
            a[int(query[1])-1] += int(query[2])
        else:
            ans.append(a[int(query[1])-1] + add)
    print(*ans, sep='

')

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    Q1 = [0] * N
    Q2 = [0] * N
    A2 = [0] * N
    for i in range(N):
        A2[i] = A[i]
    for q in query:
        if q[0] == 1:
            Q1 = [q[1]] * N
            Q2 = [0] * N
        elif q[0] == 2:
            Q2[q[1]-1] += q[2]
        else:
            print(A2[q[1]-1] + Q1[q[1]-1] + Q2[q[1]-1])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # 1 x: assign x to every element of A
    # 2 i x: add x to A_{i}
    # 3 i: print the value of A_{i}
    # 0 <= A_i <= 10^9
    # 1 <= i <= N
    # 0 <= x <= 10^9

    # 1 x: assign x to every element of A
    # 2 i x: add x to A_{i}
    # 3 i: print the value of A_{i}

    # 0 <= A_i <= 10^9
    # 1 <= i <= N
    # 0 <= x <= 10^9

    # 1 x: assign x to every element of A
    # 2 i x: add x to A_{i}
    # 3 i: print the value of A_{i}

    # 0 <= A_i <= 10^9
    # 1 <= i <= N
    # 0 <= x <= 10^9

    # 1 x: assign x to every element of A
    # 2 i x: add x to A_{i}
    # 3 i: print the value of A_{i}

    # 0 <= A_i <= 10^9
    # 1 <= i <= N
    # 0 <= x <= 10^9

    # 1 x: assign x to every element of A
    # 2 i x: add x to A_{i}
    # 3 i: print the value of A_{i}

    # 0 <= A_i <= 10^9
    # 1 <= i <= N
    # 0 <= x <= 10^9

    # 1 x: assign x to every element of A
    # 2 i x: add x to A_{i}
    # 3 i: print the value of A_{i}

    # 0 <= A_i <= 10^9
    # 1 <= i <= N
    # 0 <= x <= 10^9
