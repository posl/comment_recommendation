Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in str(oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if not ("7" in str(i) or "7" in oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if str(i).find('7') == -1 and oct(i).find('7') == -1:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in (str(i) + oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in str(oct(i)):
            continue
        else:
            result += 1
    print(result)

=======
Suggestion 10

def check(num):
    while num > 0:
        if num % 10 == 7:
            return False
        num //= 10
    return True

N = int(input())

ans = 0
for num in range(1, N+1):
    if check(num) and check(int(oct(num))):
        ans += 1
print(ans)
