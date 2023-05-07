def main():
    S_x, S_y, G_x, G_y = map(float, input().split())
    ans = (S_x * G_y + G_x * S_y) / (S_y + G_y)
    print(ans)
