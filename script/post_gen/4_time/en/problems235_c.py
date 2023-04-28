Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        count = 0
        for i in range(n):
            if a[i] == x:
                count += 1
            if count == k:
                print(i+1)
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(n):
            if a[i] == x:
                cnt += 1
            if cnt == k:
                print(i+1)
                break
        else:
            print(-1)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(len(A)):
            if A[j] == x:
                count += 1
            if count == k:
                print(j + 1)
                break
        else:
            print(-1)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)
    return

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(N):
            if A[j] == x:
                cnt += 1
                if cnt == k:
                    print(j+1)
                    break
        else:
            print(-1)

main()

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(N):
            if A[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        if cnt < k:
            print(-1)

=======
Suggestion 8

def main():
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(q):
        x,k=map(int,input().split())
        tmp=0
        for j in range(n):
            if a[j]==x:
                tmp+=1
                if tmp==k:
                    print(j+1)
                    break
        else:
            print(-1)
