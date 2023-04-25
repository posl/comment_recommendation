Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    visited = [False] * (N + 1)
    visited[X] = True
    count = 0
    while True:
        X = A[X]
        if visited[X] == True:
            break
        else:
            visited[X] = True
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    visited = [False] * (N + 1)
    count = 0
    while not visited[X]:
        visited[X] = True
        X = A[X]
        count += 1
    print(count)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]
    visited = [False]*N
    visited[X-1] = True
    count = 1
    current = X-1
    while True:
        current = A[current]
        if visited[current]:
            print(-1)
            break
        else:
            visited[current] = True
            count += 1
            if current == 0:
                print(count)
                break

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    X -= 1
    ans = 0
    visited = [False] * N
    while True:
        if visited[X]:
            ans = -1
            break
        ans += 1
        visited[X] = True
        X = A[X]
        if visited[X]:
            break
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    count = 0
    for i in range(N):
        if X == A[X]:
            print(count)
            break
        else:
            X = A[X]
            count += 1
    else:
        print(-1)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    count = 0
    used = [False] * n
    while not used[x]:
        used[x] = True
        x = a[x] - 1
        count += 1
    print(count)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    X = A[X]
    count = 0
    while X != 1:
        X = A[X]
        count += 1
        if count > 100:
            break
    if count > 100:
        print(-1)
    else:
        print(count+1)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    X -= 1
    B = [0]*N
    B[X] = 1
    while True:
        X = A[X]
        if B[X]:
            print(-1)
            return
        B[X] = 1
        if X == 1:
            break
    print(sum(B))

main()

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, X)
    #print(A)
    l = [0] * N
    l[X-1] = 1
    #print(l)
    i = X-1
    while 1:
        #print(i, A[i])
        i = A[i] - 1
        l[i] += 1
        if l[i] == 2:
            break
    print(sum(l))

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, x, a)
    s = set()
    s.add(x-1)
    i = x-1
    while True:
        i = a[i]-1
        if i in s:
            break
        else:
            s.add(i)
    print(len(s))
