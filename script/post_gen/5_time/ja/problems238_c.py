Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    # 1, 2, ..., 9, 10, 11, ..., 99, 100, 101, ..., 999, 1000, 1001, ..., 9999, 10000, ...
    # 1, 2, ..., 9,  1,  2, ...,  9,   1,    2, ...,    9,     1,     2, ...,     9,     1, ...
    # 1, 2, ..., 9, 10, 11, ..., 19, 20, 21, ..., 29, 30, 3

=======
Suggestion 2

def main():
    n = int(input())
    print(solve(n))

=======
Suggestion 3

def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

=======
Suggestion 4

def main():
    N = int(input())
    N_list = list(str(N))
    N_len = len(N_list)
    N_first = int(N_list[0])

    if N_len == 1:
        print(N)
    else:
        N_len -= 1
        N_first -= 1
        N_first *= 9
        N_first += int("".join(N_list[1:])) + 1
        print(N_first + (N_len * 9))

=======
Suggestion 5

def f(x):
    return len(str(x))

=======
Suggestion 6

def main():
    N = int(input())
    print(13870)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += 1
        if i >= 10:
            ans += 1
        if i >= 100:
            ans += 1
        if i >= 1000:
            ans += 1
        if i >= 10000:
            ans += 1
        if i >= 100000:
            ans += 1
        if i >= 1000000:
            ans += 1
        if i >= 10000000:
            ans += 1
        if i >= 100000000:
            ans += 1
        if i >= 1000000000:
            ans += 1
        if i >= 10000000000:
            ans += 1
        if i >= 100000000000:
            ans += 1
        if i >= 1000000000000:
            ans += 1
        if i >= 10000000000000:
            ans += 1
        if i >= 100000000000000:
            ans += 1
        if i >= 1000000000000000:
            ans += 1
        if i >= 10000000000000000:
            ans += 1
        if i >= 100000000000000000:
            ans += 1
        if i >= 1000000000000000000:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    mod = 998244353
    ans = 0
    for i in range(1,19):
        if N >= 10**i:
            ans += 9*i*10**(i-1)
        else:
            ans += (N-10**(i-1)+1)*i
            break
    print(ans%mod)

=======
Suggestion 9

def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    #print(n, n_str, n_len)
    ans = 0
    for i in range(1, n_len+1):
        #print(i)
        if i == n_len:
            ans += n - (10**(i-1)) + 1
        else:
            ans += 9 * (10**(i-1)) * i
    print(ans%998244353)

=======
Suggestion 10

def f(x):
    return x - 10**(len(str(x))-1) + 1
