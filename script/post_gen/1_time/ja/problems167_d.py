Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    #print(N, K)
    #print(A)

    # 1からスタート
    # K回テレポートする
    # K回目に到着する町を出力

    # 1からスタート
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]] -> ...
    # 1 -> A[0] -> A[A[0]] -> A[A[A[0]]] -> A[A[A[A[0]]]]

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, -1)
    ans = 1
    for i in range(K):
        ans = A[ans]
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    #print(a)
    visited = [0] * n
    num = 0
    while k > 0:
        if visited[num] == 1:
            break
        visited[num] = 1
        num = a[num]
        k -= 1
    #print(num)
    #print(visited)
    if k == 0:
        print(num + 1)
    else:
        loop = 0
        for i in range(n):
            if visited[i] == 1:
                loop += 1
        k %= loop
        #print(loop)
        #print(k)
        for i in range(k):
            num = a[num]
        print(num + 1)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    # 今いる町
    now = 0
    # 今回のテレポートで到達する町
    next = 0
    # 町の数
    town = [0]

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 町iに到達するために必要なテレポーターの回数
    # 初期値は-1
    # 到達できない場合は-1
    cnt = [-1] * N

    # 町1に到達するために必要なテレポーターの回数は0
    cnt[0] = 0

    # 町1からテレポーターを使って移動した場合の移動先
    next = 1

    # 町1からテレポーターを使って移動した場合の移動先が
    # 町1に戻ってくるまで繰り返す
    while cnt[next - 1] == -1:
        # 町nextに到達するために必要なテレポーターの回数は
        # 町next-1に到達するために必要なテレポーターの回数+1
        cnt[next - 1] = cnt[A[next - 1] - 1] + 1

        # 町nextに到達するために必要なテレポーターの回数が
        # K回を超える場合は
        # 町nextに到達するために必要なテレポーターの回数は
        # 町Nに到達するために必要なテレポーターの回数+1
        if cnt[next - 1] > K:
            cnt[next - 1] = cnt[N - 1] + 1

        # 町nextに到達するために必要なテレポーターの回数が
        # K回を超えない場合は
        # 町nextに到達するために必要なテレポーターの回数は
        #

=======
Suggestion 6

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a=[x-1 for x in a]
    k-=1
    visited=[0]*n
    visited[0]=1
    now=0
    while k>0:
        if visited[a[now]]==1:
            break
        visited[a[now]]=1
        now=a[now]
        k-=1
    if k==0:
        print(now+1)
        return
    k%=visited[a[now]]-1
    now=a[now]
    while k>0:
        now=a[now]
        k-=1
    print(now+1)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]

    # 1からの距離を計算
    dist = [0]
    now = 0
    for i in range(N):
        now = A[now]
        dist.append(now)

    # 1からの距離がループするまでの距離を計算
    loop = [0]
    now = 0
    for i in range(N):
        now = dist[now]
        loop.append(now)
        if now == 0:
            break

    # 1からの距離がループするまでの距離を計算
    loop = [0]
    now = 0
    for i in range(N):
        now = dist[now]
        loop.append(now)
        if now == 0:
            break

    # K回テレポートしたときの町を計算
    if K <= len(loop)-1:
        print(loop[K]+1)
    else:
        K -= len(loop)-1
        K %= len(loop)-1
        print(loop[K]+1)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]

    # 1回目の移動先
    b = [0] * n
    for i in range(n):
        b[i] = a[i]

    # 2回目の移動先
    c = [0] * n
    for i in range(n):
        c[i] = b[b[i]]

    # 3回目の移動先
    d = [0] * n
    for i in range(n):
        d[i] = c[c[i]]

    # 4回目の移動先
    e = [0] * n
    for i in range(n):
        e[i] = d[d[i]]

    # 5回目の移動先
    f = [0] * n
    for i in range(n):
        f[i] = e[e[i]]

    # 6回目の移動先
    g = [0] * n
    for i in range(n):
        g[i] = f[f[i]]

    # 7回目の移動先
    h = [0] * n
    for i in range(n):
        h[i] = g[g[i]]

    # 8回目の移動先
    i = [0] * n
    for i in range(n):
        i[i] = h[h[i]]

    # 9回目の移動先
    j = [0] * n
    for i in range(n):
        j[i] = i[i][i[i]]

    # 10回目の移動先
    k = [0] * n
    for i in range(n):
        k[i] = j[j[i]]

    # 11回目の移動先
    l = [0] * n
    for i in range(n):
        l[i] = k[k[i]]

    # 12回目の移動先
    m = [0] * n
    for i in range(n):
        m[i] = l[l[i]]

    # 13回目の移動先
    n = [0] * n
    for i in range(n):
        n[i

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    #print(a)

    #a[i]に到達するまでの移動回数を記録
    #a[i]に到達するまでの移動回数がk以上ならループが確定
    #ループの最初の町とループの最後の町を求める
    #ループの最初の町に到達するまでの移動回数を求める
    #ループの長さを求める
    #ループの最初の町に到達するまでの移動回数を引いた回数を求める
    #ループの長さで割った余りを求める
    #ループの最初の町から余り分移動する
    #ループの最初の町に到達するまでの移動回数を求める
    #ループの最初の町に到達するまでの移動回数を引いた回数を求める
    #ループの最初の町から余り分移動する
    #ループの最初の町に到達するまでの移動回数を求める
    #ループの最初の町に到達するまでの移動回数を引いた回数を求める
    #ループの最初の町から余り分移動する
    #ループの最初の町に到達するまでの移動回数を求める
    #ループの最初の町に到達するまでの移動回数を引いた回数を求める
    #ループの最初の町から余り分移動する
    #ループの最初の町に到達するまでの移

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    #print(A)
    #print(N, K)

    #K回テレポートするまでのループ
    for i in range(K):
        #print(A[i])
        if A[i] == 2:
            print(2)
            break
        else:
            A.append(A[A[i]])
    else:
        #K回テレポートした後のループ
        #print(A)
        #print(K%N)
        print(A[K%N])
