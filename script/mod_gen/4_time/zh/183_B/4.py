def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    x = (S_x * G_y + G_x * S_y) / (S_y + G_y)
    print(x)

if __name__ == '__main__':
    solve()