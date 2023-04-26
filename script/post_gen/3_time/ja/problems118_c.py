Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        a.append(a.pop() % a.pop(0))
        a.sort()
    print(a[0])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        if a[-1] > a[-2]:
            a[-1] = a[-1] % a[-2]
            a.sort()
        else:
            a.pop(-1)
    print(a[0])

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    while True:
        a.sort()
        a = list(set(a))
        if len(a) == 1:
            break
        else:
            a[-1] = a[-1] % a[0]
            if a[-1] == 0:
                a.pop()
    print(a[0])

=======
Suggestion 7

def gcd(a,b):
    if a%b==0:
        return(b)
    else:
        return(gcd(b,a%b))

n = int(input())
a = list(map(int,input().split()))
a.sort()
m = a[0]
for i in range(n):
    m = gcd(m,a[i])
print(m)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a = [min(a), max(a) % min(a)]
        a = [i for i in a if i != 0]
    print(a[0])

=======
Suggestion 9

def calc(a, b):
    return a % b
