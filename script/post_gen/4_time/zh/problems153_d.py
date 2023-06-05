Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(H):
    if H == 1:
        return 1
    else:
        return 2 * solve(H // 2) + 1

H = int(input())
print(solve(H))

=======
Suggestion 2

def main():
    H = input()
    H = int(H)
    count = 0
    while 1:
        if H == 1:
            count += 1
            break
        else:
            H = int(H / 2)
            count += 1
    print(count)

=======
Suggestion 3

def get_ans(H):
    if H < 2:
        return 1
    else:
        return 2 * get_ans(H // 2) + 1

H = int(input())
print(get_ans(H))

=======
Suggestion 4

def func(h):
    if h == 1:
        return 1
    elif h == 0:
        return 0
    else:
        return 2*func(h//2) + 1

h = int(input())
print(func(h))

=======
Suggestion 5

def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1

=======
Suggestion 6

def f(n):
    if n == 1:
        return 1
    else:
        return 2*f(n//2)+1

H = int(input())
print(f(H))

=======
Suggestion 7

def f(x):
    if x == 0:
        return 0
    return 2*f(x//2)+1

h = int(input())
print(f(h))

=======
Suggestion 8

def func(h):
    if h == 1:
        return 1
    else:
        return 2 * func(int(h / 2)) + 1

h = int(input())
print(func(h))

=======
Suggestion 9

def solve(h):
    if h == 1:
        return 1
    return 2 * solve(h//2) + 1

h = int(input())
print(solve(h))
