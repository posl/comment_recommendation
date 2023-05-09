Synthesizing 10/10 solutions

=======
Suggestion 1

def isShichiGoSan(n):
    if '7' in str(n) and '5' in str(n) and '3' in str(n):
        return True
    else:
        return False

=======
Suggestion 2

def isShichiGoSan(n):
    n = str(n)
    if '7' in n and '5' in n and '3' in n:
        return True
    else:
        return False

=======
Suggestion 3

def check753(n):
    if n < 357:
        return 0
    if n < 375:
        return 1
    if n < 537:
        return 2
    if n < 573:
        return 3
    if n < 735:
        return 4
    if n < 753:
        return 5
    if n < 3357:
        return 6
    if n < 3375:
        return 7
    if n < 3537:
        return 8
    if n < 3557:
        return 9
    if n < 3573:
        return 10
    if n < 3575:
        return 11
    if n < 3577:
        return 12
    return 13

=======
Suggestion 4

def check753(n):
    n = str(n)
    if n.count("7") > 0 and n.count("5") > 0 and n.count("3") > 0:
        return True
    else:
        return False

=======
Suggestion 5

def check_shichigosan(number):
    str_number = str(number)
    if '7' in str_number and '5' in str_number and '3' in str_number:
        return True
    else:
        return False

=======
Suggestion 6

def isSGS(n):
    s = str(n)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if isSGS(i):
        cnt += 1
print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(3, len(str(N))+1):
        for j in ['7', '5', '3']:
            for k in itertools.product(['7', '5', '3'], repeat=i):
                if int(''.join(k)) <= N and j in k and len(set(k)) == 3:
                    count += 1
    print(count)

=======
Suggestion 8

def checkShichiGoSanNumber(num):
    s = str(num)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0

=======
Suggestion 9

def check(n):
    return all([str(n).count(c) > 0 for c in '753'])

N = int(input())
print(sum([check(n) for n in range(357, N+1, 2)]))

=======
Suggestion 10

def check(n):
    return all([n.count(i) >= 1 for i in '753'])
