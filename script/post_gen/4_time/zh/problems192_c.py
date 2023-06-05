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
    x_str = str(x)
    x_list = list(x_str)
    x_list.sort(reverse=True)
    return int(''.join(x_list))

=======
Suggestion 3

def g1(x):
    l = list(str(x))
    l.sort(reverse=True)
    return int(''.join(l))

=======
Suggestion 4

def g1(x):
    return int(''.join(sorted(str(x), reverse=True)))

=======
Suggestion 5

def g_1(x):
    x_str = str(x)
    x_str = sorted(x_str,reverse=True)
    x_str = ''.join(x_str)
    x_int = int(x_str)
    return x_int

=======
Suggestion 6

def g_1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = int(''.join(x))
    return x

=======
Suggestion 7

def g1(x):
    #将x的十进制数字按降序重新排列而得到的整数
    #例如，我们有g_1（314）=431
    #注意，前导零被忽略。
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = "".join(x)
    x = int(x)
    return x

=======
Suggestion 8

def g_1(x):
    return int(''.join(sorted(str(x),reverse=True)))

=======
Suggestion 9

def g_1(x):
    return int(''.join(sorted(list(str(x)),reverse=True)))
