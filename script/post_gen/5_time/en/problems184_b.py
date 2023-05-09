Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        else:
            if x > 0:
                x -= 1
    print(x)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif x > 0:
            x -= 1
    print(x)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == "o":
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(x+ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for s in S:
        if s == 'o':
            ans += 1
        else:
            ans = max(0, ans - 1)
    print(ans)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    S = input()

    ans = X
    for s in S:
        if s == 'o':
            ans += 1
        else:
            ans = max(0, ans - 1)

    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "o":
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(X+ans)

=======
Suggestion 8

def main():
    # Get input here
    n, x = map(int, input().strip().split())
    s = list(input().strip())
    # Calculate result here
    result = x
    for i in s:
        if i == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    # Print output here
    print(result)
