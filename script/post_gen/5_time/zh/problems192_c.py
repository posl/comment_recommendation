Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def g_1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = ''.join(x)
    return int(x)

=======
Suggestion 2

def f(x):
    g1 = int(''.join(sorted(str(x), reverse=True)))
    g2 = int(''.join(sorted(str(x))))
    return g1 - g2

N, K = map(int, input().split())
a = [N]
for i in range(1, K + 1):
    a.append(f(a[i - 1]))
print(a[K])

=======
Suggestion 3

def g_1(x):
    return int(''.join(sorted(str(x),reverse=True)))

=======
Suggestion 4

def g_1(x):
    s = str(x)
    l = list(s)
    l.sort(reverse=True)
    s = ''.join(l)
    return int(s)

=======
Suggestion 5

def g_1(x):
    x = list(str(x))
    x.sort(reverse=True)
    x = int(''.join(x))
    return x

=======
Suggestion 6

def g_1(x):
    str_x = str(x)
    list_x = list(str_x)
    list_x.sort(reverse=True)
    str_x = ''.join(list_x)
    return int(str_x)

=======
Suggestion 7

def g_1(x):
    x = list(str(x))
    x.sort(reverse=True)
    return int(''.join(x))

=======
Suggestion 8

def g_1(x):
    x_str = str(x)
    x_str_list = list(x_str)
    x_str_list.sort(reverse=True)
    g_1_x = int(''.join(x_str_list))
    return g_1_x
