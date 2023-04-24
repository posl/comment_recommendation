Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    s = input()
    c = 0
    d = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            c += 1
    if c == 0:
        print(0)
    elif c == 1:
        print(a)
    else:
        print(a*(c-1)+b)

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] == s[-(i+1)]:
            continue
        elif s[i] == 'a' and s[-(i+1)] != 'a':
            ans += a
        elif s[i] != 'a' and s[-(i+1)] == 'a':
            ans += a
        elif s[i] == 'b' and s[-(i+1)] != 'b':
            ans += b
        elif s[i] != 'b' and s[-(i+1)] == 'b':
            ans += b
        else:
            ans = -1
            break
    else:
        if s[n//2] != 'a' and s[n//2] != 'b':
            ans += min(a, b)
    print(ans)

=======
Suggestion 3

def solve():
    N, A, B = map(int, input().split())
    S = input()
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        dp[i] = dp[i-1] + A
        for j in range(1, i+1):
            if S[i-1] != S[i-j]:
                dp[i] = min(dp[i], dp[i-j] + B)
            else:
                dp[i] = min(dp[i], dp[i-j])
    print(dp[N])

=======
Suggestion 4

def solve():
    n, a, b = map(int, input().split())
    s = input()
    dp = [float("inf")] * (n+1)
    dp[0] = 0
    for i in range(n):
        dp[i+1] = min(dp[i+1], dp[i]+a)
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[j+1] = min(dp[j+1], dp[i]+b)
    print(dp[n])

=======
Suggestion 5

def is_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[-1]:
        return is_palindrome(str[1:-1])
    else:
        return False

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    S = input()

    cnt = 0
    for i in range(N//2):
        if S[i] != S[N-i-1]:
            if S[i] == 'a' and S[N-i-1] == 'b':
                cnt += A
            elif S[i] == 'b' and S[N-i-1] == 'a':
                cnt += A
            elif S[i] == 'c' and S[N-i-1] == 'd':
                cnt += A
            elif S[i] == 'd' and S[N-i-1] == 'c':
                cnt += A
            elif S[i] == 'e' and S[N-i-1] == 'f':
                cnt += A
            elif S[i] == 'f' and S[N-i-1] == 'e':
                cnt += A
            elif S[i] == 'g' and S[N-i-1] == 'h':
                cnt += A
            elif S[i] == 'h' and S[N-i-1] == 'g':
                cnt += A
            elif S[i] == 'i' and S[N-i-1] == 'j':
                cnt += A
            elif S[i] == 'j' and S[N-i-1] == 'i':
                cnt += A
            elif S[i] == 'k' and S[N-i-1] == 'l':
                cnt += A
            elif S[i] == 'l' and S[N-i-1] == 'k':
                cnt += A
            elif S[i] == 'm' and S[N-i-1] == 'n':
                cnt += A
            elif S[i] == 'n' and S[N-i-1] == 'm':
                cnt += A
            elif S[i] == 'o' and S[N-i-1] == 'p':
                cnt += A
            elif S[i] == 'p' and S[N-i-1] == 'o':
                cnt += A
            elif S[i] == 'q' and S[N-i-1] == 'r':
                cnt += A
            elif S[i] == 'r' and S[N-i-1] == 'q':
                cnt += A
            elif

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    S = input()
    cnt = 0
    cnt_b = 0
    for i in range(N):
        if S[i] == S[N-i-1]:
            cnt += 1
        else:
            cnt_b += 1
    if cnt == N:
        print(0)
    elif cnt_b == 0:
        print(A*N)
    else:
        cnt_b = (cnt_b + 1) // 2
        print(A*N + B*cnt_b)

=======
Suggestion 8

def main():
    inputStr = input()
    inputList = inputStr.split(' ')
    n = int(inputList[0])
    a = int(inputList[1])
    b = int(inputList[2])
    s = input()
    print(n*a+b)

=======
Suggestion 9

def problems286_c():
    N, A, B = map(int, input().split())
    S = input()
    T = S[::-1]
    dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N+1):
        for j in range(N+1):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + A)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + A)
            if i > 0 and j > 0:
                if S[i-1] == T[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + B)
    print(dp[N][N])

=======
Suggestion 10

def process():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == s[n - i - 1]:
            continue
        elif s[i] == 'a':
            ans += a
        elif s[i] == 'b':
            ans += b
        elif s[n - i - 1] == 'a':
            ans += a
        elif s[n - i - 1] == 'b':
            ans += b
        else:
            print(-1)
            return
    if ans % 2 == 0:
        print(ans // 2)
    else:
        print(ans // 2 + 1)
