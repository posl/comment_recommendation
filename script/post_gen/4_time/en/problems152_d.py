Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        i = str(i)
        if i[0] == i[-1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if str(i)[0] == str(i)[-1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
        elif i < 100:
            if i % 11 == 0:
                count += 1
        else:
            if i % 11 == 0:
                count += 2
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i % 10 == 0:
            continue
        else:
            for j in range(1,n+1):
                if j % 10 == 0:
                    continue
                else:
                    if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                        count += 1
    print(count)

=======
Suggestion 7

def main():
    N = input()
    N = int(N)

    ans = 0
    for i in range(1, N + 1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len == 1:
            ans += 1
        else:
            if i_str[0] == i_str[-1]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0

    for i in range(1,n+1):
        if i%10 == 0:
            continue
        else:
            last = int(str(i)[-1])
            first = int(str(i)[0])
            if last == first:
                ans += 1

    print(ans)

=======
Suggestion 9

def count(N):
    if N < 10:
        return N
    else:
        return 9 + count(N-1)

=======
Suggestion 10

def last_digit(n):
    return int(str(n)[-1])
