def main():
    S_x, S_y, G_x, G_y = [int(x) for x in input().split()]
    print((S_x*G_y + G_x*S_y)/(S_y + G_y))

if __name__ == '__main__':
    main()