Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

n = int(input())
print(*S(n))

=======
Suggestion 2

def S(n):
    if n == 1:
        return [1]
    else:
        return S(n-1) + [n] + S(n-1)

n = int(input())
print(' '.join(map(str, S(n))))

=======
Suggestion 3

def getSn(n):
    if n == 1:
        return [1]
    else:
        return getSn(n-1) + [n] + getSn(n-1)

=======
Suggestion 4

def get_sn(n):
    if n == 1:
        return [1]
    else:
        sn_1 = get_sn(n-1)
        return sn_1 + [n] + sn_1

=======
Suggestion 5

def s(n):
    if n == 1:
        return [1]
    else:
        sn = s(n-1)
        return sn + [n] + sn

n = int(input())
print(*s(n))

=======
Suggestion 6

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

=======
Suggestion 7

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(*s(n))

=======
Suggestion 8

def S(n):
    if n == 1:
        return [1]
    else:
        a = S(n-1)
        return a + [n] + a

n = int(input())
print(*S(n))

=======
Suggestion 9

def recursion(n):
    if n == 1:
        return [1]
    else:
        l = recursion(n-1)
        return l + [n] + l

n = int(input())
print(*recursion(n))
