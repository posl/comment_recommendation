Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if not ("7" in str(i) or "7" in oct(i)):
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

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    print(N - (N//10 + N//8 - N//40))

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if "7" not in str(i) and "7" not in str(oct(i)):
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if not "7" in str(i) and not "7" in oct(i):
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if "7" not in str(i) and "7" not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            cnt += 1
    print(cnt)
