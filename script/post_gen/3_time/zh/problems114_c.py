Synthesizing 10/10 solutions

=======
Suggestion 1

def is753(n):
    n = str(n)
    if '7' in n and '5' in n and '3' in n:
        return True
    else:
        return False

=======
Suggestion 2

def is753(n):
    n = str(n)
    if n.count('7') > 0 and n.count('5') > 0 and n.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 3

def is753(n):
    if "7" in str(n) and "5" in str(n) and "3" in str(n):
        return True
    else:
        return False

N = int(input())
count = 0
for i in range(1,N+1):
    if is753(i):
        count += 1
print(count)

=======
Suggestion 4

def is753(n):
    s = str(n)
    return s.count('7') and s.count('5') and s.count('3')

=======
Suggestion 5

def is753(n):
    if n%10 == 7 or n%10 == 5 or n%10 == 3:
        return True
    elif n < 10:
        return False
    else:
        return is753(n//10)

=======
Suggestion 6

def check753(n):
    if n < 357:
        return False
    if n % 7 == 0 or n % 5 == 0 or n % 3 == 0:
        return False
    if '7' not in str(n) or '5' not in str(n) or '3' not in str(n):
        return False
    return True

=======
Suggestion 7

def count753(N):
    if N < 3:
        return 0
    if N == 3:
        return 1
    if N > 3:
        n = 0
        for i in range(3, N + 1):
            if '3' in str(i) and '5' in str(i) and '7' in str(i):
                n += 1
        return n

=======
Suggestion 8

def is753(num):
    s = str(num)
    if '7' in s and '5' in s and '3' in s:
        return True
    return False

=======
Suggestion 9

def is753(n):
    n = str(n)
    return n.count('3') >= 1 and n.count('5') >= 1 and n.count('7') >= 1

=======
Suggestion 10

def is753(num):
    exist7 = False
    exist5 = False
    exist3 = False
    for i in str(num):
        if i == '7':
            exist7 = True
        elif i == '5':
            exist5 = True
        elif i == '3':
            exist3 = True
    if exist7 and exist5 and exist3:
        return True
    else:
        return False
