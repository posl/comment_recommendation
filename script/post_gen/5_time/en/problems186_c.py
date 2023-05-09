Synthesizing 10/10 solutions

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
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        if "7" not in str(i) and "7" not in oct(i):
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i):
            count += 1
    print(N-count)

=======
Suggestion 9

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if not ("7" in str(i) or "7" in oct(i)):
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        answer += 1
    print(answer)
