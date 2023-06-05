Synthesizing 10/10 solutions

=======
Suggestion 1

def is753Number(num):
    numStr = str(num)
    if numStr.count('7') > 0 and numStr.count('5') > 0 and numStr.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 2

def count753(n):
    if n < 357:
        return 0
    elif n < 375:
        return 1
    elif n < 537:
        return 2
    elif n < 573:
        return 3
    elif n < 735:
        return 4
    elif n < 753:
        return 5
    elif n < 3357:
        return 6
    elif n < 3375:
        return 7
    elif n < 3537:
        return 8
    elif n < 3557:
        return 9
    elif n < 3573:
        return 10
    elif n < 3575:
        return 11
    elif n < 3577:
        return 12
    else:
        return 13

=======
Suggestion 3

def check753(num):
    check = set(['3','5','7'])
    num_str = str(num)
    for i in check:
        if i not in num_str:
            return False
    return True

=======
Suggestion 4

def is753(n):
    return set(list(str(n))) == set(list('357'))

=======
Suggestion 5

def count753(n, num):
    if num > n:
        return 0
    ret = 1 if num >= 357 else 0
    ret += count753(n, num * 10 + 3)
    ret += count753(n, num * 10 + 5)
    ret += count753(n, num * 10 + 7)
    return ret

n = int(input())
print(count753(n, 0))

=======
Suggestion 6

def is753(num):
    num = str(num)
    if "7" in num and "5" in num and "3" in num:
        return True
    else:
        return False

=======
Suggestion 7

def check753(n):
    if n < 357:
        return False
    if n % 2 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    return True

=======
Suggestion 8

def dfs(n, use):
    if n > N:
        return 0
    ret = 1 if use == 0b111 else 0
    ret += dfs(n * 10 + 3, use | 0b001)
    ret += dfs(n * 10 + 5, use | 0b010)
    ret += dfs(n * 10 + 7, use | 0b100)
    return ret

N = int(input())
print(dfs(0, 0))

=======
Suggestion 9

def is753(num):
    num_str = str(num)
    if num_str.count('7') > 0 and num_str.count('5') > 0 and num_str.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 10

def is753num(num):
    strnum = str(num)
    if strnum.count("7") > 0 and strnum.count("5") > 0 and strnum.count("3") > 0:
        return True
    else:
        return False
