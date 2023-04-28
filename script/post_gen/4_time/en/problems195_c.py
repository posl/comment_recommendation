Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n < 1000:
        print(0)
    elif n < 1000000:
        print(n - 999)
    elif n < 1000000000:
        print(999000 + 2 * (n - 999999))
    elif n < 1000000000000:
        print(999000 + 2 * 999000000 + 3 * (n - 999999999))
    elif n < 1000000000000000:
        print(999000 + 2 * 999000000 + 3 * 999000000000 + 4 * (n - 999999999999))
    else:
        print(999000 + 2 * 999000000 + 3 * 999000000000 + 4 * 999000000000000 + 5 * (n - 999999999999999))

=======
Suggestion 2

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
Suggestion 3

def main():
    N = input()
    N = int(N)
    if N < 1000:
        print(0)
    elif N < 1000000:
        print(N-999)
    elif N < 1000000000:
        print((N-999999)*2+999000)
    elif N < 1000000000000:
        print((N-999999999)*3+1998000000)
    elif N < 1000000000000000:
        print((N-999999999999)*4+2999700000000)
    elif N < 1000000000000000000:
        print((N-999999999999999)*5+3999960000000000)
    elif N < 1000000000000000000000:
        print((N-999999999999999999)*6+4999997000000000000)
    elif N < 1000000000000000000000000:
        print((N-999999999999999999999)*7+5999999400000000000000)
    elif N < 1000000000000000000000000000:
        print((N-999999999999999999999999)*8+6999999940000000000000000)
    elif N < 1000000000000000000000000000000:
        print((N-999999999999999999999999999)*9+7999999995000000000000000000)
    elif

=======
Suggestion 4

def count_comma(n):
    if n < 1000:
        return 0
    elif n < 1000000:
        return n - 999
    elif n < 1000000000:
        return 2 * (n - 999999) + 999000
    elif n < 1000000000000:
        return 3 * (n - 999999999) + 2 * 999000000 + 999000
    elif n < 1000000000000000:
        return 4 * (n - 999999999999) + 3 * 999000000000 + 2 * 999000000 + 999000
    else:
        return 5 * (n - 999999999999999) + 4 * 999000000000000 + 3 * 999000000000 + 2 * 999000000 + 999000

print(count_comma(int(input())))

=======
Suggestion 5

def main():
    N = int(input())
    if N < 1000:
        print(0)
        return
    if N < 10**6:
        print(N-999)
        return
    if N < 10**9:
        print(2*(N-10**6+1)+10**3-999)
        return
    if N < 10**12:
        print(3*(N-10**9+1)+2*(10**6-10**3+1)+10**3-999)
        return
    if N < 10**15:
        print(4*(N-10**12+1)+3*(10**9-10**6+1)+2*(10**6-10**3+1)+10**3-999)
        return

=======
Suggestion 6

def main():
    N = input()
    N = int(N)
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
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, len(str(N))+1):
        if i % 3 == 0:
            count += N - (10 ** i - 1) + 1
    print(count)
main()

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,16):
        if N >= 10**i:
            ans += (N - 10**(i-1) + 1) - 10**(i-1)
        else:
            ans += max(0, N - 10**(i-1) + 1)
        if i % 3 == 0:
            ans += 10**(i-1)
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    
    if n < 1000:
        print(0)
        return
    
    if n < 1000000:
        print((n-999)//1000)
        return
    
    if n < 1000000000:
        print(999 + 2*((n-999999)//1000000))
        return
    
    if n < 1000000000000:
        print(999 + 2*999000 + 3*((n-999999999)//1000000000))
        return
    
    if n < 1000000000000000:
        print(999 + 2*999000 + 3*999000000 + 4*((n-999999999999)//1000000000000))
        return
    
    if n < 1000000000000000000:
        print(999 + 2*999000 + 3*999000000 + 4*999000000000 + 5*((n-999999999999999)//1000000000000000))
        return
    
    if n < 1000000000000000000000:
        print(999 + 2*999000 + 3*999000000 + 4*999000000000 + 5*999000000000000 + 6*((n-999999999999999999)//1000000000000000000))
        return
    
    print(999 + 2*999000 + 3*999000000 + 4*999000000000 + 5*999000000000000 + 6*999000000000000000 + 7*((n-999999999999999999999)//1000000000000000000))
    return

solve()

=======
Suggestion 10

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_comma = int((N_len-1)/3)
    N_comma_total = N_comma * 2
    if N_len % 3 == 0:
        N_comma_total += 1
    elif N_len % 3 == 1:
        N_comma_total += 1
    elif N_len % 3 == 2:
        N_comma_total += 2
    print(N_comma_total)
