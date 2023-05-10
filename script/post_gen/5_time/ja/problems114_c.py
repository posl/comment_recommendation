Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if "7" in str(i) and "5" in str(i) and "3" in str(i):
            count += 1
    print(count)

=======
Suggestion 2

def is753(n):
    if n % 10 == 3:
        return True
    elif n % 10 == 5:
        return True
    elif n % 10 == 7:
        return True
    else:
        return False

=======
Suggestion 3

def f(n, s):
    if n > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += f(10 * n + int(c), s + c)
    return ret

N = int(input())
print(f(0, ''))

=======
Suggestion 4

def is753(num):
    if num == 0:
        return False
    if num % 10 == 7 or num % 10 == 5 or num % 10 == 3:
        return True
    return is753(num // 10)

=======
Suggestion 5

def check(n):
    s = str(n)
    return s.count("7") >= 1 and s.count("5") >= 1 and s.count("3") >= 1 and s.count("7") + s.count("5") + s.count("3") == len(s)

=======
Suggestion 6

def main():
    N = input()
    cnt = 0
    for i in range(3, len(N)+1):
        for j in range(len(N)+1-i):
            if int(N[j:j+i])%3 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if "7" in str(i) and "5" in str(i) and "3" in str(i):
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0

    for i in range(1, N + 1):
        if len(set(str(i)) - set(['7', '5', '3'])) == 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def is753(n):
    n_str = str(n)
    return '7' in n_str and '5' in n_str and '3' in n_str and n_str.count('7') + n_str.count('5') + n_str.count('3') == len(n_str)

=======
Suggestion 10

def is753(n):
    s = str(n)
    return s.count('7') and s.count('5') and s.count('3') and not s.count('0') and not s.count('1') and not s.count('2') and not s.count('4') and not s.count('6') and not s.count('8') and not s.count('9')

n = int(input())
ans = 0
for i in range(1, n+1):
    if is753(i):
        ans += 1
print(ans)
