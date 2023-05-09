Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [x - 1 for x in P]
    max_score = -10**18
    for i in range(N):
        score = 0
        pos = i
        for j in range(K):
            pos = P[pos]
            score += C[pos]
            max_score = max(max_score, score)
            if pos == i:
                break
    print(max_score)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p - 1 for p in P]
    max_score = -10 ** 18
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        score = C[i]
        j = P[i]
        while not visited[j]:
            visited[j] = True
            score += C[j]
            j = P[j]
        if score > max_score:
            max_score = score
        if K > 1:
            cycle_score = score
            cycle_length = 1
            j = P[i]
            while j != i:
                cycle_score += C[j]
                j = P[j]
                cycle_length += 1
            cycle_score += (K - 2) // cycle_length * max(0, cycle_score)
            if cycle_score > max_score:
                max_score = cycle_score
    return max_score

print(solve())

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [p[i] - 1 for i in range(n)]
    visited = [False] * n
    max_score = -10 ** 18
    for i in range(n):
        if visited[i]:
            continue
        score = 0
        visited[i] = True
        current = i
        cycle = []
        while True:
            current = p[current]
            score += c[current]
            visited[current] = True
            cycle.append(current)
            if current == i:
                break
        cycle_len = len(cycle)
        cycle_score = 0
        for j in range(cycle_len):
            cycle_score += c[cycle[j]]
            max_score = max(max_score, cycle_score)
        if score > 0:
            cycle_score = 0
            for j in range(cycle_len):
                cycle_score += c[cycle[j]]
                if j + 1 > k:
                    break
                max_score = max(max_score, cycle_score + (k - j - 1) // cycle_len * score)
    print(max_score)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [x - 1 for x in p]

    ans = -10 ** 18
    for i in range(n):
        x = i
        s = 0
        t = 0
        while True:
            x = p[x]
            s += c[x]
            t += 1
            if x == i:
                break
            if t == k:
                break
        if s > 0:
            u = (k - t) // t
            s += s * u
            t += t * u
        for j in range(k - t):
            x = p[x]
            s += c[x]
            ans = max(ans, s)
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -10 ** 18
    for i in range(N):
        score = 0
        cur = i
        for _ in range(K):
            cur = P[cur] - 1
            score += C[cur]
            ans = max(ans, score)
            if cur == i: break
    print(ans)

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    visited = [False] * N
    visited[0] = True
    score = [0] * N
    score[0] = C[0]
    cycle = []
    cycle_score = []
    cycle_score.append(score[0])
    cycle.append(0)
    while True:
        p = P[cycle[-1]]
        if visited[p]:
            break
        visited[p] = True
        cycle.append(p)
        score[p] = score[cycle[-2]] + C[p]
        cycle_score.append(score[p])
    cycle_length = len(cycle)
    if K <= cycle_length:
        return max(cycle_score[:K])
    else:
        cycle_sum = sum(cycle_score)
        cycle_max = max(cycle_score)
        cycle_sum += max(0, cycle_sum) * ((K - cycle_length) // cycle_length)
        cycle_max = max(cycle_max, cycle_max + max(0, cycle_sum) * ((K - cycle_length) % cycle_length))
        return cycle_max
print(solve())

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = -10**18
    for i in range(n):
        now = i
        path = []
        total = 0
        while True:
            now = p[now] - 1
            path.append(c[now])
            total += c[now]
            if now == i:
                break
        if total > 0:
            if k < len(path):
                ans = max(ans, max(path[:k]))
            else:
                ans = max(ans, total * (k // len(path) - 1) + max(path))
        else:
            ans = max(ans, max(path))
    print(ans)

=======
Suggestion 8

def solve():
    N,K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [x-1 for x in P]
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
            tmp = (K//cnt-1)*score
            now = i
            for _ in range(K%cnt):
                now = P[now]
                tmp += C[now]
            ans = max(ans,tmp)
        else:
            tmp = 0
            now = i
            for _ in range(min(K,cnt)):
                now = P[now]
                tmp += C[now]
            ans = max(ans,tmp)
    print(ans)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = -10**9
    for i in range(n):
        now = i
        score = 0
        num = 0
        while num < k:
            now = p[now]-1
            score += c[now]
            num += 1
            ans = max(ans,score)
            if score > 0 and num < k:
                score += (k//num-1)*score
                num += (k//num-1)*num
    print(ans)

=======
Suggestion 10

def solve(n, k, p, c):
    ans = -10**18
    for i in range(n):
        a = []
        v = i
        while True:
            v = p[v]-1
            a.append(c[v])
            if v == i:
                break
        s = sum(a)
        l = len(a)
        t = 0
        for j in range(l):
            t += a[j]
            if j+1 > k:
                break
            now = t
            if s > 0:
                e = (k-j-1)//l
                now += s*e
            ans = max(ans, now)
    return ans

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
print(solve(n, k, p, c))
