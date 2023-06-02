Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(3, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    print(count)

=======
Suggestion 2

def is753(n):
    s = str(n)
    if s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 3

def is753(num):
    if num % 10 == 3:
        return True
    if num % 10 == 5:
        return True
    if num % 10 == 7:
        return True
    return False

=======
Suggestion 4

def is753(n):
    s = str(n)
    return s.count('7') > 0 and s.count('5') > 0 and s.count('3') > 0

=======
Suggestion 5

def solve(n):
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count

n = int(input())
print(solve(n))

=======
Suggestion 6

def is753(n):
    if '7' in str(n) and '5' in str(n) and '3' in str(n):
        return True
    else:
        return False

=======
Suggestion 7

def is753(num):
    num_str = str(num)
    if num_str.count('7') > 0 and num_str.count('5') > 0 and num_str.count('3') > 0:
        return True
    else:
        return False

=======
Suggestion 8

def is753(num):
    if num < 357:
        return False
    if num % 10 == 7:
        return True
    if num % 10 == 5:
        return True
    if num % 10 == 3:
        return True
    return False

=======
Suggestion 9

def check753(n):
    n_str = str(n)
    return (n_str.count('7') > 0 and n_str.count('5') > 0 and n_str.count('3') > 0)

=======
Suggestion 10

def is753(num):
    if "7" in str(num) and "5" in str(num) and "3" in str(num):
        return True
    else:
        return False
