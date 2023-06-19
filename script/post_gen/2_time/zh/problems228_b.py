Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    T = [0 for i in range(N)]
    T[X-1] = 1
    for i in range(N):
        if T[A[i]-1] == 1:
            T[i] = 1
    print(sum(T))

=======
Suggestion 2

def get_friends_secret(N,X,A):
    # 朋友列表
    friend_list = [0] * N
    # 朋友是否知道秘密
    friend_list[X-1] = 1
    # 朋友是否已经分享秘密
    friend_list_shared = [0] * N
    # 朋友已经知道秘密的个数
    friend_secret_num = 1
    while friend_secret_num < N:
        for i in range(N):
            if friend_list[i] == 1 and friend_list_shared[i] == 0:
                friend_list_shared[i] = 1
                if friend_list[A[i]-1] == 0:
                    friend_list[A[i]-1] = 1
                    friend_secret_num += 1
    return friend_secret_num

=======
Suggestion 3

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.insert(0,0)
    B = [0]*(N+1)
    B[X] = 1
    for i in range(1,N+1):
        if B[i] == 1:
            B[A[i]] = 1
    print(sum(B))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    flag = [False] * n
    flag[x - 1] = True
    count = 1
    while True:
        for i in range(n):
            if flag[i]:
                continue
            if a[i] == x - 1:
                flag[i] = True
                count += 1
        if False not in flag:
            break
        x = a[x - 1] + 1
    print(count)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] <= x:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    c = 1
    for i in range(n):
        if a[i] == 0:
            continue
        else:
            c += 1
            a[a[i]-1] = 0
    print(c)

=======
Suggestion 7

def solve():
    #import sys
    #f = open('test.txt', 'r')
    #sys.stdin = f
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    ans = 1
    i = x
    while a[i] != x + 1:
        ans += 1
        i = a[i] - 1
    print(ans)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = -1
    b = [0]*n
    for i in range(n):
        if a[i] != -1:
            b[a[i]-1] += 1
    for i in range(n):
        if b[i] != 0:
            b[i] = 1
    print(sum(b))

=======
Suggestion 9

def solution():
    N,X = map(int, input().split())
    A = list(map(int, input().split()))
    A[X-1] = 0
    ans = 1
    for i in range(N):
        if A[i] != 0:
            ans += 1
            A[A[i]-1] = 0
    print(ans)

solution()

=======
Suggestion 10

def getSecret(N, X, A):
    A = [A[i] - 1 for i in range(N)]
    friends = [False] * N
    friends[X - 1] = True
    for i in range(N):
        if friends[A[i]]:
            friends[i] = True
    return sum(friends)
