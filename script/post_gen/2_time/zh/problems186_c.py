Synthesizing 10/10 solutions

=======
Suggestion 1

def is7(num):
    if num % 10 == 7:
        return True
    else:
        return False

=======
Suggestion 2

def getNums(n):
    count = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if '7' in str(i) or '7' in oct(i):
            count += 1
    print(n-count)

=======
Suggestion 4

def count_num(n):
    count = 0
    for i in range(1, n + 1):
        if '7' in str(i) or '7' in oct(i):
            pass
        else:
            count += 1
    return count

=======
Suggestion 5

def count7(n):
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

=======
Suggestion 6

def func(n):
    count = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

func(100000)

=======
Suggestion 7

def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            result += 1
    print(result)

=======
Suggestion 8

def seven_count(n):
    count = 0
    for i in range(n+1):
        if str(i).count('7') + oct(i).count('7') == 0:
            count += 1
    return count

=======
Suggestion 9

def count7(num):
    count = 0
    for i in range(1,num+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    return count

=======
Suggestion 10

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)
