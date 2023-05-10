Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while m > 0:
        if m >= ab[i][0]:
            ans += ab[i][1]
            m -= ab[i][0]
            i += 1
        else:
            ans += m * ab[i][1]
            m = 0
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    #print(jobs)
    ans = 0
    j = 0
    for i in range(1, M+1):
        while j < N and jobs[j][0] <= i:
            j += 1
        if j > 0:
            ans += jobs[j-1][1]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    count = 0
    for i in range(N):
        if count + AB[i][0] <= M:
            ans += AB[i][0] * AB[i][1]
            count += AB[i][0]
        else:
            ans += (M - count) * AB[i][1]
            break
    print(ans)

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    ab = sorted(zip(a, b))
    ab.reverse()

    ab_i = 0
    ab_sum = 0
    m_sum = 0

    for m_i in range(m):
        while ab_i < n and ab[ab_i][0] <= m_i + 1:
            ab_sum += ab[ab_i][1]
            ab_i += 1
        m_sum += ab_sum

    return m_sum

print(solve())

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0])
    i = 0
    ans = 0
    for _ in range(M):
        while i < N and AB[i][0] <= _ + 1:
            heapq.heappush(h, -AB[i][1])
            i += 1
        if h:
            ans -= heapq.heappop(h)
    print(ans)
h = []
solve()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1
        else:
            break
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    days = []
    for i in range(n):
        a,b = map(int,input().split())
        days.append((a,b))
    days.sort()
    ans = 0
    for i in range(n):
        if m == 0:
            break
        if days[i][0] <= m:
            m -= days[i][0]
            ans += days[i][1]
        else:
            ans += m * days[i][1]
            m = 0
    print(ans)
main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    ans = 0
    for i in range(N):
        if M >= AB[i][0]:
            ans += AB[i][1]
            M -= 1

    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while M > 0:
        if AB[i][0] <= M:
            ans += AB[i][1]
            M -= AB[i][0]
        else:
            ans += M * AB[i][1]
            M = 0
        i += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort()
    ans = 0
    for i in range(N):
        A, B = jobs[i]
        if A > M:
            break
        ans += B
        M -= A
    print(ans)
