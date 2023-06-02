Synthesizing 10/10 solutions

=======
Suggestion 1

def count_seven(n):
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 3

def solve(n):
    count = 0
    for i in range(1, n+1):
        if "7" in str(i) or "7" in oct(i):
            continue
        count += 1
    return count

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if "7" in str(i) or "7" in oct(i):
            continue
        else:
            count += 1
    print(count)

=======
Suggestion 5

def is7(num):
    if num % 7 == 0:
        return True
    while num != 0:
        if num % 10 == 7:
            return True
        num = num // 10
    return False

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        count += 1
    print(count)

=======
Suggestion 8

def is_contain_7(i):
    if i % 10 == 7:
        return True
    if i // 10 == 7:
        return True
    return False

=======
Suggestion 9

def is_valid(num):
    for i in range(len(str(num))):
        if str(num)[i] == '7':
            return False
    for i in range(len(oct(num))):
        if oct(num)[i] == '7':
            return False
    return True

=======
Suggestion 10

def check(num, base):
    while num > 0:
        if num % base == 7:
            return False
        num /= base
    return True
