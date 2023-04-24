Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((S_x * G_y + G_x * S_y) / (S_y + G_y))

=======
Suggestion 2

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + S_x * G_y) / (S_y + G_y))

=======
Suggestion 3

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    ans = (G_x * S_y + S_x * G_y) / (S_y + G_y)
    print(ans)

=======
Suggestion 4

def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print((G_x * S_y + S_x * G_y) / (S_y + G_y))
main()

=======
Suggestion 5

def main():
    S_x, S_y, G_x, G_y = map(float, input().split())
    ans = (S_x * G_y + G_x * S_y) / (S_y + G_y)
    print(ans)

=======
Suggestion 6

def f(x):
    return (Gy - Sy) / (Gx - Sx) * x + (Sx * Gy - Sy * Gx) / (Sx - Gx)

Sx, Sy, Gx, Gy = map(int, input().split())
print(f(0))
