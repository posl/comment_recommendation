Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if X == A[X-1]:
            cnt += 1
            break
        X = A[X-1]
        cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X = X - 1
    count = 0
    visited = [False] * N
    while True:
        if visited[X]:
            print(-1)
            return
        if X == 1:
            print(count)
            return
        visited[X] = True
        count += 1
        X = A[X] - 1

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X = X - 1
    ans = 1
    visited = [False] * N
    visited[X] = True
    while True:
        X = A[X] - 1
        if visited[X] == True:
            ans = -1
            break
        ans += 1
        visited[X] = True
        if ans == N:
            break
    print(ans)

=======
Suggestion 4

def main():
    N, X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A = [a-1 for a in A]
    X -= 1

    ans = 0
    visited = [False]*N
    while not visited[X]:
        visited[X] = True
        X = A[X]
        ans += 1
    print(ans)

main()

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [x-1 for x in A]
    #print(A)
    #pri

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    visit = [0 for i in range(n+1)]
    visit[x] = 1
    count = 1
    while True:
        x = a[x]
        if visit[x] == 1:
            break
        else:
            visit[x] = 1
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    ans = 0
    b = [0]*n
    while b[x-1] == 0:
        b[x-1] = 1
        ans += 1
        x = a[x-1]+1
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    X = A[X]
    count = 1
    while A[X] != X:
        X = A[X]
        count += 1
    print(count)

=======
Suggestion 9

def main():
    #input
    N, X = map(int, input().split())
    As = list(map(int, input().split()))

    #compute
    dic = {}
    dic[X] = 1
    for i in range(N):
        X = As[X-1]
        if X in dic.keys():
            break
        dic[X] = 1

    #output
    print(len(dic))

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    X -= 1
    
    count = 0
    visited = [False]*N
    i = X
    while not visited[i]:
        visited[i] = True
        i = A[i]-1
        count += 1
    print(count)
