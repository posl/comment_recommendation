def main():
    line = input().split()
    S_x = int(line[0])
    S_y = int(line[1])
    G_x = int(line[2])
    G_y = int(line[3])
    print((S_x * G_y + S_y * G_x) / (S_y + G_y))

if __name__ == '__main__':
    main()