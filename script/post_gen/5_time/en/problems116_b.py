Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

=======
Suggestion 2

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
for i in range(2,1000000):
    a.append(f(a[i-2]))
    if a[i-1] in a[0:i-2]:
        print(i)
        break

=======
Suggestion 3

def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 1
while True:
    i += 1
    a.append(f(a[i-2]))
    if a.count(a[i-1]) == 2:
        print(i)
        break

=======
Suggestion 4

def f(n):
  if n % 2 == 0:
    return int(n / 2)
  else:
    return 3 * n + 1

s = int(input())
a = [s]
i = 1
while True:
  a.append(f(a[i-1]))
  if a[i] in a[:i]:
    print(i+1)
    break
  i += 1

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
    if a[i-1] in a[:-1]:
        print(i)
        break

=======
Suggestion 6

def f(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [s]
i = 0
while True:
    a.append(f(a[i]))
    i += 1
    if a[i] in a[:i]:
        print(i+1)
        break

=======
Suggestion 7

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1] % 2 == 0:
            a.append(int(a[-1] / 2))
        else:
            a.append(3 * a[-1] + 1)
        if a.count(a[-1]) == 2:
            break
    print(len(a))

=======
Suggestion 8

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1

s = int(input())
l = [s]
while True:
    s = f(s)
    if s in l:
        print(l.index(s)+1)
        break
    else:
        l.append(s)

=======
Suggestion 9

def calc(a):
    if a % 2 == 0:
        return a/2
    else:
        return 3*a+1

s = int(input())
a = [s]
i = 1
while True:
    a.append(calc(a[i-1]))
    if a[i] in a[:i]:
        print(i+1)
        break
    i += 1
