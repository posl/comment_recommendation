Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    ans = min(R) - max(L) + 1
    if ans < 0:
        ans = 0
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    min_left = 0
    max_right = N + 1
    for i in range(M):
        left, right = map(int, input().split())
        min_left = max(min_left, left)
        max_right = min(max_right, right)
    print(max(max_right - min_left + 1, 0))

=======
Suggestion 4

def get_inputs():
    n, m = map(int, input().split())
    gates = []
    for i in range(m):
        gates.append(list(map(int, input().split())))
    return n, m, gates

=======
Suggestion 5

def main():
    n, m = map(int, input().split())

    # 1枚だけで全てのゲートを通過できるIDカードの枚数
    ans = 0

    # 1枚だけで全てのゲートを通過できるIDカードのリスト
    id_list = [False] * (n + 1)

    for _ in range(m):
        l, r = map(int, input().split())

        # l番目からr番目までのIDカードは1枚だけで全てのゲートを通過できる
        for i in range(l, r + 1):
            if not id_list[i]:
                ans += 1
                id_list[i] = True

    print(ans)

main()

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        l[a] += 1
        r[b] += 1
    ans = 0
    cnt = 0
    for i in range(1, n + 1):
        cnt += l[i]
        if cnt == m:
            ans += 1
        cnt -= r[i]
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[M-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[M-1] + 1)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    L.sort()
    R.sort()

    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)
