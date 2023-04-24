Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    K = []
    S = []
    P = []
    for _ in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(K[j]):
                if (i >> (S[j][k] - 1) & 1):
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for _ in range(M)]
    p = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(M):
            cnt = 0
            for l in range(k[j]):
                if (i >> (s[j][l] - 1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for _ in range(M)]
    p = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(M):
            cnt = 0
            for l in range(k[j]):
                if (i >> (s[j][l] - 1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for i in range(M)]
    p = [0] * M
    for i in range(M):
        line = list(map(int, input().split()))
        k[i] = line[0]
        for j in range(k[i]):
            s[i][line[j+1]-1] = 1
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        tmp = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    tmp[k] += s[k][j]
        flag = True
        for j in range(M):
            if tmp[j] % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [0] * M
    p = [0] * M
    for i in range(M):
        k[i], *s[i] = map(int, input().split())
    p = list(map(int, input().split()))

    ans = 0
    for bit in range(2 ** N):
        ok = True
        for i in range(M):
            cnt = 0
            for j in range(k[i]):
                if bit & (1 << (s[i][j] - 1)):
                    cnt += 1
            if cnt % 2 != p[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s[1:])
        P.append(s[0])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            c = 0
            for k in S[j]:
                if (i >> (k-1)) & 1:
                    c += 1
            if c % 2 != P[j]:
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
        k_i = list(map(int, input().split()))
        k.append(k_i[0])
        s.append(k_i[1:])
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(M):
            cnt = 0
            for l in range(k[j]):
                if (i >> (s[j][l]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    s = []
    p = []
    for _ in range(M):
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            tmp = 0
            for k in range(1, s[j][0]+1):
                if (i >> (s[j][k]-1)) & 1:
                    tmp += 1
            if tmp % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    switch = []
    for _ in range(M):
        switch.append(list(map(int, input().split())))
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        on = [0] * N
        for j in range(N):
            if ((i >> j) & 1):
                on[j] = 1

        flag = True
        for j in range(M):
            count = 0
            for k in range(1, switch[j][0]+1):
                if on[switch[j][k]-1] == 1:
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
    light = []
    for _ in range(M):
        light.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        count = 0
        for j in range(M):
            on = 0
            for k in range(1, light[j][0] + 1):
                if (i >> (light[j][k] - 1)) & 1:
                    on += 1
            if on % 2 == p[j]:
                count += 1
        if count == M:
            ans += 1
    print(ans)
