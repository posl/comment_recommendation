Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g_1(x):
    x_str = str(x)
    x_list = list(x_str)
    x_list.sort(reverse=True)
    x_str = "".join(x_list)
    return int(x_str)

=======
Suggestion 2

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = int(''.join(x))
    return x

=======
Suggestion 3

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 4

def g1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))

=======
Suggestion 5

def g1(x):
    return int("".join(sorted(list(str(x)), reverse=True)))

=======
Suggestion 6

def g1(x):
    return int(''.join(sorted(str(x))[::-1]))

=======
Suggestion 7

def g1(x):
    s = str(x)
    return int(''.join(sorted(s, reverse=True)))

=======
Suggestion 8

def g1(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))
