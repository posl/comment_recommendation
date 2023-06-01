Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

=======
Suggestion 2

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = []
a.append(s)
i = 1
while True:
    a.append(f(a[i - 1]))
    if a[i] in a[:i]:
        break
    i += 1
print(i + 1)

=======
Suggestion 3

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
    a.append(f(a[i - 1]))
    if a[i] in a[:i]:
        break
    i += 1
print(i + 1)

=======
Suggestion 4

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    i+=1
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        print(i)
        break

=======
Suggestion 5

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

=======
Suggestion 6

def f(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1

=======
Suggestion 7

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s=int(input())
a=[s]
for i in range(2,1000000):
    a.append(f(a[-1]))
    if a.count(a[-1])>=2:
        break
print(len(a))

=======
Suggestion 8

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

=======
Suggestion 9

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s=int(input())
a=[s]
i=1
while True:
    i+=1
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        break
print(i)
