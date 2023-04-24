Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x - 1])

=======
Suggestion 3

def main():
    N,Q = map(int,input().split())
    S = input()
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        elif t == 2:
            print(S[x-1])

=======
Suggestion 4

def main():
    N,Q = map(int, input().split())
    S = input()
    S = S[::-1]
    for _ in range(Q):
        t,x = map(int, input().split())
        if t == 1:
            S = S[1:] + S[0]
        else:
            print(S[x-1])

=======
Suggestion 5

def main():
    N,Q = list(map(int,input().split()))
    S = input()
    S = list(S)
    for i in range(Q):
        t,x = list(map(int,input().split()))
        if t == 1:
            S.insert(0,S.pop(x-1))
        else:
            print(S[x-1])

=======
Suggestion 6

def main():
    N,Q = map(int,input().split())
    S = input()
    query = [input().split() for i in range(Q)]
    for i in range(Q):
        if query[i][0] == '1':
            S = S[-int(query[i][1]):] + S[:N-int(query[i][1])]
        elif query[i][0] == '2':
            print(S[int(query[i][1])-1])

=======
Suggestion 7

def main():
    N,Q = [int(i) for i in input().split()]
    S = input()
    S = list(S)
    S.reverse()
    for i in range(Q):
        t,x = [int(i) for i in input().split()]
        if t == 1:
            for j in range(x):
                S.append(S.pop())
        else:
            print(S[x-1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]
    #print(N, Q, S, query)
    for q in query:
        if q[0] == '1':
            S = S[-int(q[1]):] + S[:-int(q[1])]
        else:
            print(S[int(q[1])-1])

=======
Suggestion 9

def main():
    N,Q = map(int, input().split())
    S = input()
    S = list(S)
    #print(S)
    query = [list(map(str, input().split())) for _ in range(Q)]
    
    for q in query:
        if q[0] == "1":
            for i in range(int(q[1])):
                tmp = S.pop()
                S.insert(0, tmp)
        else:
            print(S[int(q[1])-1])

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]

    # 1の回数をカウント
    cnt = 0
    for q in query:
        if q[0] == '1':
            cnt += int(q[1])

    # 1の回数をNで割った余りを取得
    cnt %= N

    # 1の回数をNで割った余りをSから取得
    ans = S[cnt:] + S[:cnt]
    print(ans)

    # 2のクエリの場合は、Sから取得した文字列のインデックスを出力
    for q in query:
        if q[0] == '2':
            print(ans[int(q[1]) - 1])
