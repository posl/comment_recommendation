Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(N):
        tmp = 0
        tmpC = []
        j = i
        while True:
            tmp += C[P[j] - 1]
            tmpC.append(C[P[j] - 1])
            j = P[j] - 1
            if j == i:
                break
        if tmp > 0:
            num = K // len(tmpC)
            ans = max(ans, tmp * num + sum(tmpC[:K % len(tmpC)]))
        else:
            ans = max(ans, sum(tmpC[:K]))
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
            if j in loop:
                break
            loop.append(j)
        if score <= 0:
            ans = max(ans, max(C))
        else:
            cnt = 0
            for j in loop:
                cnt += 1
                if j == i:
                    break
            ans = max(ans, max(C) * (K // cnt) + max(C[:K % cnt + 1]))
    print(ans)

main()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        j = i
        s = 0
        l = 0
        while True:
            j = p[j] - 1
            s += c[j]
            l += 1
            if j == i:
                break
        if s <= 0:
            ans = max(ans, max(c))
        else:
            m = k // l
            ans = max(ans, max(c[:i + 1]) + m * s)
            ans = max(ans, max(c[:j + 1]) + (m - 1) * s)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        tmp = 0
        cnt = 0
        j = i
        while cnt < k:
            j = p[j] - 1
            tmp += c[j]
            cnt += 1
            if j == i:
                break
        if tmp <= 0:
            continue
        if cnt == k:
            ans = max(ans, tmp)
        else:
            ans = max(ans, tmp * ((k - cnt) // cnt) + max(0, max(c[j + 1:] + c[:j + 1])))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = -10 ** 10
    for i in range(n):
        path = []
        j = i
        while True:
            path.append(j)
            j = p[j]
            if j == i:
                break
        score = 0
        for j in path:
            score += c[j]
        if score <= 0:
            continue
        score *= (k // len(path))
        k_ = k % len(path)
        score_ = 0
        for j in range(k_):
            score_ += c[path[j]]
        ans = max(ans, score + score_)
    for i in range(n):
        score = 0
        j = i
        for _ in range(k):
            j = p[j]
            score += c[j]
            if j == i:
                break
        ans = max(ans, score)
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(N):
        s = []
        j = i
        while True:
            s.append(C[j])
            j = P[j] - 1
            if j == i:
                break
        l = len(s)
        score = 0
        for k in range(l):
            score += s[k]
            if score <= 0:
                continue
            if K < k + 1:
                break
            if l < K:
                ans = max(ans, score * (K // (k + 1)))
            else:
                ans = max(ans, score)
    print(ans)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**9
    for i in range(n):
        s = 0
        j = i
        for _ in range(k):
            j = p[j]-1
            s += c[j]
            if j == i:
                break
        if s > 0:
            ans = max(ans, s*((k-1)//(j-i+1))+max(sum(c[i:j+1]) for i, j in ((i, i+(k-1)%(j-i+1)) for i in range(j+1))))
        else:
            ans = max(ans, max(sum(c[i:j+1]) for i, j in ((i, i+(k-1)%(j-i+1)) for i in range(j+1))))
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [p-1 for p in P]
    ans = -10**20
    for i in range(N):
        j = i
        cnt = 0
        tmp = 0
        while True:
            j = P[j]
            tmp += C[j]
            cnt += 1
            if j == i:
                break
        if tmp > 0:
            if K >= cnt:
                ans = max(ans, tmp*(K//cnt) + max(0, max(C)))
            else:
                ans = max(ans, max(C[:K]))
        else:
            ans = max(ans, max(C[:K]))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -10**18

    for i in range(N):
        x = i
        score = 0
        loop = []
        for j in range(K):
            x = P[x] - 1
            score += C[x]
            loop.append(C[x])
            if x == i:
                break

        if score <= 0 or len(loop) == K:
            ans = max(ans, score)
            continue

        loop_score = sum(loop)
        loop_count = (K - len(loop)) // len(loop)
        ans = max(ans, score + loop_score * loop_count)

        loop_score = loop_score * (loop_count + 1)
        loop = loop * (loop_count + 1)
        for j in range(K - len(loop)):
            loop_score += loop[j]
            ans = max(ans, loop_score)

    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**20
    for i in range(N):
        tmp = 0
        cnt = 0
        j = i
        while cnt < K:
            tmp += C[P[j]-1]
            if tmp > ans:
                ans = tmp
            j = P[j]-1
            cnt += 1
            if j == i:
                break
        if cnt == K:
            continue
        else:
            if tmp <= 0:
                continue
            else:
                tmp *= (K-cnt)//cnt
                if tmp > ans:
                    ans = tmp
                tmp = 0
                cnt = 0
                j = i
                while cnt < (K-cnt)%cnt:
                    tmp += C[P[j]-1]
                    if tmp > ans:
                        ans = tmp
                    j = P[j]-1
                    cnt += 1
                    if j == i:
                        break
    print(ans)
main()
