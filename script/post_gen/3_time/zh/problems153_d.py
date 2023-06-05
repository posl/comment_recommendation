Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(h):
    if h == 1:
        return 1
    else:
        return solve(h//2)*2+1

=======
Suggestion 2

def f(H):
    if H == 1:
        return 1
    else:
        return 2*f(H//2)+1

H = int(input())
print(f(H))

=======
Suggestion 3

def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1

h = int(input())
print(solve(h))

=======
Suggestion 4

def solve(h):
    res = 0
    while h > 0:
        res += h
        h //= 2
    return res

=======
Suggestion 5

def f(h):
    if h == 1:
        return 1
    else:
        return 2*f(h//2) + 1

h = int(input())
print(f(h))

=======
Suggestion 6

def main():
    h = int(input())
    count = 1
    while h > 1:
        count = count * 2
        h = h // 2
    print(count)

=======
Suggestion 7

def solve():
    H = int(input())
    count = 0
    while H > 0:
        count += 1
        H //= 2
    print(2 ** count - 1)

=======
Suggestion 8

def f(x):
    if x == 1:
        return 1
    else:
        return 2 * f(x//2) + 1

H = int(input())
print(f(H))

=======
Suggestion 9

def func(h):
    if h==1:
        return 1
    else:
        return 2*func(h//2)+1

h=int(input())
print(func(h))
