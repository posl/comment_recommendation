Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v, t, s, d = map(int, input().split())
    if v * t <= d <= v * s:
        print('No')
    else:
        print('Yes')

=======
Suggestion 2

def main():
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    V, T, S, D = map(int, input().split())
    if T * V <= D <= S * V:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    v, t, s, d = [int(i) for i in input().split()]
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    v, t, s, d = map(int, input().split())
    if (d/v >= t) and (d/v <= s):
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def get_input():
    return [int(x) for x in input().split()]
