Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    cake = [list(map(int, input().split())) for i in range(n)]

    ans = 0
    for i in range(2 ** 3):
        tmp = 0
        for j in range(n):
            tmp += max([cake[j][k] * (-1) ** ((i >> k) & 1) for k in range(3)])
        ans = max(ans, tmp)

    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] if i >> k & 1 else -cake[j][k] for k in range(3)]))
        tmp.sort()
        ans = max(ans, sum(tmp[-M:]))
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(2**3):
        tmp = 0
        for j in range(n):
            sum = 0
            for k in range(3):
                if i >> k & 1:
                    sum += cake[j][k]
                else:
                    sum -= cake[j][k]
            tmp += abs(sum)
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] if i >> k & 1 else -cake[j][k] for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        tmp = [0] * N
        for j in range(N):
            if i & 1:
                tmp[j] += cake[j][0]
            else:
                tmp[j] -= cake[j][0]
            if i & 2:
                tmp[j] += cake[j][1]
            else:
                tmp[j] -= cake[j][1]
            if i & 4:
                tmp[j] += cake[j][2]
            else:
                tmp[j] -= cake[j][2]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: -x[i % 3] if i // 3 == 0 else x[i % 3])
        ans = max(ans, sum([sum(cake[j]) for j in range(M)]))
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(N)]
    ans = -float('inf')
    for i in range(2 ** 3):
        tmp = []
        for j in range(N):
            tmp.append(sum([cake[j][k] * ((i >> k) & 1) * 2 - 1 for k in range(3)]))
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: -x[i % 3] if i >= 3 else x[i % 3])
        ans = max(ans, sum([sum(cake[i][:3]) for i in range(M)]))
    print(ans)
