Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))

=======
Suggestion 2

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 3

def g1(x):
    s = str(x)
    s = ''.join(sorted(s, reverse=True))
    return int(s)

=======
Suggestion 4

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 5

def g1(x):
    x=str(x)
    x=list(x)
    x.sort(reverse=True)
    x="".join(x)
    x=int(x)
    return x

=======
Suggestion 6

def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    return int("".join(s))

=======
Suggestion 7

def g_1(x):
    return int(''.join(sorted(str(x), reverse=True)))
