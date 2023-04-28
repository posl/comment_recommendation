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
                print(j + 1)
                break
        else:
            print(-1)

main()

=======
Suggestion 2

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
Suggestion 3

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

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
                if count == k:
                    print(j+1)
                    break
        else:
            print(-1)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for i, a in enumerate(A):
            if a == x:
                cnt += 1
            if cnt == k:
                print(i + 1)
                break
        else:
            print(-1)

=======
Suggestion 6

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
                    print(j + 1)
                    break
        else:
            print(-1)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(Q):
        X, K = map(int, input().split())
        ans = 0
        count = 0
        for j in range(N):
            if A[j] == X:
                count += 1
                if count == K:
                    ans = j + 1
                    break
        if ans == 0:
            ans = -1

        print(ans)

=======
Suggestion 8

def calc(x,k,a):
    cnt = 0
    for i in range(len(a)):
        if a[i] == x:
            cnt += 1
            if cnt == k:
                return i+1
    return -1
