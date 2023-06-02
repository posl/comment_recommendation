Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n%2==0:
        return int(n/2)
    else:
        return int(3*n+1)

s=int(input())
a=[s]
while True:
    a.append(f(a[-1]))
    if a.count(a[-1])>=2:
        break
print(len(a)-1)

=======
Suggestion 2

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[]
a.append(s)
i=1
while True:
    a.append(f(a[i-1]))
    for j in range(i-1):
        if a[i]==a[j]:
            print(i)
            exit()
    i+=1

=======
Suggestion 3

def func(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n+1

=======
Suggestion 4

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s = int(raw_input())
a = [s]
while True:
    s = f(s)
    if s in a:
        break
    a.append(s)
print len(a)+1

=======
Suggestion 5

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=int(input())
a=[]
a.append(s)
i=1
while True:
    a.append(f(a[i-1]))
    if a[i] in a[:i-1]:
        break
    i+=1
print(i+1)

=======
Suggestion 6

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

=======
Suggestion 7

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
    a.append(f(a[i - 2]))
    if a.count(a[i - 1]) == 2:
        break
print(i)

=======
Suggestion 8

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
while True:
    s = f(s)
    if s in a:
        print(len(a)+1)
        break
    else:
        a.append(s)
