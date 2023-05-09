Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = N
    for i in range(K):
        g1 = int("".join(sorted(str(a), reverse=True)))
        g2 = int("".join(sorted(str(a))))
        a = g1 - g2
    print(a)

=======
Suggestion 2

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 3

def g_1(x):
    digits = [int(d) for d in str(x)]
    digits.sort(reverse=True)
    return int(''.join(str(d) for d in digits))

=======
Suggestion 4

def g_1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 5

def g_1(x):
    x = list(str(x))
    x.sort(reverse=True)
    return int(''.join(x))

=======
Suggestion 6

def g_1(x):
    return int("".join(sorted(str(x), reverse=True)))

=======
Suggestion 7

def g_1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    return int("".join(x))

=======
Suggestion 8

def g_1(x):
    s = str(x)
    s = sorted(s,reverse=True)
    return int(''.join(s))
