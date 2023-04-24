Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        flag = 1
        for j in range(M):
            cnt = 0
            for k in range(S[j][0]):
                if ((i >> (S[j][k+1] - 1)) & 1):
                    cnt += 1
            if (cnt % 2) != P[j]:
                flag = 0
                break
        if flag:
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
        on = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                for k in range(M):
                    if j+1 in S[k]:
                        on[k] += 1
        for j in range(M):
            if on[j] % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    k = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for l in k[j][1:]:
                if i & (1 << (l - 1)):
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for i in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        bit = [0]*N
        for j in range(N):
            if (i >> j) & 1:
                bit[j] = 1
        for j in range(M):
            cnt = 0
            for s in S[j][1:]:
                if bit[s-1] == 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for i in range(M)]
    p = [0] * M
    for i in range(M):
        input_list = list(map(int, input().split()))
        k[i] = input_list[0]
        for j in range(1, k[i] + 1):
            s[i][input_list[j] - 1] = 1
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        tmp = 0
        for j in range(M):
            cnt = 0
            for l in range(N):
                if s[j][l] == 1 and (i >> l & 1):
                    cnt += 1
            if cnt % 2 == p[j]:
                tmp += 1
        if tmp == M:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    s = [0] * M
    p = [0] * M
    for i in range(M):
        s[i] = list(map(int, input().split()))
        s[i].pop(0)
    p = list(map(int, input().split()))
    ans = 0
    for bit in range(2 ** N):
        flag = True
        for i in range(M):
            cnt = 0
            for j in range(len(s[i])):
                if (bit >> (s[i][j] - 1)) & 1:
                    cnt += 1
            if cnt % 2 != p[i]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(M):
        S.append(list(map(int, input().split())))
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        ok = True
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0]+1):
                if i & (1<<(S[j][k]-1)):
                    cnt += 1
            if cnt%2 != P[j]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    s = [[int(x) for x in input().split()] for _ in range(M)]
    p = [int(x) for x in input().split()]

    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, s[j][0]+1):
                if (i >> (s[j][k]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    s = []
    p = []
    for i in range(M):
        s.append(list(map(int, input().split())))
        s[i].pop(0)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in s[j]:
                if ((i >> (k - 1)) & 1) == 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    S = [0]*M
    P = [0]*M
    for i in range(M):
        S[i] = list(map(int,input().split()))
        S[i].pop(0)
    P = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in S[j]:
                if (i >> (k-1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
