Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(a,b):
    c=a
    for i in range(a+1,b+1):
        c=c^i
    return c

=======
Suggestion 2

def f(A, B):
    if A == B:
        return A
    else:
        return A ^ B

A, B = map(int, input().split())
print(f(A, B))

=======
Suggestion 3

def f(a, b):
    if a == b:
        return a
    else:
        return (a & b) + f(a+1, b)

=======
Suggestion 4

def f(A,B):
    if A == B:
        return A
    else:
        return A^B

=======
Suggestion 5

def f(a,b):
    #print(a,b)
    if a==b:
        return a
    elif a+1==b:
        return a^b
    elif a+2==b:
        return a^b^(a+1)
    else:
        if a%2==0:
            if b%2==0:
                return f(a,b-1)^b
            else:
                return f(a,b-2)^b^(b-1)
        else:
            if b%2==0:
                return f(a+1,b)^a
            else:
                return f(a+2,b)^a^(a+1)

=======
Suggestion 6

def f(a, b):
    if a == b:
        return a
    else:
        return f(a, b-1) ^ b

a, b = map(int, input().split())
print(f(a, b))

=======
Suggestion 7

def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(0, b)
    if a & 1:
        return f(a + 1, b) ^ a
    if b & 1:
        return f(a, b - 1) ^ b
    return f(a >> 1, b >> 1) << 1

a, b = map(int, input().split())
print(f(a, b))

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(f(a, b))

=======
Suggestion 9

def f(a, b):
    if a == b:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return f(a // 2, b // 2) * 2
    if a % 2 == 0 and b % 2 == 1:
        return f(a // 2, b // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 0:
        return f((a + 1) // 2, b // 2) * 2
    if a % 2 == 1 and b % 2 == 1:
        return f((a + 1) // 2, b // 2) * 2 + 1

a, b = map(int, input().split())
print(f(a, b))
