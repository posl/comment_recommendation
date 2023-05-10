Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def comma_count(n):
    if n < 1000:
        return 0
    elif n < 1000000:
        return n - 999
    elif n < 1000000000:
        return 999000 + 2 * (n - 999999)
    elif n < 1000000000000:
        return 999000000 + 3 * (n - 999999999)
    elif n < 1000000000000000:
        return 999000000000 + 4 * (n - 999999999999)
    else:
        return 999000000000000 + 5 * (n - 999999999999999)

n = int(input())
print(comma_count(n))

=======
Suggestion 2

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    if N_len <= 3:
        print(0)
        return
    if N_len % 3 == 0:
        print((N_len // 3) - 1)
    else:
        print(N_len // 3)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    if N >= 1000:
        ans += N-999
    if N >= 1000000:
        ans += N-999999
    if N >= 1000000000:
        ans += N-999999999
    if N >= 1000000000000:
        ans += N-999999999999
    if N >= 1000000000000000:
        ans += N-999999999999999
    print(ans)
    return 0

=======
Suggestion 4

def main():
    # input
    N = int(input())

    # compute
    ans = 0
    if N >= 10**3:
        ans += N - 10**3 + 1
    if N >= 10**6:
        ans += N - 10**6 + 1
    if N >= 10**9:
        ans += N - 10**9 + 1
    if N >= 10**12:
        ans += N - 10**12 + 1
    if N >= 10**15:
        ans += N - 10**15 + 1

    # output
    print(ans)

=======
Suggestion 5

def comma_count(n):
    ans = 0
    for i in range(1, len(n)):
        ans += 9 * 10 ** (i - 1) * i
    ans += (int(n) - 10 ** (len(n) - 1) + 1) * len(n)
    return ans

n = input()
print(comma_count(n))

=======
Suggestion 6

def comma_count(n):
    n_str = str(n)
    n_len = len(n_str)
    count = 0

    for i in range(1, n_len+1):
        if i % 3 == 0 and i != n_len:
            count += 1

    return count

n = int(input())
count = 0

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    if N >= 1000:
        ans += N - 999
    if N >= 1000000:
        ans += N - 999999
    if N >= 1000000000:
        ans += N - 999999999
    if N >= 1000000000000:
        ans += N - 999999999999
    if N >= 1000000000000000:
        ans += N - 999999999999999
    print(ans)

=======
Suggestion 8

def count_comma(n):
    s = str(n)
    l = len(s)
    if l < 4:
        return 0
    elif l < 7:
        return int(s[:l-3]) - 1
    elif l < 10:
        return int(s[:l-6]) + 999999
    elif l < 13:
        return int(s[:l-9]) + 1999998
    elif l < 16:
        return int(s[:l-12]) + 2999997
    else:
        return 2999997 + 9000000 * (int(s[0]) - 2)

n = int(input())
print(count_comma(n))

=======
Suggestion 9

def main():
    n = int(input())
    if n < 1000:
        print(0)
        return
    ans = 0
    for i in range(1, 16):
        if 1000**i <= n:
            ans += n - 1000**i + 1
    print(ans)
