Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(H):
    if H == 1:
        return 1
    else:
        return 2 * solve(H // 2) + 1

=======
Suggestion 2

def func(h):
    if h == 1:
        return 1
    else:
        return 2*func(h//2) + 1
h = int(input())
print(func(h))

=======
Suggestion 3

def attack(num):
    if num == 1:
        return 1
    elif num % 2 == 0:
        return 2 * attack(num / 2) + 1
    else:
        return 2 * attack((num - 1) / 2) + 1

H = int(input())
print(attack(H))

=======
Suggestion 4

def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1

print(solve(int(input())))

=======
Suggestion 5

def cal_attack_times(hp):
    if hp == 1:
        return 1
    else:
        return 2 * cal_attack_times(hp // 2) + 1

=======
Suggestion 6

def main():
    H = int(input())
    count = 0
    while H > 0:
        count += 1
        H //= 2
    print(2**count - 1)

=======
Suggestion 7

def func(h):
    if h == 1:
        return 1
    elif h == 2:
        return 3
    else:
        return 2 * func(h // 2) + 1

h = int(input())
print(func(h))

=======
Suggestion 8

def get_min_attack_times(h):
    if h == 1:
        return 1
    elif h == 2:
        return 3
    else:
        i = 0
        while h > 0:
            i += 1
            h = h // 2
        return 2 ** i - 1

=======
Suggestion 9

def solve(h):
    if h == 1:
        return 1
    else:
        return 1 + 2 * solve(h // 2)
