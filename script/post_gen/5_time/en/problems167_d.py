Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    town = 1
    for i in range(K):
        town = A[town-1]
    print(town)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    town = 1
    for i in range(k):
        town = a[town-1]
    print(town)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    now = 1
    for i in range(K):
        now = A[now - 1]
    print(now)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    now = 0
    for i in range(61):
        if (K >> i) & 1:
            now = A[now]
        A = [A[A[j]] for j in range(N)]
    print(now + 1)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    while True:
        ans = A[ans] - 1
        cnt += 1
        if cnt == K:
            print(ans + 1)
            break
        if ans == 0:
            print(ans + 1)
            break

=======
Suggestion 6

def teleporter():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    town = 1
    count = 0
    while count < K:
        town = A[town-1]
        count += 1
    print(town)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    current = 1
    for i in range(K):
        current = A[current - 1]
    print(current)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    route = [1]
    next = A[0]
    while not next in route:
        route.append(next)
        next = A[next-1]
    cycle_start = route.index(next)
    cycle = route[cycle_start:]
    if K < cycle_start:
        print(route[K])
    else:
        print(cycle[(K-cycle_start)%len(cycle)])

=======
Suggestion 9

def teleporter(a, k):
    n = len(a)
    b = [None] * n
    b[0] = 0
    for i in range(1, n):
        b[i] = a[b[i - 1] - 1]
        if b[i] == 0:
            return a[k % i]
    return b[-1]

=======
Suggestion 10

def findPath(towns, start, k):
    if k == 0:
        return start
    else:
        return findPath(towns, towns[start-1], k-1)
