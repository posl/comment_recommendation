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
    print((s_x * g_y + g_x * s_y) / (s_y + g_y))

=======
Suggestion 3

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    x = (S_x * G_y + G_x * S_y) / (S_y + G_y)
    print(x)

=======
Suggestion 4

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + S_x * G_y) / (S_y + G_y))

=======
Suggestion 5

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + G_y * S_x) / (S_y + G_y))

=======
Suggestion 6

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(G_x - (G_x - S_x) * G_y / (G_y + S_y))

=======
Suggestion 7

def main():
    Sx, Sy, Gx, Gy = input().split()
    Sx, Sy, Gx, Gy = int(Sx), int(Sy), int(Gx), int(Gy)
    print((Gx*Sy + Sx*Gy)/(Sy + Gy))

main()
