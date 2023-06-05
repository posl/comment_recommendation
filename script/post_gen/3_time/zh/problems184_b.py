Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n, x = map(int, input().split())
    s = input()
    return n, x, s

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == 'o':
            count += 1
        else:
            if count > 0:
                count -= 1
    print(x + count)

main()

=======
Suggestion 3

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
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    sum = x
    for i in range(n):
        if s[i] == 'o':
            sum += 1
        elif s[i] == 'x' and sum > 0:
            sum -= 1
    print(sum)

=======
Suggestion 5

def get_point(n, x, s):
    result = x
    for i in range(n):
        if s[i] == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    return result

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == "o":
            ans += 1
        else:
            ans = max(0, ans - 1)
    print(ans)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'o':
            ans += 1
        elif s[i] == 'x' and ans > 0:
            ans -= 1
    print(ans)

=======
Suggestion 8

def get_result(n, x, s):
    result = x
    for i in range(n):
        if s[i] == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    return result

=======
Suggestion 9

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
