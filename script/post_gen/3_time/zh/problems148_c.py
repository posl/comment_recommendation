Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

A, B = map(int, input().split())
print(lcm(A, B))

=======
Suggestion 2

def solve():
    a,b = map(int, input().split())
    print(a*b)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 4

def cal(x,y):
    if x>y:
        return cal(y,x)
    else:
        if y%x==0:
            return x
        else:
            return cal(y%x,x)

=======
Suggestion 5

def lcd(a,b):
    a, b = (a, b) if a > b else (b, a)
    while b > 0:
        a, b = b, a % b
    return a

a,b=map(int,input().split(" "))
print(a*b//lcd(a,b))

=======
Suggestion 6

def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a % b)
a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
print(a * b // gcd(a, b))

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(a*b)
