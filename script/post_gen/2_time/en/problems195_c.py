Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * (10**i - 10**(i-1))
    ans += (len(str(N)) * (N - 10**(len(str(N))-1) + 1))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    i = 0
    while N > 0:
        ans += (N + 8) // 1000 * i
        N //= 1000
        i += 1
    print(ans)

=======
Suggestion 3

def solve(n):
    ans = 0
    i = 1
    while i <= n:
        ans += (n - i + 1)
        i *= 1000
    return ans

=======
Suggestion 4

def main():
    N = int(input())
    cnt = 0
    n = 1
    while n <= N:
        cnt += (N-n+1)
        n *= 1000
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**(3*i)))*3
        if N%(10**(3*i)) >= 1000:
            ans += 3
        elif N%(10**(3*i)) >= 100:
            ans += 2
        elif N%(10**(3*i)) >= 10:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    cnt = 1
    while N > 0:
        ans += N // 1000
        N = N // 1000
    print(ans)

=======
Suggestion 7

def countCommas(N):
    if N < 1000:
        return 0
    else:
        return N // 1000 + countCommas(N // 1000)

=======
Suggestion 8

def main():
    N = int(input())
    digit = len(str(N))
    #print(digit)
    if digit <= 3:
        print(0)
    elif digit == 4:
        print(N-999)
    else:
        sum = 0
        for i in range(4,digit+1):
            #print(i)
            sum += 3*(10**(i-1)-10**(i-4))
        print(sum)

=======
Suggestion 9

def count_comma(N):
    N = str(N)
    N_len = len(N)
    cnt = 0
    for i in range(N_len):
        if i % 3 == 0 and i != 0:
            cnt += 1
    return cnt

=======
Suggestion 10

def main():
    N = int(input())
    print(N-1)
