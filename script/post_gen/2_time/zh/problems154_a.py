Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    if x == 1:
        return 1
    else:
        return 2 * f(x // 2) + 1

H = int(input())
print(f(H))

=======
Suggestion 2

def get_answer(h):
    if h == 1:
        return 1
    else:
        return 2*get_answer(h//2) + 1

=======
Suggestion 3

def main():
    H = int(input())
    print(int(H.bit_length()))

=======
Suggestion 4

def solve(h):
  if h == 1:
    return 1
  elif h % 2 == 0:
    return solve(h//2) * 2 + 1
  else:
    return solve(h//2) * 2 + 1

print(solve(int(input())))

=======
Suggestion 5

def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1
print(solve(int(input())))

=======
Suggestion 6

def attack(h):
    if h == 1:
        return 1
    else:
        return 2 * attack(h // 2) + 1

=======
Suggestion 7

def solve(h):
    if h == 1:
        return 1
    else:
        return 2 * solve(h // 2) + 1

h = int(input())
print(solve(h))

=======
Suggestion 8

def solve():
    H = int(input())
    print(2**(H.bit_length())-1)

=======
Suggestion 9

def calc(n):
    if n == 1:
        return 1
    else:
        return 2 * calc(n//2) + 1

H = int(input())
print(calc(H))
