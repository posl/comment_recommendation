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
        return n / 2
    else:
        return 3 * n + 1

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
    if a[i] in a[:i]:
        print(i + 1)
        break
    i += 1

=======
Suggestion 4

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
        print(i+1)
        break
    i += 1

=======
Suggestion 5

def main():
    s = int(input())
    a = [s]
    for i in range(1, 1000000):
        if a[i-1] % 2 == 0:
            a.append(a[i-1] // 2)
        else:
            a.append(3*a[i-1]+1)
        if a[i] in a[:i]:
            print(i+1)
            break
