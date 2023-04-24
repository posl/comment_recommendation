Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 2

def g1(x):
    s = list(str(x))
    s.sort(reverse=True)
    return int("".join(s))

=======
Suggestion 3

def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    return int(''.join(s))

=======
Suggestion 4

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 5

def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    return int("".join(s))

=======
Suggestion 6

def g1(x):
    list_x = list(str(x))
    list_x.sort(reverse=True)
    str_x = "".join(list_x)
    return int(str_x)

=======
Suggestion 7

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))
