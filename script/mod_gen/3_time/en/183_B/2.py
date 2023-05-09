def main():
    S_x, S_y, G_x, G_y = map(int, input().split())
    if S_x == G_x:
        print(S_x)
    else:
        print((S_x * G_y + G_x * S_y) / (S_y + G_y))
main()

if __name__ == '__main__':
    main()