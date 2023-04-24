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

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1] % 2 == 0:
            a.append(a[-1] // 2)
        else:
            a.append(3 * a[-1] + 1)
        if a[-1] in a[:-1]:
            print(len(a) - 1)
            return

=======
Suggestion 3

def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1]%2 == 0:
            a.append(a[-1]//2)
        else:
            a.append(3*a[-1]+1)
        if a[-1] in a[:-1]:
            print(len(a))
            break

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
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a) - 1)
        break

=======
Suggestion 5

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

s = int(input())
a = [s]
while True:
    a.append(f(a[-1]))
    if a[-1] in a[:-1]:
        print(len(a))
        break

=======
Suggestion 6

def  f (n):
     if  n % 2 == 0:
         return  n / 2
     else :
         return  3 * n + 1
