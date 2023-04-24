Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                cnt += 1
    print(cnt)
main()

=======
Suggestion 2

def check(x):
    s = str(x)
    n = len(s)
    for i in range(n//2):
        if s[i] != s[i+n//2]:
            return False
    return True

N = int(input())
ans = 0
for i in range(1,N+1):
    if check(i):
        ans += 1
print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        s = str(i)
        if len(s)%2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            ans += 1
    print(ans)

=======
Suggestion 4

def func(n):
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                ans += 1
    return ans

n = int(input())
print(func(n))

=======
Suggestion 5

def solve():
    N = int(input())
    ans = 0
    for i in range(1, 1000001):
        s = str(i) + str(i)
        if int(s) <= N:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 6

def solve(N):
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                ans += 1
    return ans

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, 11):
        if N >= 10 ** i:
            ans += 9 * 10 ** ((i - 1) // 2)
        else:
            ans += (N - 10 ** (i - 1) + 1) // 2
            break
    print(ans)

=======
Suggestion 8

def is_even_digit(x):
    return len(str(x)) % 2 == 0

=======
Suggestion 9

def is_even_digit(s):
    return len(s) % 2 == 0
