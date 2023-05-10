Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a, b = [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.append(0)
    b.append(0)
    a.sort()
    ans = k
    for i in range(n+1):
        if ans < a[i]:
            break
        ans += b[i]
    print(ans)

main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    i = 0
    while K >= B[i]:
        K -= B[i]
        i += 1
        if i == N:
            break
    print(A[i - 1] + K + 1)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    for a, b in ab:
        if k < a:
            break
        k += b
    print(k)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    for i in range(N):
        if K < A[i]:
            print(K)
            exit()
        K = K + B[i]
    print(K)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    now = k
    for i in range(n):
        if now >= ab[i][0]:
            now += ab[i][1]
        else:
            print(now)
            exit()
    print(now)
main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = K
    for i in range(N):
        if ans < AB[i][0]:
            break
        ans += AB[i][1]
    print(ans)

=======
Suggestion 7

def solve():
    n,k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    # print(ab)
    money = k
    for i in range(n):
        if money >= ab[i][0]:
            money += ab[i][1]
        else:
            print(ab[i][0]-1)
            exit()
    print(money+ab[-1][0])

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    #print(AB)
    for i in range(N):
        if AB[i][0] > K:
            print(K)
            break
        else:
            K += AB[i][1]
    else:
        print(K)

=======
Suggestion 9

def solve():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    now = k
    for i in range(n):
        a,b = ab[i]
        if now < a:
            break
        now += b
    print(now)

=======
Suggestion 10

def main():
    n,k = map(int, input().split())
    friends = []
    for i in range(n):
        a,b = map(int, input().split())
        friends.append((a,b))
    friends.sort(key=lambda x:x[0])
    #print(friends)
    cnt = 0
    for friend in friends:
        if friend[0] - cnt <= k:
            k += friend[1]
            cnt = friend[0]
        else:
            break
    print(k+cnt)
