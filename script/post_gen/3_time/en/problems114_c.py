Synthesizing 10/10 solutions

=======
Suggestion 1

def isShichiGoSan(n):
    if "7" in str(n) and "5" in str(n) and "3" in str(n):
        return True
    else:
        return False

=======
Suggestion 2

def check(n):
    if '3' in str(n) and '5' in str(n) and '7' in str(n):
        return True
    else:
        return False

=======
Suggestion 3

def isShichiGoSan(num):
    num_str = str(num)
    if '7' in num_str and '5' in num_str and '3' in num_str:
        return True
    else:
        return False

=======
Suggestion 4

def isSGS(n):
    if "7" in str(n) and "5" in str(n) and "3" in str(n):
        return True
    else:
        return False

=======
Suggestion 5

def isShichiGoSan(n):
    nstr = str(n)
    if nstr.count('7') > 0 and nstr.count('5') > 0 and nstr.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 6

def check753(n):
    n = str(n)
    if ('7' in n) and ('5' in n) and ('3' in n):
        return True
    else:
        return False

=======
Suggestion 7

def check753(num):
    if num < 10:
        if num == 7 or num == 5 or num == 3:
            return True
        else:
            return False
    else:
        if num % 10 == 7:
            return check753(num // 10)
        elif num % 10 == 5:
            return check753(num // 10)
        elif num % 10 == 3:
            return check753(num // 10)
        else:
            return False

=======
Suggestion 8

def check753(num):
    if num >= 1000:
        if num % 10 == 7:
            return check753(num // 10)
        elif num % 10 == 5:
            return check753(num // 10)
        elif num % 10 == 3:
            return check753(num // 10)
        else:
            return False
    else:
        if num == 7:
            return True
        elif num == 5:
            return True
        elif num == 3:
            return True
        else:
            return False

=======
Suggestion 9

def is_sgs(n):
    if '3' in n and '5' in n and '7' in n:
        return True
    return False

=======
Suggestion 10

def is_shichigosan(n):
    digits = [int(d) for d in str(n)]
    return (7 in digits) and (5 in digits) and (3 in digits) and (set(digits) <= {7, 5, 3})
