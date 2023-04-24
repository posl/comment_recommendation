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

    correct = 0
    penalty = 0
    AC = [False] * (N+1)
    WA = [0] * (N+1)
    for i in range(M):
        if not AC[p[i]]:
            if S[i] == "AC":
                AC[p[i]] = True
                correct += 1
                penalty += WA[p[i]]
            else:
                WA[p[i]] += 1

    print(correct, penalty)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    ac = [0] * (n + 1)
    wa = [0] * (n + 1)
    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if ac[p] == 0:
            if s == 'AC':
                ac[p] = 1
            else:
                wa[p] += 1
    print(sum(ac), sum(wa[i] if ac[i] else 0 for i in range(n + 1)))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    p = [0] * m
    s = [0] * m
    for i in range(m):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
        if s[i] == "AC":
            s[i] = 1
        else:
            s[i] = 0
    wa = [0] * (n + 1)
    ac = [0] * (n + 1)
    for i in range(m):
        if ac[p[i]] == 0:
            if s[i] == 1:
                ac[p[i]] = 1
            else:
                wa[p[i]] += 1
    correct = 0
    penalty = 0
    for i in range(1, n + 1):
        if ac[i] == 1:
            correct += 1
            penalty += wa[i]
    print(correct, penalty)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    ac = [0] * N
    wa = [0] * N
    for _ in range(M):
        p, S = input().split()
        p = int(p) - 1
        if ac[p] == 0:
            if S == "AC":
                ac[p] = 1
            else:
                wa[p] += 1
    ac_sum = sum(ac)
    wa_sum = sum([wa[i] for i in range(N) if ac[i] == 1])
    print(ac_sum, wa_sum)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(M):
        p, s = input().split()
        p = int(p) - 1
        if A[p] == 0:
            if s == 'AC':
                A[p] = 1
            else:
                B[p] += 1
    AC = sum(A)
    WA = 0
    for i in range(N):
        if A[i] == 1:
            WA += B[i]
    print(AC, WA)

=======
Suggestion 6

def main():
    #input
    N, M = map(int, input().split())
    AC = [0] * N
    WA = [0] * N
    for _ in range(M):
        p, S = input().split()
        p = int(p) - 1
        if AC[p] == 0:
            if S == 'AC':
                AC[p] = 1
            else:
                WA[p] += 1

    #compute
    ans1 = sum(AC)
    ans2 = 0
    for i in range(N):
        if AC[i] == 1:
            ans2 += WA[i]

    #output
    print(ans1, ans2)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    correct = 0
    penalty = 0
    ac = [False] * (n + 1)
    wa = [0] * (n + 1)
    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if ac[p]:
            continue
        if s == "AC":
            correct += 1
            penalty += wa[p]
            ac[p] = True
        else:
            wa[p] += 1
    print(correct, penalty)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    correct = 0
    penalty = 0
    AC = [0] * (N+1)
    WA = [0] * (N+1)
    for i in range(M):
        p, S = input().split()
        p = int(p)
        if AC[p] == 0:
            if S == "AC":
                AC[p] = 1
                correct += 1
                penalty += WA[p]
            else:
                WA[p] += 1
    print(correct, penalty)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = [list(input().split()) for _ in range(M)]
    S.reverse()

    ans = [0, 0]
    AC = [0] * (N + 1)

    for i in range(M):
        if AC[int(S[i][0])] == 0:
            if S[i][1] == 'AC':
                AC[int(S[i][0])] = 1
                ans[0] += 1
            else:
                ans[1] += 1
        else:
            if S[i][1] == 'AC':
                continue
            else:
                ans[1] += 1

    print(ans[0], ans[1])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    S = [input().split() for _ in range(M)]

    # WAの数を記録するリスト
    WA = [0] * (N + 1)
    # ACしたかどうかを記録するリスト
    AC = [False] * (N + 1)

    for p, s in S:
        p = int(p)
        if s == "AC":
            AC[p] = True
        else:
            if not AC[p]:
                WA[p] += 1

    # ACした問題の合計
    ac_cnt = sum(AC)

    # WAした問題の合計
    wa_cnt = 0
    for i in range(1, N + 1):
        if AC[i]:
            wa_cnt += WA[i]

    print(ac_cnt, wa_cnt)
