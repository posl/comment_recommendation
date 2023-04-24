Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(sum([1 for d in D if d <= X]))

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([d for d in D if d <= X]))

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in range(N+1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    d = 0
    for i in range(N):
        d += L[i]
        if d <= X:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0
    cnt = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 0
    for i in range(n):
        d += l[i]
        if d <= x:
            ans += 1
    print(ans + 1)

main()

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    count = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1
        else:
            break
    print(count)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        if ans + L[i] > X:
            break
        ans += L[i]
    print(ans)
