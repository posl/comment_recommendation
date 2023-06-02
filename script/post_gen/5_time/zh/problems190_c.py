Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2**K):
        dish = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                dish[CD[j][0]-1] += 1
            else:
                dish[CD[j][1]-1] += 1
        cnt = 0
        for a, b in AB:
            if dish[a-1] > 0 and dish[b-1] > 0:
                cnt += 1
        ans = max(ans, cnt)

    print(ans)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def solve():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    K = int(input())
    CD = [list(map(int,input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        balls = [0]*N
        for j in range(K):
            if((i>>j)&1):
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for j in range(M):
            if balls[AB[j][0]-1] and balls[AB[j][1]-1]:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 4

def count_satisfied_conditions(N, M, conditions, K, persons):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            satisfied = True
            for k in range(M):
                if i < conditions[k][0] or conditions[k][1] < j:
                    satisfied = False
            for k in range(K):
                if i != persons[k][0] and j != persons[k][1]:
                    satisfied = False
            if satisfied:
                count += 1
    return count

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        cnt = 0
        balls = [0] * (N + 1)
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]] += 1
            else:
                balls[CD[j][1]] += 1
        for a, b in AB:
            if balls[a] and balls[b]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for _ in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    K = int(input())
    C = []
    D = []
    for _ in range(K):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)
    ans = 0
    for i in range(1<<K):
        dish = [False]*N
        for j in range(K):
            if i & 1<<j:
                dish[C[j]-1] = True
            else:
                dish[D[j]-1] = True
        cnt = 0
        for j in range(M):
            if dish[A[j]-1] and dish[B[j]-1]:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

=======
Suggestion 7

def dfs(i, balls):
    if i == K:
        return sum([1 if all([balls[a-1] and balls[b-1] for a, b in AB]) else 0 for AB in ABs])
    else:
        balls[C[i]-1] += 1
        res = dfs(i+1, balls)
        balls[C[i]-1] -= 1
        balls[D[i]-1] += 1
        res = max(res, dfs(i+1, balls))
        balls[D[i]-1] -= 1
        return res

N, M = map(int, input().split())
ABs = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C, D = [], []
for _ in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

print(dfs(0, [0]*N))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int,input().split())) for _ in range(k)]
    ans = 0
    for i in range(2**k):
        dish = [0] * (n+1)
        for j in range(k):
            if (i >> j) & 1:
                dish[cd[j][0]] += 1
            else:
                dish[cd[j][1]] += 1
        sum = 0
        for l in range(m):
            if dish[ab[l][0]] >= 1 and dish[ab[l][1]] >= 1:
                sum += 1
        ans = max(ans,sum)
    print(ans)

=======
Suggestion 9

def get_max_satisfied_conditions(N, M, conditions, K, people):
    max_satisfied = 0
    for i in range(2**K):
        satisfied_conditions = 0
        plates = [0]*N
        for j in range(K):
            if (i & (1<<j)) > 0:
                plates[people[j][0]-1] = 1
            else:
                plates[people[j][1]-1] = 1
        for j in range(M):
            if plates[conditions[j][0]-1] == 1 and plates[conditions[j][1]-1] == 1:
                satisfied_conditions += 1
        if max_satisfied < satisfied_conditions:
            max_satisfied = satisfied_conditions
    return max_satisfied
