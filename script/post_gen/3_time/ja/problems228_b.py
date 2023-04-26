Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    friend = [0] * N
    friend[X-1] = 1
    for i in range(N):
        if friend[A[i]-1] == 1:
            friend[A[i]-1] = 1
            friend[i] = 1
    print(sum(friend))

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 1
    for i in range(N):
        if X == A[X - 1]:
            break
        X = A[X - 1]
        count += 1
    print(count)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 0
    while X != 1:
        X = A[X]
        count += 1
    print(count)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    visited = [0] * N
    visited[X-1] = 1
    #print(A)
    #print(visited)
    for i in range(N):
        if visited[A[X-1]] == 1:
            break
        visited[A[X-1]] = 1
        X = A[X-1]+1
    print(sum(visited))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    s = []
    while True:
        s.append(X)
        X = A[X-1]
        if X in s:
            print(len(s))
            break

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(N):
        if X == 1:
            ans = i+1
            break
        else:
            X = A[X]
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    X = A[X]
    ans = 0
    while X != 1:
        X = A[X]
        ans += 1
    print(ans+1)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    #print(A)
    #print(X)
    #print(N)
    #print(A[X])
    #print(A)
    #print(N)
    friend = []
    friend.append(X)
    #print(friend)
    i = 0
    while True:
        if friend[i] == A[friend[i]]:
            break
        else:
            friend.append(A[friend[i]])
            #print(friend)
            i += 1
    print(len(friend))

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    #友達の秘密を知った回数
    friend_secret = [0] * N
    #友達の秘密を知った回数が1以上の場合は、友達の秘密を知った回数を出力
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、
    #その友達の秘密を知った回数を出力
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、
    #その友達の秘密を知った回数を出力
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、
    #その友達の秘密を知った回数を出力
    #...
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、
    #その友達の秘密を知った回数を出力
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、
    #その友達の秘密を知った回数を出力
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、
    #その友達の秘密を知った回数を出力
    #友達の秘密を知った回数が0の場合は、友達の秘密を知った回数を1にして、

=======
Suggestion 10

def main():
    N,X=map(int,input().split())
    A=list(map(int,input().split()))
    A=[a-1 for a in A]
    #print(N,X,A)
    ans=0
    f=[0 for _ in range(N)]
    while f[X-1]==0:
        f[X-1]=1
        X=A[X-1]
        ans+=1
    print(ans)
