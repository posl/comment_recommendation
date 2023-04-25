Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        score = 0
        cnt = 0
        cycle = []
        while True:
            score += C[P[i]-1]
            cycle.append(P[i]-1)
            i = P[i]-1
            cnt += 1
            if cnt > K:
                break
            if i == cycle[0]:
                break
        if score <= 0:
            ans = max(ans, max(C))
            continue
        else:
            tmp = score * ((K-cnt)//cnt)
            ans = max(ans, tmp + max(C))
            if (K-cnt) % cnt != 0:
                tmp += sum(C[cycle[0]:(K-cnt)%cnt])
                ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        score = 0
        loop = []
        j = i
        while True:
            score += C[j]
            j = P[j] - 1
            loop.append(j)
            if j == i:
                break
        loop_score = 0
        loop_score_max = 0
        for i in range(len(loop)):
            loop_score += C[loop[i]]
            if i < K:
                loop_score_max = max(loop_score_max, loop_score)
            if i >= K:
                loop_score_max = max(loop_score_max, loop_score, loop_score + loop_score_max)
        ans = max(ans, loop_score_max)
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        x = i
        score = 0
        l = []
        for j in range(k):
            x = p[x]-1
            score += c[x]
            l.append(c[x])
            if x == i:
                break
        if score > 0:
            ans = max(ans, score*(k//(j+1)) + sum(l[0:k%(j+1)]))
        else:
            ans = max(ans, sum(l[0:k]))
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**10
    for i in range(N):
        v = i
        s = 0
        p = []
        while True:
            v = P[v] - 1
            s += C[v]
            p.append(C[v])
            if v == i:
                break
        if s > 0:
            x = K // len(p)
            ans = max(ans, x * s + max(0, max(p)))
        else:
            ans = max(ans, max(p))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        # i番目のマスからスタートする
        # そのマスに到達するまでのループの長さを求める
        loop_len = 0
        j = i
        while True:
            j = p[j]
            loop_len += 1
            if j == i:
                break
        # ループの長さがk以下なら、ループの全ての要素を通る
        # ループの長さがkより大きければ、ループの長さがkになるまでの要素を通る
        # それぞれの場合で、最大の値を求める
        if loop_len <= k:
            loop_max = 0
            for j in range(loop_len):
                loop_max += c[p[i + j]]
                ans = max(ans, loop_max + (k - loop_len) // loop_len * max(0, loop_max))
        else:
            loop_max = 0
            for j in range(k):
                loop_max += c[p[i + j]]
                ans = max(ans, loop_max)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        tmp = 0
        cnt = 0
        while cnt < k:
            tmp += c[p[i] - 1]
            i = p[i] - 1
            cnt += 1
            if i == p[i] - 1:
                break
        if tmp > 0:
            ans = max(ans, tmp * ((k - cnt) // cnt) + max(0, max(c)))
        else:
            ans = max(ans, tmp * ((k - cnt) // cnt) + max(0, max(c[:i + 1])))
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))
    ans = -10**9
    for start in range(N):
        now = start
        score = 0
        loop = 0
        while True:
            score += C[now]
            now = P[now]
            loop += 1
            if now == start:
                break
        if score > 0:
            loop = min(loop, K)
            num = K // loop
            rem = K % loop
            ans = max(ans, score * num + sum(C[P[i]] for i in range(rem)))
        else:
            ans = max(ans, sum(C[P[i]] for i in range(min(loop, K))))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # print(N, K)
    # print(P)
    # print(C)

    # サイクルを見つける
    # まず、サイクルの長さを求める
    # その後、サイクルの最大値を求める
    # その後、サイクルの最大値をK回以上使う場合を考える
    # その後、サイクルの最大値をK回以下使う場合を考える

    # サイクルを見つける
    # サイクルの長さを求める
    # サイクルの最大値を求める
    # サイクルの最大値をK回以上使う場合を考える
    # サイクルの最大値をK回以下使う場合を考える

    # サイクルを見つける
    # サイクルの長さを求める
    # サイクルの最大値を求める
    # サイクルの最大値をK回以上使う場合を考える
    # サイクルの最大値をK回以下使う場合を考える

    # サイクルを見つける
    # サイクルの長さを求める
    # サイクルの最大値を求める
    # サイクルの最大値をK回以上使う場合を考える
    # サイクルの最大値をK回以下使う場合を考える

    # サイクルを見つける
    # サイクルの長さを求める
    # サイクルの最大値を求める
    # サ

=======
Suggestion 9

def main():
    N,K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**10
    for i in range(N):
        score = 0
        x = i
        cnt = 0
        while cnt < K:
            x = P[x] - 1
            score += C[x]
            cnt += 1
            if x == i:
                break
        if score <= 0:
            continue
        else:
            if cnt == K:
                ans = max(ans, score)
            else:
                loop = K // cnt
                loop_score = score * loop
                ans = max(ans, loop_score)
                rest = K % cnt
                rest_score = 0
                for j in range(rest):
                    rest_score += C[P[x] - 1]
                    x = P[x] - 1
                    ans = max(ans, loop_score + rest_score)
    print(ans)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    P = [p-1 for p in P]
    ans = -10**9
    for i in range(N):
        score = 0
        visited = [False]*N
        visited[i] = True
        score += C[i]
        j = P[i]
        while not visited[j]:
            visited[j] = True
            score += C[j]
            j = P[j]
        if score > 0:
            cycle = 0
            while not visited[j]:
                visited[j] = True
                cycle += C[j]
                j = P[j]
            m = K//(cycle//score)
            score = score*(m-1) + cycle*(m-1)*(m-2)//2 + score*(K-cycle//score*(m-1))
        ans = max(ans,score)
    print(ans)
