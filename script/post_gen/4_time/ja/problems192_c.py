Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g1(x):
    #x を十進法で表したときの各桁の数字を大きい順に並び替えてできる整数
    str_x = str(x)
    list_str_x = sorted(str_x, reverse=True)
    return int("".join(list_str_x))

=======
Suggestion 2

def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 3

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = int(''.join(x))
    return x

=======
Suggestion 4

def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = "".join(x)
    return int(x)

=======
Suggestion 5

def g1(x):
    l = []
    for i in range(len(str(x))):
        l.append(int(str(x)[i]))
    l.sort(reverse=True)
    ret = 0
    for i in range(len(l)):
        ret += l[i] * (10 ** (len(l)-i-1))
    return ret

=======
Suggestion 6

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 7

def g1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))

=======
Suggestion 8

def g1(n):
    s = str(n)
    l = list(s)
    l.sort(reverse = True)
    s = ''.join(l)
    return int(s)
