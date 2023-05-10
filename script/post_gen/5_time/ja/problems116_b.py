Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

s = int(input())
a = [s]
for i in range(2,1000000+1):
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        print(i)
        break

=======
Suggestion 2

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())

a = [s]

for i in range(2, 1000000):
    a.append(f(a[i - 2]))
    if a[i - 1] in a[:i - 1]:
        print(i)
        break

=======
Suggestion 3

def main():
    s = int(input())
    a = []
    a.append(s)
    i = 1
    while True:
        if a[i-1] % 2 == 0:
            a.append(a[i-1] // 2)
        else:
            a.append(3*a[i-1] + 1)
        if a[i] in a[:i]:
            break
        i += 1
    print(i+1)

=======
Suggestion 4

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1]) == 2:
        break
print(len(a))

=======
Suggestion 5

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
print(i-1+a[:i-1].index(a[i-1])+1)

=======
Suggestion 6

def calc(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(calc(a[i-2]))
    if a[i-1] in a[:i-1]:
        break
print(i)

=======
Suggestion 7

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(int(f(a[i-2])))
    if a[i-1] in a[0:i-1]:
        print(i)
        break

=======
Suggestion 8

def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
for i in range(2,1000001):
    a.append(f(a[i-2]))
    if a[i-1] in a[0:i-1]:
        print(i)
        break

=======
Suggestion 9

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        break
print(len(a))

=======
Suggestion 10

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1]) == 2:
        break
print(len(a))
