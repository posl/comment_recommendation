def solve():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(S_x + (G_x - S_x) * S_y / (S_y + G_y))

if __name__ == '__main__':
    solve()