Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def xor(a,b):
    c = 0
    for i in range(8):
        if a%2 != b%2:
            c += 2**i
        a = a//2
        b = b//2
    return c

a,b = map(int,input().split())
print(xor(a,b))

=======
Suggestion 2

def xor(a, b):
    return a ^ b

a, b = map(int, input().split())

print(xor(a, b))

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    c = a^b
    print(c)

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print(a^b)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(A^B)

=======
Suggestion 6

def xor(a,b):
    if a == b:
        return 0
    else:
        return 1

=======
Suggestion 7

def xor(a,b):
    a = int(a)
    b = int(b)
    return a^b

=======
Suggestion 8

def xor(a,b):
    return a^b
