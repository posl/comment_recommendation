Synthesizing 10/10 solutions

=======
Suggestion 1

def problem167_d():
    N, K = map(int, input().split())
    A = l

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    now = 0
    for i in range(60):
        if k & (1 << i):
            now = a[now]
        a = [a[a[j]] for j in range(n)]
    print(now + 1)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 町1から出発して、K回テレポートすると、どこの町にいるか
    # テレポートは、1回だけでなく、複数回使ってもよい
    # 町の番号は1からNまで
    # 町の番号は、1からNまで連続しているとは限らない

    # 町1から出発して、K回テレポートすると、どこの町にいるか
    # テレポートは、1回だけでなく、複数回使ってもよい
    # 町の番号は1からNまで
    # 町の番号は、1からNまで連続しているとは限らない

    # 町1から出発して、K回テレポートすると、どこの町にいるか
    # テレポートは、1回だけでなく、複数回使ってもよい
    # 町の番号は1からNまで
    # 町の番号は、1からNまで連続しているとは限らない
    # 町1から出発して、K回テレポートすると、どこの町にいるか
    # テレポートは、1回だけでなく、複数回使ってもよい
    # 町の番号は1からNまで
    # 町の番号は、1からNまで連続しているとは限らない

    # 町1から出発して、K回テレポートすると、どこの町にいるか
    # テレポートは、1回だけでなく、複数回使ってもよい
    # 町の番号は1からNま

=======
Suggestion 4

def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    while i < K:
        i += 1
        A = A[A[i-1]-1:]
        if len(A) == 0:
            break
    print(A[0])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - 1
    C = [0] * N
    C[0] = 1
    D = [0] * N
    D[0] = 0
    p = 0
    for i in range(1, N + 1):
        p = B[p]
        if C[p] == 1:
            break
        C[p] = 1
        D[p] = i
    if i == N:
        print(B[p] + 1)
    else:
        n = i - D[p]
        K = (K - D[p]) % n
        for i in range(K):
            p = B[p]
        print(p + 1)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    #print(N,K,A)

    #テレポートの移動先を格納するリスト
    teleport = [1]

    #テレポートの移動先を格納するリストのインデックス
    teleport_index = 0

    #テレポートの移動先を格納するリストの長さ
    teleport_len = 1

    #移動回数
    move_count = 0

    #移動先が変わらない場合のループ回数
    loop_count = 0

    #移動先が変わらない場合のループ回数
    loop_count_max = 0

    #テレポートの移動先を格納するリストの長さがNになるまでループ
    while teleport_len < N:

        #テレポートの移動先を格納するリストの長さがNになるまでループ
        while teleport_len < N:

            #テレポートの移動先を格納するリストのインデックスが移動回数より大きい場合
            if teleport_index > move_count:

                #移動回数をインクリメント
                move_count += 1

                #ループ回数をリセット
                loop_count = 0

                #テレポートの移動先を格納するリストのインデックスをリセット
                teleport_index = 0

                #テレポートの移動先を格納するリストの長さをリセット
                teleport_len = 1

                #テレポートの移動先を格納するリストをリセット
                teleport = [1]

                #print("move_count:",move_count)

                #print("teleport_index:",teleport_index)

                #print("teleport_len:",teleport_len)

                #print("teleport:",teleport)

                break

            #テレポートの移動先を格納するリ

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    T = [1]
    T.append(A[0])
    i = 0
    while(1):
        i = T[i]
        T.append(A[i-1])
        if(T[i] == 1):
            break
    if(K < len(T)):
        print(T[K])
    else:
        K -= i
        K %= (len(T) - i)
        print(T[i+K])

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    now = 1
    visited = [False] * (n + 1)
    visited[1] = True
    for i in range(k):
        now = a[now - 1]
        if visited[now]:
            break
        visited[now] = True
    if i == k - 1:
        print(now)
    else:
        loop = []
        loop.append(now)
        while True:
            now = a[now - 1]
            if now == loop[0]:
                break
            loop.append(now)
        print(loop[(k - i - 1) % len(loop)])

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    now = 1
    for i in range(K):
        now = A[now]
    print(now)
