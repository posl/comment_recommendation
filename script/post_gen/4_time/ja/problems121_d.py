Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return (b - a + 1) // 2 % 2
    elif a % 2 == 0 and b % 2 != 0:
        return (b - a + 2) // 2 % 2
    elif a % 2 != 0 and b % 2 == 0:
        return (b - a) // 2 % 2
    else:
        return (b - a + 1) // 2 % 2

=======
Suggestion 2

def f(A, B):
    if A == B:
        return A
    elif A == 0:
        return f(1, B)
    elif A % 2 == 0:
        return f(A + 1, B) ^ A
    else:
        return f(A - 1, B) ^ A

A, B = map(int, input().split())
print(f(A, B))

=======
Suggestion 3

def f(a, b):
    if a == b:
        return a
    if a % 2 == 0:
        if (b - a) % 2 == 0:
            return (b - a) ^ b
        else:
            return (b - a) ^ b ^ 1
    else:
        if (b - a) % 2 == 0:
            return (b - a) ^ b ^ a
        else:
            return (b - a) ^ b ^ a ^ 1

a, b = map(int, input().split())
print(f(a, b))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
    else:
        print(a ^ b)

=======
Suggestion 5

def f(a,b):
    if a == b:
        return a
    elif a == 0:
        return f(b)
    else:
        return f(b) ^ f(a-1)

a,b = map(int,input().split())
print(f(a,b))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(a^b)

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    print(f(a, b))

=======
Suggestion 8

def f(a, b):
    if a == b:
        return a
    else:
        return 0

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    #print(A,B)
    #print(bin(A),bin(B))
    #print(bin(A^B))
    print(A^B)
