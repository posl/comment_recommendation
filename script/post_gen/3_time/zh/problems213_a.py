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

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(A^B)

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print(a^b)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    print(a^b)
    
main()

=======
Suggestion 5

def xor(a,b):
    c = a^b
    return c

a,b = map(int,input().split())

print(xor(a,b))

=======
Suggestion 6

def xor(a,b):
    c = []
    d = []
    for i in range(8):
        c.append(a%2)
        d.append(b%2)
        a = int(a/2)
        b = int(b/2)
    e = []
    for i in range(8):
        if c[i] == d[i]:
            e.append(0)
        else:
            e.append(1)
    f = 0
    for i in range(8):
        f = f + e[i] * (2**i)
    return f
