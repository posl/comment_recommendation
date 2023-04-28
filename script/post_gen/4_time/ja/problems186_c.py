Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if "7" not in str(i) and "7" not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        if "7" not in str(i) and "7" not in oct(i):
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i):
            ans += 1
    print(n - ans)
main()

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        if '7' not in str(i+1) and '7' not in oct(i+1):
            ans += 1
    print(ans)
main()

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if not "7" in str(i) and not "7" in str(oct(i)):
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())

    ans = 0
    for i in range(1, N + 1):
        if "7" in str(i):
            continue
        if "7" in str(oct(i)):
            continue
        ans += 1

    print(ans)

=======
Suggestion 10

def num_of_7(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] == '7':
            return 1
    return 0

n = int(input())
ans = 0
for i in range(1, n+1):
    if num_of_7(i) == 0 and num_of_7(int(oct(i)[2:])) == 0:
        ans += 1
print(ans)
