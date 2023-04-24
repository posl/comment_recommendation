Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a.append(10**100)
    b.append(0)
    ans = k
    for i in range(n+1):
        if ans < a[i]:
            break
        ans += b[i]
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append((a, b))

    friends.sort(key=lambda x:x[0])
    for i in range(n):
        if k >= friends[i][0]:
            k += friends[i][1]
        else:
            break
    print(k)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if ab[i][0] > k:
            break
        k += ab[i][1]
    print(k)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k < ab[i][0]:
            break
        k += ab[i][1]
    print(k)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    friends = []
    for i in range(N):
        friends.append(list(map(int, input().split())))
    friends.sort()
    for i in range(N):
        if K < friends[i][0]:
            break
        K += friends[i][1]
    print(K)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    pos = 0
    for i in range(N):
        if K >= AB[i][0] - pos:
            K += AB[i][1] - (AB[i][0] - pos)
            pos = AB[i][0]
        else:
            pos += K
            K = 0
            break
    pos += K
    print(pos)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    ans = k
    for a,b in ab:
        if ans < a:
            break
        ans += b
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    cnt = 0
    for a, b in AB:
        cnt += b
        if cnt >= K:
            print(a)
            break

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k - ab[i][0] >= 0:
            k += ab[i][1]
    print(k)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()

    money = K
    i = 0
    while i < N:
        if AB[i][0] <= money:
            money += AB[i][1]
        else:
            break
        i += 1
    print(money)
