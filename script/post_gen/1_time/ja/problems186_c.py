Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if "7" not in str(i) and "7" not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i):
            continue
        ans += 1
    print(ans)

main()

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if ('7' not in str(i)) and ('7' not in str(oct(i))):
            ans += 1
    print(ans)

=======
Suggestion 8

def check(n):
    while n > 0:
        if n % 10 == 7:
            return False
        n //= 10
    return True

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if not(str(7) in str(i) or str(7) in oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    #n = 100000
    ans = 0
    for i in range(1,n+1):
        if not("7" in str(i) or "7" in str(oct(i))):
            ans += 1
    print(ans)
