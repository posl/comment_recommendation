Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    for i in range(N + 1):
        if D[i] > X:
            print(i)
            return
    print(N + 1)

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    count = 0
    for i in range(n+1):
        if d[i] <= x:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([i for i in D if i <= X]))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    cnt = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 1
    for d in D:
        if d <= X:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    ans = 0
    for i in range(n+1):
        if d[i] <= x:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    cnt = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
        else:
            break
    print(cnt)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    l_list = list(map(int, input().split()))
    cnt = 1
    d = 0
    for l in l_list:
        d += l
        if d <= x:
            cnt += 1
        else:
            break
    print(cnt)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + L[i]
    ans = 0
    for i in range(N + 1):
        if D[i] <= X:
            ans += 1
    print(ans)
