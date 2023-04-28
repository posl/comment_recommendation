Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[0])

    ans = 0
    i = 0
    while M > 0 and i < N:
        a, b = jobs[i]
        if M < a:
            ans += M * b
            M = 0
        else:
            ans += a * b
            M -= a
        i += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()

    from heapq import heappop, heappush
    q = []
    ans = 0
    j = 0
    for i in range(1, M + 1):
        while j < N and jobs[j][0] <= i:
            heappush(q, -jobs[j][1])
            j += 1
        if q:
            ans -= heappop(q)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if M <= AB[i][0]:
            ans += AB[i][1]
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][0]
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    work = []
    for _ in range(N):
        A, B = map(int, input().split())
        work.append((A, B))
    work.sort()
    ans = 0
    for i in range(N):
        if work[i][0] > M:
            break
        ans += work[i][1]
        M -= work[i][0]
    print(ans)

main()

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    from heapq import heappush, heappop
    h = []
    j = 0
    for i in range(1, M+1):
        while j < N and AB[j][0] <= i:
            heappush(h, -AB[j][1])
            j += 1
        if len(h) > 0:
            ans += -heappop(h)
    print(ans)

solve()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    ab = []
    for i in range(N):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x:x[0])
    ans = 0
    for i in range(N):
        if ab[i][0] <= M:
            ans += ab[i][1]
            M -= ab[i][0]
        else:
            ans += M * ab[i][1]
            break
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    i = 0
    from heapq import heappop, heappush
    h = []
    for day in range(M):
        while i < N and AB[i][0] == day + 1:
            heappush(h, -AB[i][1])
            i += 1
        if h:
            ans -= heappop(h)
    print(ans)

=======
Suggestion 8

def calc():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    #print(jobs)
    ans = 0
    i = 0
    while m > 0:
        if i >= n:
            break
        if jobs[i][0] > m:
            break
        ans += jobs[i][1]
        m -= jobs[i][0]
        i += 1
    print(ans)

calc()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    work.sort(key=lambda x: x[0])
    now = 0
    ans = 0
    for i in range(N):
        if work[i][0] - now <= M:
            ans += work[i][1]
            now = work[i][0]
        else:
            ans += M * work[i][1]
            break
        if now == M:
            break
    print(ans)

=======
Suggestion 10

def solve(n, m, a, b):
    work = []
    for i in range(n):
        work.append([a[i], b[i]])
    work.sort()
    ans = 0
    for i in range(n):
        if m > work[i][0]:
            m += work[i][1]
            ans += work[i][1]
        else:
            break
    print(ans)

n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
solve(n, m, a, b)
