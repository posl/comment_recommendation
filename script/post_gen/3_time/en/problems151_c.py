Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    ans = [0] * N
    for i in range(M):
        if ans[p[i]-1] == 0 and S[i] == "AC":
            ans[p[i]-1] = i+1
    cnt = 0
    for i in range(N):
        if ans[i] != 0:
            cnt += 1
    ans2 = 0
    for i in range(M):
        if ans[p[i]-1] == i+1 and S[i] == "WA":
            ans2 += 1
    print(cnt, ans2)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    ans = 0
    penalty = 0
    ac = [0] * (N + 1)
    wa = [0] * (N + 1)
    for i in range(M):
        if ac[p[i]] == 1:
            continue
        if S[i] == "AC":
            ac[p[i]] = 1
            ans += 1
            penalty += wa[p[i]]
        else:
            wa[p[i]] += 1
    print(ans, penalty)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
    ans = [0] * N
    for i in range(M):
        if S[i] == 'WA':
            ans[p[i]-1] -= 1
        else:
            ans[p[i]-1] = 10000
    ans = [a for a in ans if a > 0]
    print(len(ans), sum(ans))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AC = [0 for _ in range(N)]
    WA = [0 for _ in range(N)]
    for _ in range(M):
        p, S = input().split()
        p = int(p)-1
        if AC[p] == 0:
            if S == "AC":
                AC[p] = 1
            else:
                WA[p] += 1
    AC = sum(AC)
    WA = sum([WA[i] for i in range(N) if AC[i] == 1])
    print(AC, WA)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(M):
        p, S = input().split()
        p = int(p) - 1
        if S == "AC":
            A[p] = 1
        else:
            if A[p] == 0:
                B[p] += 1
    ans = 0
    pen = 0
    for i in range(N):
        if A[i] == 1:
            ans += 1
            pen += B[i]
    print(ans, pen)

=======
Suggestion 6

def main():
    N, M = [int(x) for x in input().split()]
    AC = [0] * N
    WA = [0] * N
    for i in range(M):
        p, S = input().split()
        p = int(p) - 1
        if S == "AC":
            AC[p] = 1
        elif S == "WA" and AC[p] == 0:
            WA[p] += 1

    AC = sum(AC)
    WA = sum([WA[i] for i in range(N) if AC[i] == 1])
    print(AC, WA)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ans = [0] * n
    pen = [0] * n
    ac = [False] * n
    for _ in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            if not ac[p]:
                ac[p] = True
        else:
            if not ac[p]:
                pen[p] += 1
    for i in range(n):
        if ac[i]:
            ans[0] += 1
            ans[1] += pen[i]
    print(*ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AC = [False] * N
    WA = [0] * N
    ac_cnt = 0
    wa_cnt = 0
    for i in range(M):
        p, s = input().split()
        p = int(p) - 1
        if AC[p]:
            continue
        if s == 'AC':
            AC[p] = True
            ac_cnt += 1
            wa_cnt += WA[p]
        else:
            WA[p] += 1
    print(ac_cnt, wa_cnt)

=======
Suggestion 9

def main():
    # Read input
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)
    # Write output
    print(solve(N, M, p, S))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    p_ac = [0] * (N + 1)
    p_wa = [0] * (N + 1)
    for i in range(M):
        p[i], S[i] = input().split()
        p[i] = int(p[i])
        if S[i] == "AC":
            p_ac[p[i]] = 1
        else:
            if p_ac[p[i]] == 1:
                continue
            else:
                p_wa[p[i]] += 1
    ac = 0
    wa = 0
    for i in range(1, N + 1):
        if p_ac[i] == 1:
            ac += 1
            wa += p_wa[i]
    print(ac, wa)
