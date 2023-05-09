def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    x = g_x - g_y * (s_x - g_x) / (s_y + g_y)
    print(x)

if __name__ == '__main__':
    main()