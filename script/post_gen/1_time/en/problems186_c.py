Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    c = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            c += 1
    print(c)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        else:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(n+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            count += 1
    print(count)
