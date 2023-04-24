Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

=======
Suggestion 2

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
Suggestion 3

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
    a.append(f(a[i - 1]))
    i += 1
    if a.count(a[i - 1]) == 2:
        break
print(a.index(a[i - 1]) + 1)

=======
Suggestion 4

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1] % 2 == 0:
            a.append(a[-1] // 2)
        else:
            a.append(3*a[-1] + 1)
        if a[-1] in a[:-1]:
            print(len(a))
            break

=======
Suggestion 5

def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

=======
Suggestion 6

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
n = 1
while True:
    a.append(f(a[n-1]))
    if a[n-1] in a[:n-1]:
        print(n)
        break
    n += 1

=======
Suggestion 7

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
m = 0
while True:
    n = f(a[-1])
    if n in a:
        m = a.index(n)
        break
    a.append(n)
print(m + 1)

=======
Suggestion 8

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[s]
for i in range(1000000):
    a.append(f(a[i]))
    if a[i] in a[:i]:
        print(i+1)
        break

=======
Suggestion 9

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

S = int(input())
a = [S]

i = 1
while True:
    a.append(f(a[i-1]))
    if a[i] in a[:i]:
        print(i+1)
        break
    i += 1
