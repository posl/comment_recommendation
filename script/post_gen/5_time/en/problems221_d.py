Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [2, 3, 1]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 2
    #A = [1000000000, 1000000000]
    #B = [1000000000, 1000000000]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [1, 2, 3]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [1, 1, 1]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [3, 3, 3]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [1, 2, 2]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [2, 2, 2]

    #print(N)
    #print(A)
    #print(B)

    #print('---')

    #N = 3
    #A = [1, 2, 3]
    #B = [2, 3, 3]

    #print(N)
    #print(A)
    #print(B

=======
Suggestion 2

def solve():
    from collections import defaultdict
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        d[a] += 1
        d[a+b] -= 1
    d = sorted(d.items())
    ans = [0] * (N+1)
    for i in range(1, len(d)):
        ans[d[i-1][1]] += d[i][0] - d[i-1][0]
    print(*ans[1:])

=======
Suggestion 3

def main():
    n = int(input())
    d = [0]*(10**9+2)
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] += 1
        d[a+b] -= 1
    for i in range(1, 10**9+2):
        d[i] += d[i-1]
    print(*d[1:-1])

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if n % 2 == 0:
        ans = b[n // 2] + b[n // 2 - 1] - a[n // 2] - a[n // 2 - 1] + 1
    else:
        ans = b[n // 2] - a[n // 2] + 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)

=======
Suggestion 6

def solve():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    m = max(a) + max(b)
    c = [0] * m
    for i in range(n):
        c[a[i]-1] += 1
        c[a[i]+b[i]-1] -= 1
    for i in range(1, m):
        c[i] += c[i-1]
    print(*c[:n])
solve()

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    B = list(map(lambda x: x-1, B))
    max_day = max(A) + max(B)
    day_count = [0] * (max_day + 1)
    for i in range(N):
        day_count[A[i]] += 1
        day_count[A[i]+B[i]+1] -= 1
    for i in range(max_day):
        day_count[i+1] += day_count[i]
    print(*day_count[:-1])

main()

=======
Suggestion 8

def main():
    N = int(input())
    #print(N)
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    d = {}
    for i in range(N):
        for j in range(A[i], A[i]+B[i]):
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    #print(d)
    for i in range(1, N+1):
        if i in d:
            print(d[i], end=" ")
        else:
            print(0, end=" ")
main()

=======
Suggestion 9

def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append((10**9+1, 0))

    ans = [0]*(N+1)
    day = 0
    for i in range(N):
        if day < AB[i][0]:
            day = AB[i][0]
        ans[AB[i][1]] += AB[i][0]-day+1
        ans[AB[i+1][1]] -= AB[i][0]-day+1
        day += AB[i][1]
    print(*ans[:-1])

=======
Suggestion 10

def main():
    """ main function
    """
    import sys
    from collections import defaultdict
    from itertools import accumulate
    input = sys.stdin.readline
    n = int(input().rstrip())
    a_b = [list(map(int, input().rstrip().split())) for _ in range(n)]
    a_b.sort()
    a = [x[0] for x in a_b]
    b = [x[1] for x in a_b]
    d = defaultdict(int)
    for i in range(n):
        d[a[i]] += 1
        d[a[i]+b[i]] -= 1
    d = sorted(d.items(), key=lambda x:x[0])
    d = list(accumulate([x[1] for x in d]))
    print(*d)
