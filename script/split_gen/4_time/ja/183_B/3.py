def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    print(S_x + ((S_y * (G_x - S_x)) / (S_y + G_y)))
