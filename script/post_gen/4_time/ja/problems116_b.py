Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
for i in range(2, 10**6):
    a.append(f(a[i-2]))
    if a[i-1] in a[0:i-1]:
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
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

=======
Suggestion 3

def main():
    s = int(input())
    a = [s]
    i = 1
    while True:
        if a[i-1] % 2 == 0:
            a.append(int(a[i-1]/2))
        else:
            a.append(int(3*a[i-1]+1))
        if a.count(a[i]) == 2:
            break
        i += 1
    print(i+1)

=======
Suggestion 4

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())

a = [s]
while True:
    if a[-1] in a[:-1]:
        break
    a.append(f(a[-1]))

print(len(a))

=======
Suggestion 5

def main():
    s = int(input())
    a = [s]
    i = 1
    while True:
        i += 1
        if a[-1] % 2 == 0:
            a.append(a[-1] / 2)
        else:
            a.append(3 * a[-1] + 1)
        if a.count(a[-1]) == 2:
            print(i)
            break

=======
Suggestion 6

def func(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())

a = [s]
i = 1
while True:
    a.append(func(a[i-1]))
    if a[i] in a[:i]:
        print(i+1)
        break
    i += 1

=======
Suggestion 7

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    if f(a[i-1]) in a:
        print(i+1)
        break
    else:
        a.append(f(a[i-1]))
        i+=1

=======
Suggestion 8

def solve():
    s = int(input())
    a = []
    a.append(s)
    for i in range(1, 1000000):
        if a[i-1] % 2 == 0:
            a.append(int(a[i-1]/2))
        else:
            a.append(int(3*a[i-1]+1))
        for j in range(i-1):
            if a[i] == a[j]:
                print(i+1)
                return
solve()

=======
Suggestion 9

def func(s):
    if s % 2 == 0:
        return s // 2
    else:
        return 3 * s + 1

s = int(input())
a = [s]
i = 1
while True:
    if a[i-1] in a[:i-1]:
        print(i+1)
        break
    else:
        a.append(func(a[i-1]))
        i += 1

=======
Suggestion 10

def func(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[0 for i in range(1000000)]
a[0]=s

for i in range(1,1000000):
    a[i]=func(a[i-1])
    if a[i] in a[:i-1]:
        print(i+1)
        exit()
