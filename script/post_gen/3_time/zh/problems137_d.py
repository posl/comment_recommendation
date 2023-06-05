Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[0])
    import heapq
    h = []
    i = 0
    ans = 0
    for d in range(1, M + 1):
        while i < N and jobs[i][0] == d:
            heapq.heappush(h, -jobs[i][1])
            i += 1
        if h:
            ans += -heapq.heappop(h)
    print(ans)

solve()

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    #print(AB)
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
        else:
            break
    print(ans)

solve()

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    c = [x for _,x in sorted(zip(a,b))]
    d = [x for _,x in sorted(zip(a,a))]
    a = d
    b = c
    sum = 0
    j = 0
    for i in range(m):
        if j < n and a[j] <= i+1:
            sum += b[j]
            j += 1
    print(sum)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m > jobs[i][0]:
            ans += jobs[i][1]
            m -= 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    ans = 0
    cnt = 0
    for a, b in ab:
        if cnt + a <= m:
            cnt += a
            ans += b
        else:
            ans += (m - cnt) * b
            break
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    data = [tuple(map(int, input().split())) for i in range(n)]
    data.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while m > 0:
        if i < n and data[i][0] <= m:
            ans += data[i][1]
            m -= data[i][0]
            i += 1
        else:
            break
    print(ans)

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ab.append([m+1, 0])
    ans = 0
    now = 0
    for i in range(n):
        if ab[i][0] != ab[i+1][0]:
            ans += ab[i][1]
        else:
            now += ab[i][1]
        if ab[i][0] != ab[i+1][0] or i == n-1:
            if now < ans:
                now = ans
    print(now)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while M > 0:
        if i >= N:
            break
        if AB[i][0] > M:
            break
        ans += AB[i][1]
        M -= AB[i][0]
        i += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, input().split())))

    jobs.sort(key=lambda x: x[0])

    max_reward = 0
    for job in jobs:
        if M > 0:
            max_reward += job[1]
            M -= 1
        else:
            break

    print(max_reward)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key = lambda x:x[0])
    total = 0
    i = 0
    while m > 0 and i < n:
        if jobs[i][0] <= m:
            total += jobs[i][1]
            m -= jobs[i][0]
        i += 1
    print(total)
