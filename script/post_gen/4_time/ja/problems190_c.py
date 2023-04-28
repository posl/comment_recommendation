Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        dish = [0] * (N+1)
        tmp = 0
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        for j in range(M):
            if dish[AB[j][0]] >= 1 and dish[AB[j][1]] >= 1:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        cnt = [0] * N
        for j in range(K):
            if (i>>j)&1:
                cnt[CD[j][0]-1] += 1
            else:
                cnt[CD[j][1]-1] += 1

        tmp = 0
        for j in range(M):
            if cnt[AB[j][0]-1] > 0 and cnt[AB[j][1]-1] > 0:
                tmp += 1

        ans = max(ans, tmp)

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        dish = [0]*N
        for j in range(K):
            if ((i >> j) & 1):
                dish[CD[j][1]-1] += 1
            else:
                dish[CD[j][0]-1] += 1
        tmp = 0
        for k in range(M):
            if dish[AB[k][0]-1] > 0 and dish[AB[k][1]-1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        dish = [0] * n
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0] - 1] += 1
            else:
                dish[cd[j][1] - 1] += 1
        cnt = 0
        for a, b in ab:
            if dish[a - 1] >= 1 and dish[b - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        dish = [0]*(N+1)
        for j in range(K):
            if (i>>j)&1:
                dish[CD[j][0]] += 1
            else:
                dish[CD[j][1]] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]] > 0 and dish[AB[j][1]] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        dish = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0] - 1] += 1
            else:
                dish[CD[j][1] - 1] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0] - 1] >= 1 and dish[AB[j][1] - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int, input().split())))
    K = int(input())
    CD = []
    for _ in range(K):
        CD.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**K):
        dish = [0]*N
        for j in range(K):
            if (i>>j)&1:
                dish[CD[j][0]-1] += 1
            else:
                dish[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if dish[AB[j][0]-1] > 0 and dish[AB[j][1]-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        A, B = map(int, input().split())
        edges.append((A, B))

    K = int(input())
    people = []
    for _ in range(K):
        C, D = map(int, input().split())
        people.append((C, D))

    ans = 0
    for i in range(2**K):
        balls = [0] * (N+1)
        for j in range(K):
            if (i>>j)&1:
                balls[people[j][0]] += 1
            else:
                balls[people[j][1]] += 1

        tmp = 0
        for A, B in edges:
            if balls[A] > 0 and balls[B] > 0:
                tmp += 1
        ans = max(ans, tmp)

    print(ans)

=======
Suggestion 9

def check(plate, condition):
    cnt = 0
    for i in range(len(condition)):
        if plate[condition[i][0]-1] == 1 and plate[condition[i][1]-1] == 1:
            cnt += 1
    return cnt

=======
Suggestion 10

def get_bit(n, i):
    return (n >> i) & 1
