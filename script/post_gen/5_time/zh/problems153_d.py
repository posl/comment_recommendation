Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solution(h):
    if h == 1:
        return 1
    return solution(h//2)*2+1

=======
Suggestion 2

def f(h):
    if h == 1:
        return 1
    else:
        return 2 * f(h // 2) + 1

h = int(input())
print(f(h))

=======
Suggestion 3

def solve(H):
    if H == 1:
        return 1
    else:
        return 2*solve(H//2)+1

=======
Suggestion 4

def solve():
    h = int(input())
    print(2**(h.bit_length())-1)

=======
Suggestion 5

def solve(H):
    if H == 1:
        return 1
    else:
        return 2*solve(H//2)+1

H = int(input())
print(solve(H))

=======
Suggestion 6

def f(x):
    if x == 1:
        return 1
    else:
        return 2*f(x//2)+1

H = int(input())
print(f(H))

=======
Suggestion 7

def solve(h):
    if h == 1:
        return 1
    else:
        return 2*solve(h//2)+1

h = int(input())
print(solve(h))

=======
Suggestion 8

def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1

=======
Suggestion 9

def f(h):
    if h == 1:
        return 1
    else:
        return 2 * f(h // 2) + 1
