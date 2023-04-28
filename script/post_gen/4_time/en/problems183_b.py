Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))

=======
Suggestion 2

def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    print((s_x * g_y + g_x * s_y) / (s_y + g_y))

=======
Suggestion 3

def main():
    S_x, S_y, G_x, G_y = [int(x) for x in input().split()]
    print((S_x*G_y + G_x*S_y)/(S_y + G_y))

=======
Suggestion 4

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y+G_x*S_y)/(S_y+G_y))

solve()

=======
Suggestion 5

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y+G_y*S_x)/(S_y+G_y))

=======
Suggestion 6

def main():
    from sys import stdin
    from math import atan2, degrees, pi
    from decimal import Decimal, getcontext
    getcontext().prec = 15
    S_x, S_y, G_x, G_y = map(int, stdin.readline().split())
    print(Decimal(S_x + G_x) / 2)
