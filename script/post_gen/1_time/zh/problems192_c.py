Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g_1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 2

def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    s = ''.join(s)
    return int(s)

=======
Suggestion 3

def g_1(x):
    x_str = str(x)
    x_list = list(x_str)
    x_list.sort(reverse=True)
    x_str = ''.join(x_list)
    return int(x_str)

=======
Suggestion 4

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 5

def g_1(x):
    return int("".join(sorted(str(x), reverse=True)))

=======
Suggestion 6

def g1(x):
    s = str(x)
    l = list(s)
    l.sort(reverse=True)
    s = "".join(l)
    return int(s)

=======
Suggestion 7

def f(x):
    g1 = int("".join(sorted(str(x), reverse=True)))
    g2 = int("".join(sorted(str(x))))
    return g1 - g2

n, k = map(int, input().split())
a = n
for _ in range(k):
    a = f(a)
print(a)

=======
Suggestion 8

def g_1(x):
    x = str(x)
    x_list = []
    for i in x:
        x_list.append(i)
    x_list.sort()
    x_list.reverse()
    x = ''.join(x_list)
    return int(x)
