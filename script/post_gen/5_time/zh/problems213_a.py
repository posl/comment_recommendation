Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    print(a^b)

=======
Suggestion 2

def xor(a,b):
    c = 0
    for i in range(8):
        if (a >> i) & 1 != (b >> i) & 1:
            c += 1 << i
    return c

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    for i in range(256):
        if a^i==b:
            print(i)
            break

=======
Suggestion 4

def xor(a, b):
    return a ^ b

=======
Suggestion 5

def xor(a, b):
    c = 0
    for i in range(8):
        if (a % 2) != (b % 2):
            c += 2**i
        a //= 2
        b //= 2
    return c

=======
Suggestion 6

def xor(a,b):
    return a^b

a,b = map(int,input().split())
print(xor(a,b))

=======
Suggestion 7

def xor(a,b):
    c = a^b
    return c

a,b = input().split()
a = int(a)
b = int(b)
c = xor(a,b)
print(c)
