Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    S = [0] * N
    T = [0] * N
    P = [0] * N
    for i in range(N):
        S[i], T[i], P[i] = map(int, input().split())
    M = max(T)
    A = [0] * (M + 1)
    for i in range(N):
        A[S[i]] += P[i]
        A[T[i]] -= P[i]
    for i in range(M):
        A[i + 1] += A[i]
        if A[i] > W:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 2

def main():
    n, w = map(int, input().split())
    a = [0]*(2*10**5+1)
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(2*10**5):
        a[i+1] += a[i]
        if a[i] > w:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    water = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        S, T, P = map(int, input().split())
        water[S] += P
        water[T] -= P
    for i in range(2 * 10 ** 5):
        water[i + 1] += water[i]
        if water[i] > W:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def main():
    n, w = map(int, input().split())
    s = [0] * (2 * 10 ** 5 + 1)
    for _ in range(n):
        l, r, p = map(int, input().split())
        s[l] += p
        s[r] -= p
    for i in range(1, 2 * 10 ** 5 + 1):
        s[i] += s[i - 1]
        if s[i] > w:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    s = [0] * (200001)
    for i in range(N):
        S, T, P = map(int, input().split())
        s[S] += P
        s[T] -= P
    for i in range(1, 200001):
        s[i] += s[i-1]
        if s[i] > W:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    plan = [tuple(map(int, input().split())) for _ in range(N)]
    event = []
    for s, t, p in plan:
        event.append((s, p))
        event.append((t, -p))
    event.sort()
    current = 0
    for _, p in event:
        current += p
        if current > W:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    T = 2 * 10 ** 5 + 1
    A = [0 for _ in range(T)]
    for _ in range(N):
        S, T, P = map(int, input().split())
        A[S] += P
        A[T] -= P

    for i in range(T):
        A[i + 1] += A[i]

    for i in range(T):
        if A[i] > W:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    d = [0] * 200001
    for s, t, p in data:
        d[s] += p
        d[t] -= p
    for i in range(1, 200001):
        d[i] += d[i-1]
    if max(d) <= W:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    #print(n,w)
    req = [0] * 200005
    for i in range(n):
        s, t, p = map(int, input().split())
        req[s] += p
        req[t] -= p
    #print(req)
    for i in range(1, 200005):
        req[i] += req[i-1]
        if req[i] > w:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 10

def main():
    n, w = map(int, input().split())
    plans = [list(map(int, input().split())) for _ in range(n)]
    #print(n, w)
    #print(plans)

    # 0~200000
    # 1~200000
    # 2~200000
    # 3~200000
    # 4~200000
    # 5~200000
    # 6~200000
    # 7~200000
    # 8~200000
    # 9~200000
    # 10~200000
    # 11~200000
    # 12~200000
    # 13~200000
    # 14~200000
    # 15~200000
    # 16~200000
    # 17~200000
    # 18~200000
    # 19~200000
    # 20~200000
    # 21~200000
    # 22~200000
    # 23~200000
    # 24~200000
    # 25~200000
    # 26~200000
    # 27~200000
    # 28~200000
    # 29~200000
    # 30~200000
    # 31~200000
    # 32~200000
    # 33~200000
    # 34~200000
    # 35~200000
    # 36~200000
    # 37~200000
    # 38~200000
    # 39~200000
    # 40~200000
    # 41~200000
    # 42~200000
    # 43~200000
    # 44~200000
    # 45~200000
    # 46~200000
    # 47~200000
    # 48~200000
    # 49~200000
    # 50~200000
    # 51~200000
    # 52~200000
    # 53~200000
    # 54~200000
    # 55~200000
    # 56~200000
