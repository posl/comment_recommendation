Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    g1 = int(''.join(sorted(str(x), reverse=True)))
    g2 = int(''.join(sorted(str(x))))
    return g1 - g2

N, K = map(int, input().split())
for i in range(K):
    N = f(N)
print(N)

=======
Suggestion 2

def f(x):
    g1 = int("".join(sorted(str(x), reverse=True)))
    g2 = int("".join(sorted(str(x))))
    return g1 - g2

N, K = map(int, input().split())

for i in range(K):
    N = f(N)
print(N)

=======
Suggestion 3

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 4

def g1(x):
    l = list(str(x))
    l.sort(reverse=True)
    return int(''.join(l))

=======
Suggestion 5

def g1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))

=======
Suggestion 6

def g_1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))

=======
Suggestion 7

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    return int("".join(x))
