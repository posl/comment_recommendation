Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    for i in range(N):
        if K >= A[i]:
            K += B[i]
        else:
            print(K)
            return
    print(K)

=======
Suggestion 2

def problems203_c():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        A, B = map(int, input().split())
        friends.append([A, B])
    friends = sorted(friends, key=lambda x:x[0])
    for i in range(N):
        if friends[i][0] > K:
            break
        else:
            K += friends[i][1]
    print(K)
problems203_c()

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for a, b in ab:
        if k < a:
            break
        k += b
    print(k)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    for a, b in ab:
        if a > k:
            break
        k += b
    print(k)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    v = [0] * (10 ** 5 + 1)
    for i in range(n):
        a, b = map(int, input().split())
        v[a] += b
    for i in range(10 ** 5):
        if k <= v[i]:
            print(i)
            return
        k -= v[i]
        v[i + 1] += v[i]

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()

    money = K
    village = 0
    for i in range(N):
        if village < AB[i][0] and money >= AB[i][0] - village:
            money -= AB[i][0] - village
            money += AB[i][1]
            village = AB[i][0]

    village += money
    print(village)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k >= ab[i][0]:
            k += ab[i][1]
        else:
            break
    print(k)
    return

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    ab = []
    for i in range(n):
        a,b = map(int, input().split())
        ab.append((a,b))
    ab.sort()
    #print(ab)
    i = 0
    while k > 0:
        if i >= n:
            break
        if ab[i][0] <= k:
            k += ab[i][1]
        i += 1
    print(k)

=======
Suggestion 9

def main():
    # input
    N, K = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]

    # compute
    ab.sort()
    for a, b in ab:
        if a > K:
            break
        K += b

    # output
    print(K)

=======
Suggestion 10

def main():
    N, K = [int(v) for v in input().split()]
    AB = [[int(v) for v in input().split()] for _ in range(N)]
    AB.sort(key=lambda ab: ab[0])
    for ab in AB:
        if K < ab[0]:
            break
        K += ab[1]
    print(K)
