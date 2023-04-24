Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return burger(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + burger(n - 1, x - 2 - a[n - 1])

n, x = map(int, input().split())
a, p = [1], [1]
for i in range(n):
    a.append(2 * a[i] + 3)
    p.append(2 * p[i] + 1)
print(burger(n, x))

=======
Suggestion 2

def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return burger(n-1,x-1)
    else:
        return p[n-1] + 1 + burger(n-1,x-2-a[n-1])

n,x = map(int,input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(a[i]*2+3)
    p.append(p[i]*2+1)
print(burger(n,x))

=======
Suggestion 3

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
Suggestion 4

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
Suggestion 5

def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return burger(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + burger(n - 1, x - 2 - a[n - 1])

n, x = map(int,input().split())
p, a = [1], [1]
for i in range(n):
    p.append(2 * p[i] + 1)
    a.append(2 * a[i] + 3)
print(burger(n, x))

=======
Suggestion 6

def f(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*f(n-1,x-2):
        return f(n-1,x-2)
    else:
        return 1+2*f(n-1,x-2)-f(n-1,x-2-2*f(n-1,x-2))

n,x=map(int,input().split())
print(f(n,x))

=======
Suggestion 7

def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1+burger(n-1,x-1):
        return burger(n-1,x-1)
    else:
        return 1+burger(n-1,x-2-burger(n-1,x-2))

n,x = map(int,input().split())
print(burger(n,x))

=======
Suggestion 8

def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    num = 2**(n+2) - 3
    if x <= 1:
        return 0
    elif x <= num:
        return burger(n-1, x-1)
    elif x == num + 1:
        return 1 + burger(n-1, x-2)
    elif x <= num * 2 + 1:
        return 1 + burger(n-1, x-num-2)
    else:
        return 2**(n+1) - 1

n, x = map(int, input().split())
print(burger(n, x))
