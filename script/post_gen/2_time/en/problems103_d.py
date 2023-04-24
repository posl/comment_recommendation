Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    ans = 0
    for i in range(M):
        a = A[i]
        b = B[i]
        for j in range(i+1, M):
            c = A[j]
            d = B[j]
            if (a < c < b < d) or (c < a < d < b):
                ans += 1
                break
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    bridges = [set() for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        bridges[a].add(b)
        bridges[b].add(a)
    ans = 0
    for i in range(1, N + 1):
        if bridges[i]:
            ans += 1
            for j in bridges[i]:
                bridges[j].discard(i)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    bridges = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        bridges[a-1] += 1
        bridges[b-1] += 1
    print(bridges.count(1))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append([a, b])
    bridges.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for bridge in bridges:
        if last < bridge[0]:
            last = bridge[1] - 1
            ans += 1
    print(M - ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    prev = 0
    for i in range(M):
        if prev < bridges[i][0]:
            ans += 1
            prev = bridges[i][1]
    print(ans)

main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for a, b in bridges:
        if bridge < a:
            ans += 1
            bridge = b-1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    bridge = [0] * (N-1)
    for _ in range(M):
        a, b = map(int, input().split())
        bridge[min(a, b)-1] += 1
    print(bridge.count(0))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    L = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        L[i] = [a, b]
    L.sort()
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if L[i][1] <= L[j][0]:
                ans += 1
                break
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for a, b in AB:
        if a <= last:
            continue
        else:
            last = b - 1
            ans += 1
    print(ans)
    return

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])

    cnt = 0
    last = 0
    for a, b in bridges:
        if last < a:
            cnt += 1
            last = b - 1

    print(M - cnt)
