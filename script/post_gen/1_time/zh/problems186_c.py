Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 2

def is_contain_seven(num, base):
    while num > 0:
        if num % base == 7:
            return True
        num = num // base
    return False

=======
Suggestion 3

def main():
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        if str(i).find('7') >= 0:
            continue
        if str(oct(i)).find('7') >= 0:
            continue
        result += 1
    print(result)

main()

=======
Suggestion 4

def check_seven(n):
    if '7' in str(n):
        return True
    else:
        return False

N = int(input())
count = 0
for i in range(1,N+1):
    if check_seven(i):
        continue
    else:
        if check_seven(oct(i)):
            continue
        else:
            count += 1
print(count)

=======
Suggestion 5

def is_contain_seven(n):
    if '7' in str(n):
        return True
    else:
        return False

=======
Suggestion 6

def check_seven(num):
    while num > 0:
        if num % 10 == 7:
            return True
        num = num // 10
    return False

=======
Suggestion 7

def is_contain_seven(n):
    if n%10 == 7:
        return True
    elif n//10 == 0:
        return False
    else:
        return is_contain_seven(n//10)

=======
Suggestion 8

def count_dec(num):
    count = 0
    for i in range(1, num+1):
        if '7' in str(i):
            count += 1
    return count

=======
Suggestion 9

def f(n):
    s = 0
    for i in range(1,n+1):
        if '7' in str(i) or '7' in oct(i):
            s += 1
    return n-s

N = int(input())
print(f(N))

=======
Suggestion 10

def count(n):
    count=0
    for i in range(1,n+1):
        if not '7' in str(i) and not '7' in oct(i):
            count+=1
    return count

print(count(100000))
