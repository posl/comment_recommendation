Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    job = []
    for i in range(n):
        job.append(tuple(map(int, input().split())))

    job.sort(key=lambda x: x[0])

    ans = 0
    for i in range(n):
        if job[i][0] <= m:
            ans += job[i][1]
            m -= job[i][0]
        else:
            ans += job[i][1] * m
            m = 0
            break

    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    ab_list = []
    for i in range(n):
        ab_list.append(list(map(int, input().split())))
    ab_list.sort(key = lambda x : x[0])
    #print(ab_list)
    ans = 0
    for i in range(n):
        if ab_list[i][0] > m:
            break
        else:
            ans += ab_list[i][1]
            m -= ab_list[i][0]
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    a = [x[0] for x in ab]
    b = [x[1] for x in ab]
    import bisect
    ans = 0
    for i in range(n):
        if a[i] > m:
            break
        ans += b[i]
        m -= a[i]
    print(ans)

=======
Suggestion 4

def main():
    N,M = map(int, input().split())
    jobs = []
    for i in range(N):
        a,b = map(int, input().split())
        jobs.append((a,b))
    jobs.sort(key=lambda x:x[0])
    #print(jobs)
    ans = 0
    for i in range(N):
        if jobs[i][0] <= M:
            ans += jobs[i][1]
            M -= jobs[i][0]
        else:
            ans += jobs[i][1] * M
            break
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m > ab[i][0]:
            m -= ab[i][0]
            ans += ab[i][1]
        else:
            ans += ab[i][1] * m
            break
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort()
    sum = 0
    for i in range(len(ab)):
        if ab[i][0] <= m:
            sum += ab[i][1]
            m -= ab[i][0]
        else:
            sum += ab[i][1] * m
            break
    print(sum)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[0])
    ans = 0
    for i in range(n):
        if m == 0:
            break
        if m >= ab[i][0]:
            m -= ab[i][0]
            ans += ab[i][1]
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    works = []
    for i in range(n):
        a, b = map(int, input().split())
        works.append([a, b])
    works.sort(key=lambda x: x[0])
    sum = 0
    day = 0
    index = 0
    while day < m:
        if index < n and works[index][0] == day + 1:
            sum += works[index][1]
            index += 1
        day += 1
    print(sum)

=======
Suggestion 9

def main():
    n,m = map(int,raw_input().split())
    work = []
    for i in range(n):
        work.append(map(int,raw_input().split()))

    work.sort(key=lambda x:x[0])
    #print work
    ans = 0
    for i in range(n):
        if m >= work[i][0]:
            m -= work[i][0]
            ans += work[i][1]

    print ans

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a1 = []
    b1 = []
    for i in range(n):
        if a[i] <= m:
            a1.append(a[i])
            b1.append(b[i])
    if len(a1) == 0:
        print(0)
    else:
        print(max(b1))
