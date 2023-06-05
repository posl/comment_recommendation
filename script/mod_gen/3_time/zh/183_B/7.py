def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    print((g_x * s_y + s_x * g_y) / (g_y + s_y))

if __name__ == '__main__':
    main()