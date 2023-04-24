Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if "7" not in str(i) and "7" not in oct(i):
            ans += 1
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in oct(i):
            cnt += 1
    print(cnt)
main()

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if not "7" in str(i) and not "7" in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if not ('7' in str(i) or '7' in oct(i)):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if "7" in str(i) or "7" in str(oct(i)):
            cnt += 1
    print(N - cnt)

=======
Suggestion 8

def count_7(n):
    s = str(n)
    if "7" in s:
        return True
    else:
        return False
