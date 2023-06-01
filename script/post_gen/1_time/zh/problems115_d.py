Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num_of_patty(n, x):
    if n == 0:
        return 0
    elif x == 1 and n == 1:
        return 0
    elif x <= 1 + get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return get_num_of_patty(n - 1, x - 1)
    elif x == 2 + get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return 1 + get_num_of_patty(n - 1, x - 2)
    elif x <= 2 + 2 * get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return 1 + get_num_of_patty(n - 1, x - 2)
    elif x == 3 + 2 * get_num_of_patty(n - 1, (2 ** n - 1) / 2):
        return 2 + get_num_of_patty(n - 1, x - 3)
    else:
        return 2 + get_num_of_patty(n - 1, x - 3)

=======
Suggestion 2

def hamburger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + hamburger(n-1,n-1):
        return hamburger(n-1,x-1)
    elif x == 2 + hamburger(n-1,n-1):
        return 1 + hamburger(n-1,n-1)
    elif x <= 2 + 2 * hamburger(n-1,n-1):
        return 1 + hamburger(n-1,x-2-hamburger(n-1,n-1))
    else:
        return 2 * hamburger(n-1,n-1) + 1

n,x = map(int,input().split())
print(hamburger(n,x))

=======
Suggestion 3

def f(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*f(n-1,2**(n-1)-1):
        return f(n-1,x-1)
    else:
        return 1+2*f(n-1,2**(n-1)-1)+f(n-1,x-2-2*f(n-1,2**(n-1)-1))

=======
Suggestion 4

def f(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + a[n-1]:
        return f(n-1,x-1)
    elif x == 2 + a[n-1]:
        return p[n-1] + 1
    elif x <= 2 + 2 * a[n-1]:
        return p[n-1] + 1 + f(n-1,x-2-a[n-1])
    elif x == 3 + 2 * a[n-1]:
        return 2 * p[n-1] + 1
    else:
        return 2 * p[n-1] + 1 + f(n-1,x-3-2*a[n-1])

n,x = map(int,input().split())
a = [0] * 51
p = [0] * 51
a[0] = 1
p[0] = 1
for i in range(1,51):
    a[i] = 2 * a[i-1] + 3
    p[i] = 2 * p[i-1] + 1
print(f(n,x))

=======
Suggestion 5

def f(n,x):
    if n==0:
        return 0
    elif x==1:
        return 0
    elif x<=1+f(n-1,x-1):
        return f(n-1,x-1)
    elif x==2+f(n-1,x-1):
        return 1+g(n-1)
    elif x<=2+2*f(n-1,x-2):
        return 1+g(n-1)+f(n-1,x-2)
    else:
        return 1+2*g(n-1)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    if X == 1:
        print(0)
        return
    if X == 2**(N+1) - 1:
        print(2**N - 1)
        return
    if X < 2**(N+1) - 1:
        solve()
    else:
        print(2**N - 1)
        return

solve()

=======
Suggestion 7

def solve(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return solve(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + solve(n - 1, x - 2 - a[n - 1])

n, x = map(int, input().split())
p = [1]
a = [1]
for i in range(n):
    p.append(2 * p[i] + 1)
    a.append(2 * a[i] + 3)
print(solve(n, x))

=======
Suggestion 8

def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    y = (2 ** (n + 2)) - 3
    if x <= 1:
        return 0
    elif x <= y:
        return f(n - 1, x - 1)
    elif x == y + 1:
        return 1 + (2 ** n - 1)
    elif x <= 2 * y + 2:
        return 1 + (2 ** n - 1) + f(n - 1, x - y - 2)
    else:
        return 2 * (2 ** n - 1)

=======
Suggestion 9

def hamburger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + hamburger(n-1, (2**(n+1)-3)//2 + 1):
        return hamburger(n-1, x-1)
    else:
        return 1 + hamburger(n-1, x - (2**(n+1)-3)//2 - 1)

=======
Suggestion 10

def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return f(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + f(n - 1, x - 2 - a[n - 1])

n, x = map(int, input().split())
p = [1]
a = [1]
for i in range(n):
    p.append(p[i] * 2 + 1)
    a.append(a[i] * 2 + 3)
print(f(n, x))
