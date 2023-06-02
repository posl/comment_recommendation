Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    print(len([i for i in d if i <= x]))

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    count = 1
    for i in l:
        d += i
        if d <= x:
            count += 1
    print(count)

=======
Suggestion 3

def problem130_b():
    n, x = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (n + 1)
    for i in range(1, n + 1):
        D[i] = D[i - 1] + L[i - 1]
        if D[i] > x:
            print(i)
            break
    else:
        print(n + 1)

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    count = 0
    for i in range(n+1):
        if d[i] <= x:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    d=0
    count=1
    for i in range(n):
        d+=l[i]
        if d<=x:
            count+=1
    print(count)

=======
Suggestion 6

def problems130_b():
    n,x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    cnt = 0
    for i in range(n+1):
        if d[i] <= x:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    cnt = 0
    for i in d:
        if i <= x:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def get_input():
    return map(int, input().split())

=======
Suggestion 9

def bouncing_ball(N, X, L):
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
        if D[i] > X:
            return i - 1
    return N
