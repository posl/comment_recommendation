Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0]+1):
                if i >> (S[j][k]-1) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    k = [0] * M
    s = [[0] * N for _ in range(M)]
    p = [0] * M
    for i in range(M):
        s[i] = list(map(int, input().split()))
        k[i] = s[i][0]
        s[i].pop(0)
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        cnt = 0
        for j in range(M):
            c = 0
            for l in range(k[j]):
                if (i >> (s[j][l] - 1)) & 1:
                    c += 1
            if c % 2 == p[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    K = []
    S = []
    for i in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        cnt = 0
        for j in range(M):
            on = 0
            for k in range(K[j]):
                if i & (1 << (S[j][k] - 1)):
                    on += 1
            if on % 2 == P[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = [[int(i) for i in input().split()] for _ in range(M)]
    P = [int(i) for i in input().split()]
    ans = 0
    for i in range(2**N):
        for j in range(M):
            if P[j] != sum([i >> (s-1) & 1 for s in S[j][1:]]) & 1:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        k, *s = map(int, input().split())
        S.append(s)
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(M):
            cnt = 0
            for s in S[j]:
                if (i >> (s - 1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    S = []
    P = []
    for i in range(M):
        S.append(list(map(int, input().split())))
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** N):
        flag = 0
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0] + 1):
                if ((i >> (S[j][k] - 1)) & 1):
                    cnt += 1
            if cnt % 2 == P[j]:
                flag += 1
        if flag == M:
            ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    S = []
    for i in range(M):
        S.append(list(map(int, input().split())))
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        tmp = 0
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0]+1):
                if i >> (S[j][k]-1) & 1:
                    cnt += 1
            if cnt % 2 == P[j]:
                tmp += 1
        if tmp == M:
            ans += 1
    print(ans)
solve()

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    S = []
    P = []
    for i in range(M):
        S.append(list(map(int,input().split())))
    P = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1,len(S[j])):
                if (i >> (S[j][k]-1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 9

def solve(n,m,k,s,p):
    ans = 0
    for i in range(2**n):
        ok = True
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                if (i >> (s[j][l]-1)) & 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                ok = False
        if ok:
            ans += 1
    return ans

n,m = map(int, input().split())
k = []
s = []
for i in range(m):
    k.append(0)
    s.append([])
for i in range(m):
    a = list(map(int, input().split()))
    k[i] = a[0]
    for j in range(k[i]):
        s[i].append(a[j+1])
p = list(map(int, input().split()))
print(solve(n,m,k,s,p))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    switch = [[0 for j in range(N)] for i in range(M)]
    for i in range(M):
        s = list(map(int, input().split()))
        for j in range(s[0]):
            switch[i][s[j+1]-1] = 1
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        f = 1
        for j in range(M):
            if sum([switch[j][k] for k in range(N) if (i >> k) & 1]) % 2 != p[j]:
                f = 0
                break
        ans += f
    print(ans)
main()
