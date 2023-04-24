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
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if "7" not in str(i) and "7" not in oct(i)[2:]:
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
    ans = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        count += 1
    print(count)

main()

=======
Suggestion 8

def is_seven(num):
    if '7' in str(num) or '7' in oct(num)[2:]:
        return True
    return False
