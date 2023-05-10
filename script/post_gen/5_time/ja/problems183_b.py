Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(G_x - (G_y / (S_y + G_y)) * (G_x - S_x))

=======
Suggestion 2

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y + G_x*S_y)/(S_y+G_y))

=======
Suggestion 3

def main():
    sx, sy, gx, gy = map(int, input().split())
    if sx < gx:
        print(sx + (gx - sx) * sy / (sy + gy))
    else:
        print(sx - (sx - gx) * sy / (sy + gy))

=======
Suggestion 4

def main():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Gx * Sy + Sx * Gy) / (Sy + Gy))

=======
Suggestion 5

def main():
    sx, sy, gx, gy = map(int, input().split())
    if sx > gx:
        gx, sx = sx, gx
        gy, sy = sy, gy
    print(sx + (gx - sx) * sy / (sy + gy))

=======
Suggestion 6

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y + S_x*G_y)/(S_y + G_y))

=======
Suggestion 7

def solve():
    sx,sy,gx,gy = map(int,input().split())
    print((sx*gy+gx*sy)/(sy+gy))

=======
Suggestion 8

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    x = (S_y * G_x + S_x * G_y) / (S_y + G_y)
    print(x)

=======
Suggestion 9

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))
