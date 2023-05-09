Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + S_y * G_x) / (S_y + G_y))

=======
Suggestion 2

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(S_x + (G_x - S_x) * S_y / (S_y + G_y))

=======
Suggestion 3

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y + S_x*G_y)/(S_y + G_y))

=======
Suggestion 4

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y + G_x*S_y)/(S_y+G_y))

=======
Suggestion 5

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(S_x+(G_x-S_x)*(S_y/(S_y+G_y)))

=======
Suggestion 6

def main():
    sx,sy,gx,gy = map(int,input().split())
    print((sx*gy+gx*sy)/(sy+gy))

=======
Suggestion 7

def solve(S_x, S_y, G_x, G_y):
    return (G_x*S_y + S_x*G_y)/(S_y+G_y)
