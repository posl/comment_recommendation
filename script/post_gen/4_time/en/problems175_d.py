Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = -10 ** 18
    for i in range(N):
        score = 0
        v = i
        for _ in range(K):
            v = P[v]
            score += C[v]
            ans = max(ans, score)
            if v == i:
                break
    return ans

print(solve())

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [x - 1 for x in P]
    ans = -10 ** 18
    for i in range(N):
        j = P[i]
        s = []
        while j != i:
            s.append(C[j])
            j = P[j]
        s.append(C[i])
        t = [0]
        for x in s:
            t.append(t[-1] + x)
        for k in range(1, len(t)):
            if k > K:
                break
            if t[k] > 0:
                tmp = t[k] * ((K - k) // len(s))
                if tmp > ans:
                    ans = tmp
            if t[k] + t[-1] > ans:
                ans = t[k] + t[-1]
    print(ans)

solve()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = -10 ** 18
    for i in range(N):
        j = P[i]
        score = C[j]
        for _ in range(K - 1):
            j = P[j]
            score += C[j]
            ans = max(ans, score)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        x = i
        s = 0
        l = 0
        while True:
            x = p[x] - 1
            s += c[x]
            l += 1
            if x == i:
                break
            if l == k:
                break
        if s > 0:
            t = (k // l - 1) * s
            x = i
            u = 0
            while True:
                x = p[x] - 1
                u += c[x]
                if x == i:
                    break
                t = max(t, u)
            ans = max(ans, t)
        else:
            ans = max(ans, s)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(N):
        nxt = P[i] - 1
        score = 0
        cnt = 0
        while True:
            cnt += 1
            score += C[nxt]
            if nxt == i:
                break
            nxt = P[nxt] - 1
            if cnt == K:
                break
        if cnt < K and score > 0:
            score *= K // cnt
            ans = max(ans, score)
        ans = max(ans, score)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    max_score = -float('inf')
    for i in range(N):
        score = 0
        current = i
        for _ in range(K):
            current = P[current] - 1
            score += C[current]
            max_score = max(max_score, score)
            if current == i:
                break

    print(max_score)

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [i-1 for i in P]
    ans = -10**18
    for i in range(N):
        now = i
        score = 0
        cnt = 0
        while True:
            now = P[now]
            score += C[now]
            cnt += 1
            if now == i:
                break
        if score > 0:
            if K < cnt:
                tmp = 0
                now = i
                for j in range(K):
                    now = P[now]
                    tmp += C[now]
                ans = max(ans, tmp)
            else:
                if score > 0:
                    tmp = score * (K//cnt)
                    now = i
                    for j in range(K%cnt):
                        now = P[now]
                        tmp += C[now]
                    ans = max(ans, tmp)
    print(ans)
solve()

=======
Suggestion 8

def solve(N, K, P, C):
    ans = -10**18
    for i in range(N):
        j = P[i] - 1
        k = 0
        score = 0
        while j != i and k < K:
            score += C[j]
            ans = max(ans, score)
            j = P[j] - 1
            k += 1
        if k < K:
            l = min(K, K - (K - k) % (k + 1))
            if score > 0:
                ans = max(ans, score * (K // (k + 1)) + max(score * (l // (k + 1)), score + max(score * ((l - k - 1) // (k + 1)), 0)))
            else:
                ans = max(ans, score * (K // (k + 1)) + max(score * (l // (k + 1)), score + max(score * ((l - k - 1) // (k + 1)), 0)), score * (K // (k + 1)) + max(score * (l // (k + 1)), score + max(score * ((l - k - 1) // (k + 1)), 0)))
    return ans

=======
Suggestion 9

def solve(N, K, P, C):
    max_score = -10**10
    for i in range(N):
        score = 0
        cnt = 0
        j = i
        while cnt < K:
            cnt += 1
            j = P[j] - 1
            score += C[j]
            max_score = max(max_score, score)
            if j == i:
                break
    return max_score

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
print(solve(N, K, P, C))

=======
Suggestion 10

def solve(n,k,p,c):
    ans = -1000000000000000000
    for i in range(n):
        s = 0
        t = 0
        j = i
        while True:
            s += c[p[j]-1]
            t += 1
            j = p[j]-1
            if j==i:
                break
        if s > 0:
            u = (k//t-1)*s
            for j in range(k%t):
                u += c[p[(i+j)%n]-1]
            ans = max(ans,u)
        else:
            for j in range(min(k,t)):
                s += c[p[(i+j)%n]-1]
                ans = max(ans,s)
    return ans
