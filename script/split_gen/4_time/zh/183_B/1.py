def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    ans = s_x + (g_x - s_x) * s_y / (s_y + g_y)
    print(ans)
