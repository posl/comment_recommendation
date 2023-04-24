Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + S_x * G_y) / (S_y + G_y))

=======
Suggestion 2

def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    print(s_x + (g_x - s_x) * s_y / (s_y + g_y))

=======
Suggestion 3

def main():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Sx*Gy+Gx*Sy)/(Sy+Gy))

=======
Suggestion 4

def solve():
    sx, sy, gx, gy = map(int, input().split())
    print((sx * gy + gx * sy) / (sy + gy))

=======
Suggestion 5

def solve():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Gx*Sy+Sx*Gy)/(Sy+Gy))

=======
Suggestion 6

def main():
    sx, sy, gx, gy = map(int, input().split())
    print((sx*gy+sy*gx)/(sy+gy))

=======
Suggestion 7

def solve():
    Sx, Sy, Gx, Gy = map(int, input().split())
    print((Sx*Gy + Gx*Sy)/(Sy+Gy))

=======
Suggestion 8

def solve():
    sx, sy, gx, gy = map(int, input().split())
    ans = sx + (gx - sx) * (sy / (sy + gy))
    print(ans)
