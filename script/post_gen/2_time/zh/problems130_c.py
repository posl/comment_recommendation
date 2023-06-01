Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    for i in range(n+1):
        if d[i]>x:
            print(i)
            break

=======
Suggestion 2

def main():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    for i in range(N+1):
        if D[i] > X:
            print(i)
            break
        elif D[i] == X:
            print(i+1)
            break
        elif i == N:
            print(i+1)

main()

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
        if D[i] > X:
            print(i)
            break
    else:
        print(N + 1)

=======
Suggestion 4

def main():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    D = [0]
    for i in range(N):
        D.append(D[-1]+L[i])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    print(sum([1 for i in d if i<=x]))

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    print(len(list(filter(lambda y: y <= x, d))))

=======
Suggestion 8

def problem130_b():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    print(len([i for i in D if i<=X]))

=======
Suggestion 9

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

main()

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    for i in range(n+1):
        if i == 0:
            d = 0
        else:
            d = d + l[i-1]
        if d > x:
            print(i)
            break
        elif d == x:
            print(i+1)
            break
        elif i == n:
            print(i+1)
            break
