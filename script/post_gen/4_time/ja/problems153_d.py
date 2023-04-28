Synthesizing 10/10 solutions

=======
Suggestion 1

def f(h):
    if h == 1:
        return 1
    else:
        return 2 * f(h // 2) + 1

h = int(input())
print(f(h))

=======
Suggestion 2

def main():
    h = int(input())
    count = 0
    while h > 0:
        count += 1
        h //= 2
    print(2 ** count - 1)

=======
Suggestion 3

def solve(H):
    if H == 1:
        return 1
    else:
        return 1 + 2*solve(H//2)

H = int(input())
print(solve(H))

=======
Suggestion 4

def calc_attack_count(h):
    if h == 1:
        return 1
    else:
        return 2 * calc_attack_count(h // 2) + 1

h = int(input())
print(calc_attack_count(h))

=======
Suggestion 5

def solve():
    H = int(input())
    cnt = 0
    while H > 0:
        H = H // 2
        cnt += 1
    print(2 ** cnt - 1)

=======
Suggestion 6

def attack(h):
    if h == 1:
        return 1
    else:
        return attack(h//2) * 2 + 1

h = int(input())
print(attack(h))

=======
Suggestion 7

def f(x):
    if x == 1:
        return 1
    else:
        return f(x//2)*2+1

h = int(input())
print(f(h))

=======
Suggestion 8

def solve():
    H = int(input())
    ans = 0
    while H > 0:
        H = H // 2
        ans += 1
    print(2**ans - 1)

=======
Suggestion 9

def calc_attack_times(H):
    if H == 1:
        return 1
    else:
        return 1 + 2 * calc_attack_times(H // 2)

H = int(input())
print(calc_attack_times(H))

=======
Suggestion 10

def solve(H):
    if H == 1:
        return 1
    else:
        return 1 + 2*solve(H // 2)
