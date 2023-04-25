Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if "7" not in str(i) and "7" not in oct(i)[2:]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if not '7' in str(i) and not '7' in oct(i)[2:]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if '7' in str(i) or '7' in str(oct(i))[2:]:
            continue
        else:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    a = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            a += 1
    print(a)

=======
Suggestion 9

def is_valid(n):
    if '7' in str(n):
        return False
    if '7' in oct(n):
        return False
    return True

=======
Suggestion 10

def main():
    N = int(input())
    print(N - sum([N // 10**d * 2 - (N // 10**(d+1) * 2) for d in range(6)]) - sum([N // 8**d * 2 - (N // 8**(d+1) * 2) for d in range(6)]) + sum([N // (8**d * 10**d) * 2 - (N // (8**(d+1) * 10**(d+1)) * 2) for d in range(6)]))
