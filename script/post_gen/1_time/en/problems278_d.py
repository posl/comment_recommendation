Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(str, input().split())))
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            A = [int(query[i][1])]*N
        elif query[i][0] == '2':
            A[int(query[i][1])-1] += int(query[i][2])
        else:
            ans.append(A[int(query[i][1])-1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(str, input().split())))
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            x = int(query[i][1])
            for j in range(N):
                A[j] = x
        elif query[i][0] == '2':
            i = int(query[i][1]) - 1
            x = int(query[i][1])
            A[i] += x
        else:
            i = int(query[i][1]) - 1
            ans.append(str(A[i]))
    print('

'.join(ans))

=======
Suggestion 3

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
        else:
            ans.append(A[q[1]-1])
    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = []
    add = 0
    for q in query:
        if q[0] == '1':
            add = int(q[1])
        elif q[0] == '2':
            A[int(q[1])-1] += int(q[2]) - add
        else:
            ans.append(A[int(q[1])-1] + add)
    print(*ans, sep='

')
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [input().split() for _ in range(q)]
    x = 0
    for query in queries:
        if query[0] == '1':
            x = int(query[1])
        elif query[0] == '2':
            a[int(query[1]) - 1] += int(query[2]) - x
        else:
            print(a[int(query[1]) - 1] + x)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    ans = []
    cnt = 0
    for i in range(Q):
        if query[i][0] == 1:
            cnt += query[i][1]
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            ans.append(A[query[i][1]-1] + cnt)
    for i in ans:
        print(i)

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    X = []
    for query in queries:
        if query[0] == 1:
            A = [query[1]] * N
        elif query[0] == 2:
            A[query[1] - 1] += query[2]
        elif query[0] == 3:
            X.append(A[query[1] - 1])
    for x in X:
        print(x)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    #1 x _ q: assign x_q to every element of A.
    #2 i _ q x _ q: add x_q to A _ {i _ q}.
    #3 i _ q: print the value of A _ {i _ q}.
    # (1, 2, 3)
    # (x, i, x)
    # (x, x, x)
    query = [(int(q[0]), int(q[1]), int(q[2]) if len(q) == 3 else 0) for q in query]
    #print(query)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 1 x
    # 2 i x
    # 3 i
    # 1 x を実行するときにxを保存しておく
    # 2 i x を実行するときにi, xを保存しておく
    # 3 i を実行するときにiを保存しておく
    # 1 x を実行した時に、2 i x を実行した回数を保存しておく
    # 2 i x を実行した時に、2 i x を実行した回数を保存しておく
    # 3 i を実行した時に、2 i x を実行した回数を保存しておく

    # 1 x を実行した時に、2 i x を実行した回数を保存しておく
    # 2 i x を実行した時に、2 i x を実行した回数を保存しておく
    # 3 i を実行した時に、2 i x を実行した回数を保存しておく
    # 1 x を実行した時に、2 i x を実行した回数を保存しておく
    # 2 i x を実行した時に、2 i x を実行した回数を保存しておく
    # 3 i を実行した時に、2 i x を実行した回数を保存しておく

    # 1 x を実行した時に、2 i x を実行した回数を保存しておく
    # 2 i x を実行した時に、2 i x を実行した回数を保存しておく
    # 3 i を実行した時に、2 i x を実行した回数を保存しておく
    # 1 x を実行した時に、2 i x を実行した回数

=======
Suggestion 10

def main():

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    ans = []
    for i in range(q):
        if query[i][0] == 1:
            a = [query[i][1]] * n
        elif query[i][0] == 2:
            a[query[i][1] - 1] += query[i][2]
        else:
            ans.append(a[query[i][1] - 1])

    print(*ans, sep='

')
