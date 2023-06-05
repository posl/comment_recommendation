Synthesizing 10/10 solutions

=======
Suggestion 1

def seven_count(n):
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

=======
Suggestion 2

def is_contain_7(num):
    if num % 10 == 7:
        return True
    elif num > 10:
        return is_contain_7(num // 10)
    else:
        return False

=======
Suggestion 3

def is_contain_seven(num, base):
    while num > 0:
        if num % base == 7:
            return True
        num //= base
    return False

=======
Suggestion 4

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        if '7' in str(i) or '7' in oct(i):
            cnt += 1
    print(n - cnt)
    return 0

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i):
            count += 1
    print(n - count)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0

    for i in range(1, n + 1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 9

def is_contain_7(num):
    if str(num).find('7') != -1:
        return True
    elif str(oct(num)).find('7') != -1:
        return True
    else:
        return False

=======
Suggestion 10

def is_7_in_num(num, base=10):
    if base == 10:
        return str(num).find('7') >= 0
    elif base == 8:
        while num > 0:
            if num % 8 == 7:
                return True
            num //= 8
        return False
