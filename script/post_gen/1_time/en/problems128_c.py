Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        cnt = 0
        for j in range(M):
            tmp = 0
            for k in range(1, S[j][0]+1):
                if (i >> (S[j][k]-1)) & 1:
                    tmp += 1
            if tmp % 2 == P[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    K = []
    S = []
    P = []
    for i in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        on = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    if j+1 in S[k]:
                        on[k] += 1

        ok = True
        for k in range(M):
            if on[k] % 2 != P[k]:
                ok = False
                break

        if ok:
            ans += 1

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for i in range(M)]
    p = [0] * M
    for i in range(M):
        s[i] = list(map(int, input().split()))
        k[i] = s[i][0]
        s[i] = s[i][1:]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = 1
        for j in range(M):
            count = 0
            for l in range(k[j]):
                if (i >> (s[j][l] - 1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = 0
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    K, S, P = [], [], []
    for _ in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        on = [0]*M
        for j in range(N):
            if ((i >> j) & 1):
                for k in range(M):
                    if j+1 in S[k]:
                        on[k] += 1
        flag = 1
        for k in range(M):
            if on[k] % 2 != P[k]:
                flag = 0
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [0] * M
    p = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
        s[i] = list(map(lambda x: x - 1, s[i]))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        on = [0] * N
        for j in range(N):
            if (i >> j) & 1:
                on[j] = 1
        if all([sum([on[s[i][j]] for j in range(k[i])]) % 2 == p[i] for i in range(M)]):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(k[i][1:])
        p.append(k[i][0])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for k in s[j]:
                if (i >> (k-1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(M):
        k.append(int(input().split()[0]))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for l in range(k[j]):
                if i & (1 << (s[j][l] - 1)) > 0:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(M):
            cnt = 0
            for k in range(S[j][0]):
                if (i >> (S[j][k+1]-1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    bulbs = [list(map(int, input().split())) for i in range(M)]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for k in range(1, bulbs[j][0]+1):
                if i >> (bulbs[j][k]-1) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())

    bulbs = []
    for _ in range(M):
        bulbs.append(list(map(int, input().split())))

    p = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        on = [False] * N
        for j in range(N):
            if ((i >> j) & 1):
                on[j] = True

        ok = True
        for j in range(M):
            count = 0
            for k in bulbs[j][1:]:
                if on[k-1]:
                    count += 1

            if count % 2 != p[j]:
                ok = False
                break

        if ok:
            ans += 1

    print(ans)
