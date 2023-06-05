Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    # 1~999
    if n_len <= 3:
        print(0)
        return
    # 1000~999999
    elif 3 < n_len <= 6:
        print(n_len - 3)
        return
    # 1000000~999999999
    elif 6 < n_len <= 9:
        print((n_len - 3) * 2 + 3)
        return
    # 1000000000~999999999999
    elif 9 < n_len <= 12:
        print((n_len - 3) * 3 + 3)
        return
    # 1000000000000~999999999999999
    elif 12 < n_len <= 15:
        print((n_len - 3) * 4 + 3)
        return
    # 1000000000000000~999999999999999999
    elif 15 < n_len <= 18:
        print((n_len - 3) * 5 + 3)
        return
    # 1000000000000000000~999999999999999999999
    elif 18 < n_len <= 21:
        print((n_len - 3) * 6 + 3)
        return
    # 1000000000000000000000~999999999999999999999999
    elif 21 < n_len <= 24:
        print((n_len - 3) * 7 + 3)
        return
    # 1000000000000000000000000~999999999999999999999999999
    elif 24 < n_len <= 27:
        print((n_len - 3) * 8 + 3)
        return
    # 1000000000000000000

=======
Suggestion 2

def main():
    n = int(input())
    cnt = 0
    for i in range(1, 15):
        if n < 10 ** i:
            cnt += (n - 10 ** (i - 1) + 1) * i
            break
        else:
            cnt += (10 ** i - 10 ** (i - 1)) * i
    print(cnt)

=======
Suggestion 3

def solve(n):
    s = str(n)
    l = len(s)
    cnt = 0
    for i in range(3, l+1, 3):
        cnt += (l-i+1) * 10**(i//3-1)
    cnt += (n - 10**(l-1) + 1) * (l//3)
    return cnt

=======
Suggestion 4

def f(n):
    if n < 1000:
        return 0
    if n < 1000000:
        return n // 1000
    if n < 1000000000:
        return n // 1000000 + 999
    if n < 1000000000000:
        return n // 1000000000 + 1998
    if n < 1000000000000000:
        return n // 1000000000000 + 2997
    if n < 1000000000000000000:
        return n // 1000000000000000 + 3996
    return n // 1000000000000000000 + 4995

=======
Suggestion 5

def main():
    n = int(input())
    digit = 0
    for i in range(1, 16):
        if n < 10 ** i:
            digit = i
            break
    if digit <= 3:
        print(0)
        return
    elif digit <= 6:
        print(n - 999)
        return
    elif digit <= 9:
        print((n - 999999) * 2 + 999000)
        return
    elif digit <= 12:
        print((n - 999999999) * 3 + 1998000)
        return
    elif digit <= 15:
        print((n - 999999999999) * 4 + 2999700000)
        return
    else:
        print(107730272137364)

=======
Suggestion 6

def get_comma_count(num):
    comma_count = 0
    num_len = len(str(num))
    if num_len <= 3:
        return 0
    else:
        for i in range(1, num_len - 1):
            if i % 3 == 0:
                comma_count += 1
        return comma_count

=======
Suggestion 7

def solve(n):
    if n < 1000:
        return 0
    else:
        s = str(n)
        if len(s) % 3 == 0:
            return len(s) // 3 - 1
        else:
            return len(s) // 3

=======
Suggestion 8

def count_comma(n):
    n_str = str(n)
    n_len = len(n_str)
    if n_len < 4:
        return 0
    else:
        return n_len//3 - 1

=======
Suggestion 9

def solve(n):
    if n <= 999:
        return 0
    elif n <= 999999:
        return n - 999
    elif n <= 999999999:
        return 2 * (n - 999999) + 999000
    elif n <= 999999999999:
        return 3 * (n - 999999999) + 999000000
    elif n <= 999999999999999:
        return 4 * (n - 999999999999) + 999000000000
    else:
        return 5 * (n - 999999999999999) + 999000000000000

n = int(input())
print(solve(n))

=======
Suggestion 10

def count_comma(n):
    if n < 1000:
        return 0
    else:
        return 1 + count_comma(n//1000)
