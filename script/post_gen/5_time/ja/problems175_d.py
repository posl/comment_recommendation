Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    P = [x-1 for x in P]
    ans = -10**18
    for i in range(N):
        score = 0
        cnt = 0
        now = i
        while True:
            now = P[now]
            score += C[now]
            cnt += 1
            if now == i:
                break
            if cnt == K:
                break
        if score > 0:
            m = (K-cnt)//cnt
            score += score*m
        ans = max(ans,score)
    print(ans)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))

    ans = -float('inf')
    for i in range(N):
        #print(i)
        tmp = 0
        t = 0
        j = i
        while True:
            #print(j)
            tmp += C[j]
            j = P[j]-1
            t += 1
            if j == i:
                break
            if t == K:
                break
        #print(tmp)
        if t == K:
            ans = max(ans,tmp)
        else:
            if tmp > 0:
                if K % t == 0:
                    ans = max(ans,tmp*(K//t))
                else:
                    ans = max(ans,tmp*(K//t)+max(0,tmp))
            else:
                ans = max(ans,tmp)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = -10**18
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x] - 1
            s += c[x]
            t += 1
            if x == i:
                break
            if t >= k:
                break
        if c[x] > 0:
            u = (k - t) // t
            s += s * u
            t += t * u
            v = 0
            while v < k - t:
                x = p[x] - 1
                s += c[x]
                v += 1
        ans = max(ans, s)
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = -10**18
    for i in range(n):
        score = 0
        cnt = 0
        now = i
        while True:
            now = p[now] - 1
            score += c[now]
            cnt += 1
            if now == i:
                break
        #print(score, cnt)
        if score > 0:
            ans = max(ans, score * (k // cnt))
            if k % cnt != 0:
                ans = max(ans, score * (k // cnt - 1) + max(0, score))
        else:
            ans = max(ans, score)
    print(ans)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 1回移動した時の最大値を求める
    max_score = -10**18
    for i in range(N):
        score = 0
        next = i
        for j in range(K):
            next = P[next] - 1
            score += C[next]
            max_score = max(max_score, score)

    # 1回移動した時の最大値が正の場合、
    # K回移動した時の最大値は、
    # K回移動した時の最大値 = (K // N) * (1回移動した時の最大値) + (K % N)回移動した時の最大値
    if max_score > 0:
        # K回移動した時の最大値 = (K // N) * (1回移動した時の最大値) + (K % N)回移動した時の最大値
        # (K // N) * (1回移動した時の最大値) は、K回移動した時の最大値の候補の一つ
        # (K % N)回移動した時の最大値は、
        # 1回移動した時の最大値から、(K % N)回移動した時の最大値を求める
        # (K % N)回移動した時の最大値は、
        # 1回移動した時の最大値から、(K % N)回移動した時の最大値を求める
        # 1回移動した時の最大値は、
        # 1回移動した時の最大値から、(K % N)回移動した時の最大値を求める
        # 1回移動した時の最大値は、
        # 1回移動した時の最大値

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    max = -float('inf')
    for i in range(N):
        score = 0
        next = i
        for j in range(K):
            score += C[next]
            next = P[next] - 1
            if score > max:
                max = score
        if score > max:
            max = score

    print(max)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(n):
        next = p[i] - 1
        score = 0
        cnt = 0
        while cnt < k:
            cnt += 1
            score += c[next]
            next = p[next] - 1
            ans = max(ans, score)
            if next == i:
                break
    print(ans)
main()

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    P = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    P = [x - 1 for x in P]
    P = [P[x] for x in P]
    C = [C[x] for x in P]
    #print(P)
    #print(C)
    ans = -10**18
    for i in range(N):
        now = i
        score = 0
        cnt = 0
        while True:
            now = P[now]
            score += C[now]
            cnt += 1
            if cnt >= K:
                break
            if now == i:
                break
        #print(i, now, score, cnt)
        if cnt < K:
            if score > 0:
                max_score = score * (K // cnt - 1)
                if cnt == 1:
                    max_score += score
                else:
                    max_score += score + max(0, score * (K % cnt - 1))
            else:
                max_score = score + max(0, score * (K % cnt - 1))
            ans = max(ans, max_score)
        else:
            ans = max(ans, score)
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -10**18
    for i in range(N):
        score = 0
        j = i
        cnt = 0
        while True:
            score += C[j]
            j = P[j] - 1
            cnt += 1
            if j == i:
                break
            if cnt == K:
                break
        if score > ans:
            ans = score

    print(ans)

main()
