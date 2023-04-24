Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[X-1] == X:
            ans = i + 1
            break
        X = A[X-1]
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X -= 1
    A = [a-1 for a in A]
    ans = 0
    visited = [0] * N
    while 1:
        if visited[X] == 1:
            ans = -1
            break
        ans += 1
        visited[X] = 1
        X = A[X]
        if visited[X] == 1:
            break
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X -= 1
    ans = 0
    visited = [False] * N
    visited[X] = True
    while not visited[A[X]-1]:
        X = A[X] - 1
        visited[X] = True
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    X -= 1
    count = 0
    while True:
        X = A[X]
        count += 1
        if X == 1:
            break
        if count == N:
            count = -1
            break
    print(count)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    i = X - 1
    ans = 0
    while True:
        ans += 1
        if A[i] == X:
            print(ans)
            break
        else:
            i = A[i] - 1

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    friends = [0]*N
    friends[X-1] = 1
    for i in range(N):
        if friends[A[X-1]] == 1:
            break
        friends[A[X-1]] = 1
        X = A[X-1]+1
    print(sum(friends))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    friend = [False] * (N + 1)
    count = 0
    while True:
        if friend[X] == True:
            break
        else:
            friend[X] = True
            count += 1
            X = A[X]
    print(count)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, X)
    #print(A)
    #print(A[X-1])
    #print(A[A[X-1]-1])
    #print(A[A[A[X-1]-1]-1])
    #print(A[A[A[A[X-1]-1]-1]-1])
    #print(A[A[A[A[A[X-1]-1]-1]-1]-1])
    #print(A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1])
    #print(A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1])
    #print(A[A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1]-1])
    #print(A[A[A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1]-1]-1])
    #print(A[A[A[A[A[A[A[A[A[A[X-1]-1]-1]-1]-1]-1]-1]-1]-1]-1])

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    count = 0
    check = [0 for i in range(n)]
    while True:
        if check[x] == 0:
            check[x] = 1
            count += 1
            x = a[x] - 1
        else:
            break
    print(count)

main()

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    # ある友達が知ったら、その友達はその友達にも知らせる
    # つまり、友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達の友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達の友達の友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達の友達の友達の友達の友達の友達はその友達にも知らせる
    # つまり、友達の友達の友達の友達の友達の友達の友達の友達の友達の友達はその友達にも知らせる
