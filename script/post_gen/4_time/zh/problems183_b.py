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
    ans = s_x + (g_x - s_x) * s_y / (s_y + g_y)
    print(ans)

=======
Suggestion 3

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x*G_y + G_x*S_y)/(S_y + G_y))

=======
Suggestion 4

def main():
    S_x, S_y, G_x, G_y = map(int,input().split())
    print(S_x + (G_x - S_x) * S_y / (S_y + G_y))

=======
Suggestion 5

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    x = (S_x * G_y + G_x * S_y) / (S_y + G_y)
    print(x)

=======
Suggestion 6

def solve():
    S_x,S_y,G_x,G_y = map(int,input().split())
    print(G_x-(G_y*S_x/(S_y+G_y)))

=======
Suggestion 7

def main():
    s = input()
    x1, y1, x2, y2 = map(int, s.split())
    x = (x2 * y1 + x1 * y2) / (y1 + y2)
    print(x)

=======
Suggestion 8

def main():
    sx,sy,gx,gy = map(int,input().split())
    print((sx*gy + gx*sy)/(sy+gy))
