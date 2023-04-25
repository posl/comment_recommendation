Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

=======
Suggestion 2

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
        print(i + 1)
        break
    i += 1

=======
Suggestion 3

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
for i in range(1,1000000):
    a.append(f(a[i-1]))
    if len(a) != len(set(a)):
        print(i+1)
        break

=======
Suggestion 4

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

s = int(input())
a = [s]
for i in range(1,1000000):
    a.append(f(a[i-1]))
    if a[i] in a[:-1]:
        print(i+1)
        break

=======
Suggestion 5

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

=======
Suggestion 6

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s = int(input())
a = [s]
for i in range(1,1000000):
    a.append(f(a[i-1]))
    if a[i-1] in a[:i-1]:
        print(i+1)
        exit()

=======
Suggestion 7

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        print(i)
        break

=======
Suggestion 8

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())

a = [s]
i = 1
while True:
    a.append(f(a[i-1]))
    if a[i] in a[:i]:
        break
    i += 1

print(i+1)

=======
Suggestion 9

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
m = 0
while True:
    m += 1
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        break
print(m+1)

=======
Suggestion 10

def func(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
while True:
    a.append(func(a[-1]))
    if a.count(a[-1]) == 2:
        print(len(a))
        break
