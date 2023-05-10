Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return burger(n-1, x-1)
    else:
        return p[n-1] + 1 + burger(n-1, x-2-a[n-1])

n, x = map(int, input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(2 * a[i] + 3)
    p.append(2 * p[i] + 1)
print(burger(n, x))

=======
Suggestion 2

def burger(n):
    if n == 0:
        return 'P'
    return burger(n-1) + 'B' + burger(n-1) + 'P' + burger(n-1) + 'B'

=======
Suggestion 3

def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + burger(n-1, x-2):
        return burger(n-1, x-2)
    else:
        return 1 + burger(n-1, x-2) + 1

n, x = map(int, input().split())
print(burger(n, x))

=======
Suggestion 4

def burger(n, x):
    if n == 0:
        return 1
    p = 2**(n+2)-3
    if x == 1:
        return 0
    elif x <= p:
        return burger(n-1, x-1)
    elif x == p+1:
        return 1+burger(n-1, x-1)
    elif x <= p*2:
        return 1+burger(n-1, x-1-p)+1
    else:
        return 1+burger(n-1, x-1-p*2)+1+burger(n-1, x-1-p*2)

n, x = map(int, input().split())
print(burger(n, x))

=======
Suggestion 5

def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + burger(n - 1, x - 2):
        return burger(n - 1, x - 2)
    else:
        return 1 + burger(n - 1, x - 2 - burger(n - 1, x - 2))

n, x = map(int, input().split())
print(burger(n, x))

=======
Suggestion 6

def burger(l,x):
    if l == 0:
        return 1
    elif x == 1:
        return 0
    elif x <= 1 + burger(l-1,x-1):
        return burger(l-1,x-1)
    elif x == 2 + burger(l-1,x-2):
        return 1 + burger(l-1,x-2)
    elif x <= 2 + 2*burger(l-1,x-2):
        return 1 + burger(l-1,x-2)
    else:
        return 2 + 2*burger(l-1,x-2)

l,x = map(int,input().split())
print(burger(l,x))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    patty = [1]
    bread = [1]
    for i in range(50):
        patty.append(patty[i] * 2 + 1)
        bread.append(bread[i] * 2 + 3)
    def f(N, X):
        if N == 0:
            return 0 if X <= 0 else 1
        elif X <= 1 + bread[N - 1]:
            return f(N - 1, X - 1)
        else:
            return patty[N - 1] + 1 + f(N - 1, X - 2 - bread[N - 1])
    print(f(N, X))

=======
Suggestion 8

def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return burger(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + burger(n - 1, x - 2 - a[n - 1])

n, x = map(int, input().split())
p = [1]
a = [1]
for i in range(n):
    p.append(p[i] * 2 + 1)
    a.append(a[i] * 2 + 3)
print(burger(n, x))
