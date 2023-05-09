Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n, a, b = map(int, input().split())
    s = input()
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                dp[j+1] = min(dp[j+1], dp[i] + a)
            else:
                dp[j+1] = min(dp[j+1], dp[i] + b)
    print(dp[n])

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    S = input()
    count = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            if S[i] == 'a':
                count += A
            else:
                count += B
        else:
            if S[i] != 'a':
                count += min(A, B)
    if N%2 == 1:
        if S[N//2] != 'a':
            count += min(A, B)
    print(count)

=======
Suggestion 3

def main():
    n, a, b = map(int, input().split())
    s = input()
    c = 0
    d = 0
    for i in range(n):
        if s[i] != s[n - i - 1]:
            c += 1
        elif s[i] == s[n - i - 1] and i < n // 2:
            d += 1
    if c == 0:
        print(0)
    elif c == 1:
        print(a)
    elif c == 2:
        print(min(a, b))
    else:
        if a > b:
            print(b * (c - 1) + a)
        else:
            print(b * c)

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    s = input()
    res = 0
    for i in range(n):
        if s[i] == s[n - i - 1]:
            continue
        elif s[i] == 'a':
            if s[n - i - 1] == 'b':
                res += a
            else:
                res += b
        elif s[i] == 'b':
            if s[n - i - 1] == 'a':
                res += a
            else:
                res += b
        else:
            if s[n - i - 1] == 'a':
                res += b
            else:
                res += a
    print(res)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()
    print('')

=======
Suggestion 6

def main():
    # Get input here
    n, a, b = map(int, input().strip().split())
    s = input().strip()

    # Calculate result here
    result = 0
    if a < b:
        result += a * n
    else:
        result += b * n

    # Print output here
    print(result)

=======
Suggestion 7

def main():
    n, a, b = map(int, input().split())
    s = input()
    print(s)
    print(n, a, b)
    print(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7])

=======
Suggestion 8

def main():
    N,A,B = map(int,input().split())
    S = input()
    print(S)

=======
Suggestion 9

def palindrome_cost(n, a, b, s):
    is_palindrome = True
    cost = 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            is_palindrome = False
            break
    if is_palindrome:
        return 0
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i] == 'a' or s[n - i - 1] == 'a':
                cost += a
            else:
                cost += b
    return cost
