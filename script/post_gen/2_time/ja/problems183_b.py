Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))

=======
Suggestion 2

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y+S_y*G_x)/(S_y+G_y))

=======
Suggestion 3

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y + S_x*G_y) / (S_y + G_y))

=======
Suggestion 4

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y - S_x * G_y) / (G_y - S_y))

=======
Suggestion 5

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(G_x + (G_x - S_x) * G_y / (G_y + S_y))

=======
Suggestion 6

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y + S_x*G_y)/(G_y + S_y))

=======
Suggestion 7

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y+S_x*G_y)/(S_y+G_y))

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y + S_x*G_y)/(S_y + G_y))

=======
Suggestion 9

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    # (G_x - S_x) / (x - S_x) = (G_y - S_y) / (0 - S_y)
    # (G_x - S_x) / (x - S_x) = G_y / S_y
    # (G_x - S_x) / (x - S_x) = G_y / S_y
    # (G_x - S_x) * S_y = (x - S_x) * G_y
    # (G_x - S_x) * S_y + S_x * (x - S_x) = G_y * (G_x - S_x)
    # (G_x - S_x) * S_y + S_x * x - S_x * S_x = G_y * (G_x - S_x)
    # (G_x - S_x) * S_y + S_x * x = G_y * (G_x - S_x) + S_x * S_x
    # (G_x - S_x) * S_y = G_y * (G_x - S_x) + S_x * S_x - S_x * x
    # (G_x - S_x) * S_y = G_y * (G_x - S_x) + S_x * (S_x - x)
    # x = (G_y * (G_x - S_x) + S_x * S_x) / (G_x - S_x + S_y)
    x = (G_y * (G_x - S_x) + S_x * S_x) / (G_x - S_x + S_y)
    print(x)
