Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[-1] + L[i])
    print(sum(1 for i in D if i <= X))

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(sum([1 for d in D if d <= X]))

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([d for d in D if d <= X]))

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(sum([1 for i in D if i <= X]))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    d = 0
    for i in range(N):
        d += L[i]
        if d <= X:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        d = d + l[i]
        if d <= x:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 0
    for i in range(n):
        d = d + l[i]
        if d <= x:
            count = count + 1
        else:
            break
    if d <= x:
        count = count + 1
    print(count)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if x >= sum(l[:i+1]):
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    # put your code here
    N, X = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    D = [0]
    for i in range(N):
        D.append(D[i]+L[i])
    print(sum(1 for i in D if i <= X))

=======
Suggestion 10

def main():
    # Write your code here
    pass
