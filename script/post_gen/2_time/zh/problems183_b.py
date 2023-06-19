Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())

    print(S_x + (G_x - S_x) * S_y / (S_y + G_y))

=======
Suggestion 2

def main():
    sx,sy,gx,gy = map(int,input().split())
    print((sx*gy+gx*sy)/(sy+gy))

=======
Suggestion 3

def main():
    S_x,S_y,G_x,G_y = map(int,input().split())
    x = S_x - (S_y * (S_x - G_x) / (S_y + G_y))
    print(x)

=======
Suggestion 4

def solve():
    sx,sy,gx,gy = map(int, input().split())
    ans = sx + sy * (gx - sx) / (sy + gy)
    print(ans)

=======
Suggestion 5

def main():
    sx, sy, gx, gy = map(int, input().split())
    print((sx * gy + sy * gx) / (sy + gy))

=======
Suggestion 6

def main():
    S_x,S_y,G_x,G_y=map(int,input().split())
    print((S_x*G_y+S_y*G_x)/(S_y+G_y))

=======
Suggestion 7

def solve():
    sx, sy, gx, gy = map(int, input().split())
    print(sx + (gx - sx) * sy / (sy + gy))

=======
Suggestion 8

def get_x(sx, sy, gx, gy):
    return (sx * gy + sy * gx) / gy

=======
Suggestion 9

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(S_x + (G_x - S_x) * S_y / (S_y + G_y))
