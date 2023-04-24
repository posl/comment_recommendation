Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    L_max = max(L)
    R_min = min(R)

    if R_min >= L_max:
        print(R_min - L_max + 1)
    else:
        print(0)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(M):
        l, r = map(int, input().split())
        L[l-1] += 1
        R[r-1] += 1
    ans = 0
    cnt = 0
    for i in range(N):
        cnt += L[i]
        if cnt == i + 1:
            ans += 1
        cnt -= R[i]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for i in range(M):
        l, r = map(int, input().split())
        L[l] += 1
        R[r] += 1
    ans = 0
    cnt = 0
    for i in range(1, N + 1):
        cnt += L[i]
        cnt -= R[i]
        if cnt == M:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    gates = [0] * N
    for i in range(M):
        L, R = map(int, input().split())
        gates[L-1] += 1
        if R < N:
            gates[R] -= 1
    for i in range(1, N):
        gates[i] += gates[i-1]
    print(gates.count(M))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    L = [LR[i][0] for i in range(M)]
    R = [LR[i][1] for i in range(M)]
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for i in range(M)]
    L = [LR[i][0] for i in range(M)]
    R = [LR[i][1] for i in range(M)]
    if max(L) > min(R):
        print(0)
    else:
        print(min(R) - max(L) + 1)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    gates = [list(map(int, input().split())) for _ in range(M)]
    gates.sort(key=lambda x: x[1])
    ans = 0
    R = 0
    for L, R in gates:
        if L > R:
            ans = 0
            break
        if L > R:
            break
        ans += 1
        R = R
    print(ans)
    return

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    L = [0 for _ in range(N)]
    R = [0 for _ in range(N)]
    for i in range(1, N+1):
        for l, r in LR:
            if l == i:
                L[i-1] += 1
            if r == i:
                R[i-1] += 1
    ans = 0
    for i in range(N):
        if L[i] == 1 and R[i] == 1:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 1-indexed
    gates = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        gates[L] += 1
        gates[R + 1] -= 1
    for i in range(1, N + 1):
        gates[i] += gates[i - 1]
    print(gates.count(M))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    # N 枚の ID カードのうち、i 番目の ID カードがどのゲートを通過できるかを格納する
    gate = [[] for _ in range(n)]
    for _ in range(m):
        l, r = map(int, input().split())
        gate[l-1].append(r-1)
    # 1 枚の ID カードで全てのゲートを通過できるかどうかを格納する
    can_pass = [False] * n
    # 1 枚の ID カードで全てのゲートを通過できる ID カードの枚数
    cnt = 0
    for i in range(n):
        # 1 枚の ID カードで全てのゲートを通過できる ID カードの枚数を更新
        if can_pass[i]:
            cnt += 1
        # i 番目の ID カードが通過できるゲートを更新
        for j in gate[i]:
            can_pass[j] = True
    print(cnt)
