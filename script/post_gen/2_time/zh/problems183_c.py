Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + G_y * S_x) / (G_y + S_y))

=======
Suggestion 2

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))

=======
Suggestion 3

def f(x):
    return ((x-sx)*(gy-sy)/(gx-sx)+sy)
sx,sy,gx,gy=map(int,input().split())
print(f(gx))

=======
Suggestion 4

def solve(S_x,S_y,G_x,G_y):
    return (S_x*G_y+S_y*G_x)/(G_y+S_y)

=======
Suggestion 5

def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + S_y * G_x) / (S_y + G_y))

=======
Suggestion 6

def ball():
    s_x,s_y,g_x,g_y = map(int,input().split())
    #print(s_x,s_y,g_x,g_y)
    x = (s_y*g_x + s_x*g_y)/(g_y+s_y)
    print(x)

ball()

=======
Suggestion 7

def main():
    S_x,S_y,G_x,G_y = map(int,input().split())
    print((G_x*S_y-S_x*G_y)/(G_y-S_y))

=======
Suggestion 8

def solve():
    line = input().split()
    S_x = int(line[0])
    S_y = int(line[1])
    G_x = int(line[2])
    G_y = int(line[3])
    x = (G_x*S_y + G_y*S_x)/(S_y + G_y)
    print(x)

=======
Suggestion 9

def main():
    sx,sy,gx,gy = map(int,input().split())
    x = sx + (gx-sx)*sy/(sy+gy)
    print(x)

=======
Suggestion 10

def main():
    x1,y1,x2,y2 = map(int,input().split())
    print((x1*y2-x2*y1)/(y2-y1))
