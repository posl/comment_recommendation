Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + S_x * G_y) / (S_y + G_y))

=======
Suggestion 2

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y+G_x*S_y)/(S_y+G_y))

=======
Suggestion 3

def main():
    sx,sy,gx,gy=map(int,input().split())
    print((sx*gy+gx*sy)/(sy+gy))

=======
Suggestion 4

def solve():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Gx * Sy + Sx * Gy) / (Sy + Gy))

=======
Suggestion 5

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y + S_y*G_x)/(S_y + G_y))

=======
Suggestion 6

def main():
    S_x,S_y,G_x,G_y = map(int,input().split())
    print(G_x-((G_y-S_y)*(G_x-S_x))/(G_y+S_y))

=======
Suggestion 7

def get_x(sx, sy, gx, gy):
    return (sx * gy + sy * gx) / (sy + gy)

=======
Suggestion 8

def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    print((g_x * s_y + s_x * g_y) / (g_y + s_y))

=======
Suggestion 9

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(G_x - (G_y * (G_x - S_x)) / (G_y + S_y))

=======
Suggestion 10

def solve():
    s_x,s_y,g_x,g_y = map(int,input().split())
    print((s_x*g_y+g_x*s_y)/(s_y+g_y))
