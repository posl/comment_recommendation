def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    # (G_x - S_x) / (x - S_x) = (G_y - S_y) / (0 - S_y)
    # (G_x - S_x) / (x - S_x) = G_y / S_y
    # (G_x - S_x) / (x - S_x) = G_y / S_y
    # (G_x - S_x) * S_y = (x - S_x) * G_y
    # (G_x - S_x) * S_y + S_x * (x - S_x) = G_y * (G_x - S_x)
    # (G_x - S_x) * S_y + S_x * x - S_x * S_x = G_y * (G_x - S_x)
    # (G_x - S_x) * S_y + S_x * x = G_y * (G_x - S_x) + S_x * S_x
    # (G_x - S_x) * S_y = G_y * (G_x - S_x) + S_x * S_x - S_x * x
    # (G_x - S_x) * S_y = G_y * (G_x - S_x) + S_x * (S_x - x)
    # x = (G_y * (G_x - S_x) + S_x * S_x) / (G_x - S_x + S_y)
    x = (G_y * (G_x - S_x) + S_x * S_x) / (G_x - S_x + S_y)
    print(x)
