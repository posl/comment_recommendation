Synthesizing 10/10 solutions

=======
Suggestion 1

def g_1(x):
    # x を十進法で表したときの各桁の数字を大きい順に並び替えてできる整数
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 2

def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = "".join(x)
    x = int(x)
    return x

=======
Suggestion 3

def g1(x):
    x = str(x)
    x = sorted(x,reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

=======
Suggestion 4

def g1(x):
    x_str = str(x)
    x_str_list = list(x_str)
    x_str_list.sort(reverse=True)
    x_str = ''.join(x_str_list)
    return int(x_str)

=======
Suggestion 5

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 6

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 7

def g1(x):
    return int("".join(sorted(str(x), reverse=True)))

=======
Suggestion 8

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    return int("".join(x))

=======
Suggestion 9

def g_1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    return int(''.join(x))

=======
Suggestion 10

def g1(x):
    s = str(x)
    return int(''.join(sorted(s, reverse=True)))
