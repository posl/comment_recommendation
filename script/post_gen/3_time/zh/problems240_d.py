Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in range(n):
        print(n - sum([d[j] for j in d if j < a[i]]))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = []
    for i in range(n):
        while len(s) > 0 and s[-1] == a[i]:
            s.pop()
        s.append(a[i])
        print(len(s))

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    c = [0] * (n + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = n
    for i in range(1, n + 1):
        if c[i] >= 2:
            ans -= c[i]
    for i in range(n):
        print(ans)
        x = a[i]
        c[x] -= 1
        if c[x] >= 2:
            ans -= 1

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i])
        while len(b) > 1:
            if b[-1] == b[-2]:
                b.pop()
                b.pop()
            else:
                break
        print(len(b))

=======
Suggestion 5

def main():
    N = input()
    A = raw_input().split()
    A = map(int, A)
    B = []
    for i in range(N):
        B.append(i)
    C = []
    for i in range(N):
        C.append(0)
    for i in range(N):
        C[A[i]-1] += 1
    for i in range(N):
        print N - sum(C[:A[i]-1]) - 1

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    #print(n,a)
    b = [0]*n
    for i in range(n-1):
        b[i] = a[i]
        if b[i] == 2:
            b[i] = 0
        elif b[i] % 2 == 0:
            b[i] -= 1
    #print(b)
    for i in range(n-1):
        if b[i] == 0:
            b[i+1] = 0
    #print(b)
    for i in range(n):
        print(n-sum(b[:i+1]))

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] == 2:
            count += 1
        else:
            count -= 1
        print(N - count)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    c = [0] * (2 * 10**5 + 1)

    for i in range(n):
        c[a[i]] += 1

    for i in range(1, 2 * 10**5 + 1):
        c[i] += c[i - 1]

    for i in range(n):
        b[c[a[i]] - 1] = i + 1
        c[a[i]] -= 1

    for i in range(n):
        print(b[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    ans = 0
    for i in range(n):
        if d[a[i]] > 0:
            ans += 1
            d[a[i]] -= 1
            if a[i] - 1 in d:
                d[a[i] - 1] += 1
            else:
                d[a[i] - 1] = 1

    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(n):
        b.append(a[i])
        if i == 0:
            c.append(1)
        else:
            c.append(c[i - 1] + 1)
        while len(b) >= 2 and b[-1] == b[-2]:
            b.pop()
            b.pop()
            c[-1] = c[-1] + c[-2]
            c.pop()
            c.pop()
            if len(b) == 0:
                break
    for i in range(n):
        print(c[i])
