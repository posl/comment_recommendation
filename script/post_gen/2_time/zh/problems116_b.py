Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(f(a[i-2]))
    if a[i-1] in a[:i-1]:
        break
print(i)

=======
Suggestion 2

def calc(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)

=======
Suggestion 3

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

=======
Suggestion 4

def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

s=int(input())
a=[s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

=======
Suggestion 5

def f(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

s = int(input())
a = [s]
while True:
    next = f(a[-1])
    if next in a:
        print(len(a)+1)
        break
    else:
        a.append(next)

=======
Suggestion 6

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(raw_input())
a=[]
a.append(s)
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        break
print len(a)

=======
Suggestion 7

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

=======
Suggestion 8

def function(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    if function(a[i-1]) in a:
        print(i+1)
        break
    else:
        a.append(function(a[i-1]))
    i+=1

=======
Suggestion 9

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i=1
while True:
    a.append(f(a[i-1]))
    if a.count(a[i])==2:
        break
    i+=1
print(i+1)
