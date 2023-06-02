Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s_x,s_y,g_x,g_y = map(int,input().split())
    print(s_x+(g_x-s_x)*(s_y/(s_y+g_y)))

=======
Suggestion 2

def main():
    S_x,S_y,G_x,G_y = map(int,input().split())
    print((G_x*S_y+S_x*G_y)/(G_y+S_y))

=======
Suggestion 3

def main():
    s_x,s_y,g_x,g_y = map(int,input().split())
    print((s_x*g_y+g_x*s_y)/(s_y+g_y))

=======
Suggestion 4

def main():
    line = input().split()
    S_x = int(line[0])
    S_y = int(line[1])
    G_x = int(line[2])
    G_y = int(line[3])
    print((S_x * G_y + S_y * G_x) / (S_y + G_y))

=======
Suggestion 5

def main():
    sx,sy,gx,gy = map(int,input().split())
    print(sx+(gx-sx)*sy/(sy+gy))

=======
Suggestion 6

def main():
    # 输入
    S_x, S_y, G_x, G_y = map(int, input().split())
    # 计算
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))

=======
Suggestion 7

def main():
    s_x,s_y,g_x,g_y = map(int,input().split())
    print((g_x*s_y+s_x*g_y)/(s_y+g_y))

=======
Suggestion 8

def main():
    S_x,S_y,G_x,G_y = map(int,input().split())
    print((S_x*G_y+S_y*G_x)/(S_y+G_y))

=======
Suggestion 9

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x*S_y+G_y*S_x)/(G_y+S_y))

=======
Suggestion 10

def main():
    #读取输入
    S_x, S_y, G_x, G_y = map(int, input().split())
    #计算
    x = (S_x*G_y + S_y*G_x)/(S_y + G_y)
    #输出
    print(x)
