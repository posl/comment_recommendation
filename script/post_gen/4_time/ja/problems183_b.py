Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y+G_y*S_x)/(S_y+G_y))

=======
Suggestion 2

def main():
    sx, sy, gx, gy = map(int, input().split())
    print((sx * gy + sy * gx) / (sy + gy))

=======
Suggestion 3

def main():
    sx, sy, gx, gy = map(int, input().split())
    print((sx*gy+gx*sy)/(sy+gy))

=======
Suggestion 4

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(S_x + ((S_y * (G_x - S_x)) / (S_y + G_y)))

=======
Suggestion 5

def solve():
    sx, sy, gx, gy = map(int, input().split())
    print((sx*gy+gx*sy)/(sy+gy))

=======
Suggestion 6

def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    x = g_x - g_y * (s_x - g_x) / (s_y + g_y)
    print(x)

=======
Suggestion 7

def main():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print(Sx+(Gx-Sx)*Sy/(Sy+Gy))
