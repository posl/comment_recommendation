Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    for i in range(K):
        N = int(''.join(sorted(str(N), reverse=True))) - int(''.join(sorted(str(N))))
    print(N)

=======
Suggestion 2

def f(x):
    x = str(x)
    g1 = ''.join(sorted(x, reverse=True))
    g2 = ''.join(sorted(x))
    return int(g1) - int(g2)

N, K = map(int, input().split())
a = N
for i in range(K):
    a = f(a)
print(a)

I think this is the best solution for this problem.

=======
Suggestion 3

def f(x):
    s = str(x)
    s = ''.join(sorted(s))
    g1 = int(s[::-1])
    g2 = int(s)
    return g1 - g2

=======
Suggestion 4

def f(n):
    if n == 0:
        return 0
    else:
        g1 = int("".join(sorted(str(n), reverse=True)))
        g2 = int("".join(sorted(str(n), reverse=False)))
        return g1 - g2

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    a = [N]
    for i in range(K):
        if a[i] == 0:
            break
        a.append(int(''.join(sorted(str(a[i]), reverse=True))) - int(''.join(sorted(str(a[i])))))
    print(a[-1])

=======
Suggestion 6

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 7

def g1(n):
    return int("".join(sorted(str(n), reverse=True)))
