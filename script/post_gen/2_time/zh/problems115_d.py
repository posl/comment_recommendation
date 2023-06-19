Synthesizing 10/10 solutions

=======
Suggestion 1

def burger(n,x):
    if x == 1:
        return 0
    elif n == 1:
        return 1
    else:
        if x <= 2**n-2**(n-1)+1:
            return burger(n-1,x-1)
        else:
            return 2**(n-1)+burger(n-1,x-2**(n-1))+1

=======
Suggestion 2

def num_of_patty(n):
    if n==0:
        return 0
    else:
        return 2*num_of_patty(n-1)+1

=======
Suggestion 3

def f(n,x):
    if n==0:
        return 0
    if x==1:
        return 0
    if x<=1+f(n-1,(2**(n+1)-3)//2):
        return f(n-1,x-1)
    if x==1+f(n-1,(2**(n+1)-3)//2)+1:
        return 1+f(n-1,(2**(n+1)-3)//2)
    if x<=1+f(n-1,(2**(n+1)-3)//2)+1+f(n-1,(2**(n+1)-3)//2):
        return 1+f(n-1,(2**(n+1)-3)//2)+f(n-1,x-1-f(n-1,(2**(n+1)-3)//2)-1)
    return 1+f(n-1,(2**(n+1)-3)//2)+f(n-1,(2**(n+1)-3)//2)
n,x=map(int,input().split())
print(f(n,x))

=======
Suggestion 4

def solve(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return solve(n-1, x-1)
    else:
        return p[n-1] + 1 + solve(n-1, x-2-a[n-1])

n, x = map(int, input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(1 + 2 * a[i])
    p.append(1 + 2 * p[i])
print(solve(n, x))

=======
Suggestion 5

def f(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + a[n-1]:
        return f(n-1,x-1)
    elif x == 2 + a[n-1]:
        return p[n-1] + 1
    elif x <= 2 + 2*a[n-1]:
        return p[n-1] + 1 + f(n-1,x-2-a[n-1])
    elif x == 3 + 2*a[n-1]:
        return 2*p[n-1] + 1
    else:
        return 2*p[n-1] + 1 + f(n-1,x-3-2*a[n-1])

n,x = map(int,input().split())
a = [1]
p = [1]
for i in range(n):
    a.append(2*a[i]+3)
    p.append(2*p[i]+1)
print(f(n,x))

=======
Suggestion 6

def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + burger(n-1, burger(n-1, x-1)):
        return burger(n-1, x-1)
    else:
        return 1 + burger(n-1, burger(n-1, x-2))

n, x = map(int, input().split())
print(burger(n, x))

=======
Suggestion 7

def solve(n,x):
    if n==0:
        return 0
    elif x==1:
        return 0
    elif x<=1+f[n-1]:
        return solve(n-1,x-1)
    elif x==2+f[n-1]:
        return p[n-1]+1
    elif x<=2+2*f[n-1]:
        return p[n-1]+1+solve(n-1,x-2-f[n-1])
    else:
        return 2*p[n-1]+1

n,x=map(int,input().split())
f=[1]
p=[1]
for i in range(n):
    f.append(2*f[i]+3)
    p.append(2*p[i]+1)
print(solve(n,x))

=======
Suggestion 8

def solve(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*burger[n-1]:
        return solve(n-1,x-1)
    else:
        return patty[n-1]+1+solve(n-1,x-2-burger[n-1])

n,x=map(int,input().split())
burger=[1]
patty=[1]
for i in range(n):
    burger.append(2*burger[-1]+3)
    patty.append(2*patty[-1]+1)
print(solve(n,x))

=======
Suggestion 9

def func(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + func(n-1,2**(n+1)-3):
        return func(n-1,x-1)
    elif x == 2 + func(n-1,2**(n+1)-3):
        return 1 + func(n-1,2**(n+1)-3)
    elif x <= 2 + 2*func(n-1,2**(n+1)-3):
        return 1 + func(n-1,x-2-func(n-1,2**(n+1)-3))
    elif x == 3 + 2*func(n-1,2**(n+1)-3):
        return 1 + 2*func(n-1,2**(n+1)-3)
    else:
        return 2 + func(n-1,x-3-2*func(n-1,2**(n+1)-3))

n,x = map(int,input().split())
print(func(n,x))

=======
Suggestion 10

def burger(n,x):
    if n==0:
        return 0
    elif x==1:
        return 0
    elif x<=2**(n+1)-3:
        return burger(n-1,x-1)
    elif x==2**(n+1)-2:
        return 2**n
    elif x==2**(n+1)-1:
        return 2**n
    elif x<=2**(n+2)-3:
        return 2**n+burger(n-1,x-2**(n+1)+1)
    elif x==2**(n+2)-2:
        return 2**(n+1)-1
    elif x==2**(n+2)-1:
        return 2**(n+1)-1

n,x=map(int,input().split())
print(burger(n,x))
