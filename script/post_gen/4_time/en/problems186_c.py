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
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if "7" not in str(i) and "7" not in oct(i)[2:]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N + 1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if "7" not in str(i) and "7" not in oct(i)[2:]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if ('7' not in str(i)) and ('7' not in oct(i)[2:]):
            count += 1
    print(count)

=======
Suggestion 7

def check(n):
    if '7' in str(n):
        return False
    if '7' in oct(n):
        return False
    return True

=======
Suggestion 8

def is_seven(n):
    if '7' in str(n):
        return True
    else:
        return False
