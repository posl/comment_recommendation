Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

=======
Suggestion 2

def g_1(x):
    a = list(str(x))
    a.sort(reverse=True)
    return int(''.join(a))

=======
Suggestion 3

def g1(x):
    x = str(x)
    x = list(x)
    x.sort()
    x = ''.join(x)
    return int(x)

=======
Suggestion 4

def g1(x):
    l = []
    while x > 0:
        l.append(x % 10)
        x //= 10
    l.sort(reverse=True)
    return 0 if l[0] == 0 else int(''.join(str(x) for x in l))

=======
Suggestion 5

def g_1(x):
    x_list = list(str(x))
    x_list.sort(reverse=True)
    return int("".join(x_list))

=======
Suggestion 6

def g1(x):
    x = str(x)
    x = ''.join(sorted(x, reverse=True))
    return int(x)

=======
Suggestion 7

def g_1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

=======
Suggestion 8

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 9

def g1(x):
    l = list(str(x))
    l.sort(reverse=True)
    return int(''.join(l))
